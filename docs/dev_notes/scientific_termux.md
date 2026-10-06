# Scientific Python on Termux for `pocket-cocktail-party`

This note records the successful setup of a scientific Python environment for
`pocket-cocktail-party` on Android through Termux. It includes the failed paths,
because those explain several choices in the working procedure.

## Verified platform and result

The successful build used:

- Android on `aarch64` (`arm64-v8a`)
- Termux Python 3.14
- a virtual environment with access to Termux's system Python packages
- Termux-packaged NumPy and SciPy
- locally built scikit-learn, SoundFile dependencies, kiwisolver, ContourPy,
  Pillow, and Matplotlib

The final checks established:

- NumPy 2.4.4 imports
- SciPy 1.18.1 imports
- scikit-learn 1.9.1 imports, including `FastICA`
- SoundFile 0.14.0 imports and finds libsndfile 1.2.2
- kiwisolver 1.5.1 imports
- Matplotlib 3.11.2 imports and renders through the noninteractive `Agg` backend
- `python -m pip check` reports `No broken requirements found.`
- a real sine/cosine PNG was written and successfully displayed by Android

Versions below are observations from this build, not permanent pins.

## Why the environment uses system site packages

Installing the complete stack from PyPI in an ordinary isolated venv caused
pip to attempt native NumPy builds. On Termux, the more reliable foundation was
the NumPy and SciPy packages already adapted for Android by Termux.

Create the environment with system packages visible:

```bash
cd ~/my_repos_dwb/pocket-cocktail-party

python -m venv --system-site-packages .venv_pocketcp_sys
source .venv_pocketcp_sys/bin/activate

python -c 'import sys; print(sys.executable)'
```

Expected executable:

```text
/data/data/com.termux/files/home/my_repos_dwb/pocket-cocktail-party/.venv_pocketcp_sys/bin/python
```

The activation target is the file `bin/activate`, not the venv directory:

```bash
source .venv_pocketcp_sys/bin/activate
```

## Termux mirror

The working mirror reported in the installation output was:

```text
https://plug-mirror.rcac.purdue.edu/termux/termux-main
```

If the configured mirror is unavailable or stale, select another with:

```bash
termux-change-repo
```

## Native and Termux-packaged prerequisites

Install the scientific foundation and build toolchain with Termux's package
manager:

```bash
pkg update
pkg install -y python python-numpy python-scipy
pkg install -y clang make cmake ninja pkg-config
pkg install -y libsndfile freetype libpng libffi libjpeg-turbo zlib
```

Some library packages bring in further runtime dependencies automatically,
including OpenBLAS and audio codecs.

### A failed package-manager command

This combined command was not valid because `meson` and `python-cython` were not
available under those names in the configured Termux repository:

```bash
pkg install -y clang make cmake ninja pkg-config meson python-cython
```

Install the native tools with `pkg`, then install the Python build tools with
pip inside the activated venv.

## Python build tools

With `.venv_pocketcp_sys` activated:

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install meson meson-python Cython joblib threadpoolctl
python -m pip install pybind11 setuptools-scm
```

Observed tool versions included:

```text
pip             26.2.1
setuptools      84.0.0
wheel           0.48.0
meson           1.12.0
meson-python    0.21.1
Cython          3.3.0
pybind11        3.1.0
setuptools-scm  10.3.4
```

Useful checks:

```bash
clang --version
cmake --version
ninja --version
meson --version
```

## Timestamped build logs

For commands piped through `tee`, enable pipeline failure propagation and save
the pip process's status immediately. Epoch timestamps make build attempts
lexically sortable and prevent one attempt from overwriting another.

```bash
set -o pipefail

my_logfile="pocketcp_COMPONENT_build_$(date +'%s').log"
python -u -m pip install PACKAGE \
  --no-build-isolation \
  2>&1 | tee "$my_logfile"
retval=${PIPESTATUS[0]}

echo "pip exit status: ${retval}"
echo "logfile: ${my_logfile}"
```

Do not run another command before saving `${PIPESTATUS[0]}`: every new pipeline
replaces the array.

To recover the newest log when the filename convention is consistent:

```bash
my_logfile=$(
  find . -maxdepth 1 -type f \
    -name 'pocketcp_COMPONENT_build_*.log' \
    -print |
  sort |
  tail -n 1
)
printf 'logfile: %s\n' "$my_logfile"
```

Build logs should be ignored rather than committed. A suitable rule is:

```gitignore
pocketcp_*_build*.log
```

## scikit-learn

The PyPI source distribution built successfully against Termux's NumPy and
SciPy when build isolation was disabled:

```bash
set -o pipefail
my_logfile="pocketcp_scikit_learn_build_$(date +'%s').log"

python -u -m pip install 'scikit-learn>=1.4' \
  --no-build-isolation \
  2>&1 | tee "$my_logfile"
retval=${PIPESTATUS[0]}

echo "scikit-learn pip exit status: ${retval}"
echo "logfile: ${my_logfile}"
```

Verify both the package and the compiled decomposition extension:

```bash
python -c 'from sklearn.decomposition import FastICA; import sklearn; print(sklearn.__version__, FastICA)'
```

Observed result:

```text
1.9.1 <class 'sklearn.decomposition._fastica.FastICA'>
```

## SoundFile and libsndfile

Install the native library first, then the Python package:

```bash
pkg install -y libsndfile freetype libpng libffi
python -u -m pip install 'soundfile>=0.12'
```

The `cffi` dependency built successfully on Termux.

Verify the wrapper and native library together:

```bash
python - <<'PY'
import soundfile as sf

print("SoundFile:", sf.__version__)
print("libsndfile:", sf.__libsndfile_version__)
PY
```

Observed result:

```text
SoundFile: 0.14.0
libsndfile: 1.2.2
```

## Matplotlib

### First failure: missing `cppy`

The first Matplotlib attempt reached kiwisolver metadata generation and failed
with:

```text
RuntimeError: Missing setup required dependencies: cppy.
error: metadata-generation-failed
```

This was a consequence of using `--no-build-isolation`: build prerequisites
that an isolated build environment would normally install must already exist in
the active environment.

Install and verify `cppy`:

```bash
python -m pip install cppy

python - <<'PY'
from importlib.metadata import version
print("cppy:", version("cppy"))
PY
```

Observed version: 1.3.1.

### Build kiwisolver separately

Building kiwisolver separately made its failure or success independent of the
larger Matplotlib build:

```bash
set -o pipefail
my_logfile="pocketcp_kiwisolver_build_$(date +'%s').log"

python -u -m pip install 'kiwisolver>=1.3.1' \
  --no-build-isolation \
  2>&1 | tee "$my_logfile"
retval=${PIPESTATUS[0]}

echo "kiwisolver pip exit status: ${retval}"
echo "logfile: ${my_logfile}"
```

Verify:

```bash
python - <<'PY'
import kiwisolver
print("kiwisolver:", kiwisolver.__version__)
PY
```

Observed result: kiwisolver 1.5.1, built as a CPython 3.14 Android ARM64 wheel.

### Successful Matplotlib build

Ensure the image libraries are present:

```bash
pkg install -y libjpeg-turbo zlib
```

Then build Matplotlib:

```bash
set -o pipefail
my_logfile="pocketcp_matplotlib_build_$(date +'%s').log"

python -u -m pip install 'matplotlib>=3.8' \
  --no-build-isolation \
  2>&1 | tee "$my_logfile"
retval=${PIPESTATUS[0]}

echo "matplotlib pip exit status: ${retval}"
echo "logfile: ${my_logfile}"
```

This successfully built Matplotlib 3.11.2, ContourPy 1.4.0, and Pillow 12.3.0.
The repeated `Preparing metadata ... still running` messages were progress
reports, not evidence of a hang.

## Verification

Check the core imports and versions:

```bash
python - <<'PY'
import numpy
import scipy
import sklearn
import soundfile
import matplotlib
import kiwisolver

print("numpy:", numpy.__version__)
print("scipy:", scipy.__version__)
print("sklearn:", sklearn.__version__)
print("soundfile:", soundfile.__version__)
print("matplotlib:", matplotlib.__version__)
print("kiwisolver:", kiwisolver.__version__)
PY

python -m pip check
```

### Rendering smoke test

The following test exercises NumPy, Matplotlib, font rendering, PNG output,
and the Android image decoder:

```bash
mkdir -p figures

python - <<'PY'
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 400)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label="sin(x)")
ax.plot(x, np.cos(x), label="cos(x)")
ax.set_title("Matplotlib on Termux")
ax.legend()
fig.savefig("figures/termux_matplotlib_smoke.png", dpi=150)

print("matplotlib:", matplotlib.__version__)
print("backend:", matplotlib.get_backend())
print("wrote: figures/termux_matplotlib_smoke.png")
PY
```

Observed backend: `Agg`.

Copy the result to Android shared storage:

```bash
cp figures/termux_matplotlib_smoke.png ~/storage/downloads/
stat ~/storage/downloads/termux_matplotlib_smoke.png
```

If `~/storage` has not been initialized:

```bash
termux-setup-storage
```

Android's aggregate Downloads view may lag behind direct filesystem changes
because its media/document index is cached. Navigating directly to **Internal
storage → Download** revealed the image immediately in this test. This was a UI
indexing delay, not incomplete Python output or heredoc buffering.

With an X11 setup and `feh` available, the suitably Unix-shaped command would
be:

```bash
feh figures/termux_matplotlib_smoke.png &
```

Use `disown` afterward if the viewer should survive the current shell.

## Heredoc notes

A quoted heredoc delimiter prevents the shell from expanding variables,
commands, arithmetic, and backslashes in the body:

```bash
python - <<'PY'
print("The shell passes this text to Python's standard input.")
PY
```

The delimiter terminates shell input collection; it does not control Python's
output buffering. Python flushes ordinary buffered output on normal exit, and
`savefig()` finishes writing before it returns.

For inert scratch notes, either of these works:

```bash
cat >/dev/null <<'EOF'
Arbitrary text, including shell or Python code.
It is input to cat and is not executed.
EOF
```

```bash
: <<'EOF'
Arbitrary text consumed as a redirection for the shell's no-op command.
EOF
```

The closing delimiter must appear alone and exactly as written. If it occurs in
the pasted material, the heredoc ends and later lines may be interpreted as
shell commands. `<<-EOF` additionally strips leading tab characters, but not
spaces.

## Known unsuccessful approaches

1. **Ordinary isolated venv plus PyPI for everything:** pip attempted native
   NumPy builds instead of using Termux's working NumPy/SciPy packages.
2. **Installing `meson` and `python-cython` with `pkg`:** those package names
   were unavailable; installing Meson and Cython with pip worked.
3. **First Matplotlib build:** kiwisolver metadata generation failed because
   `cppy` was missing while build isolation was disabled.
4. **Looking only in Android's aggregate Downloads view:** the copied PNG was
   temporarily absent there even though `stat` showed a complete 62,067-byte
   file. Direct navigation to the Download directory showed and opened it.

## Next: install this project

With the scientific stack verified, install the project itself in editable
mode. The release extra is the intended next step; disabling build isolation
keeps the build attached to the working Termux environment.

```bash
cd ~/my_repos_dwb/pocket-cocktail-party
source .venv_pocketcp_sys/bin/activate
set -o pipefail

my_logfile="pocketcp_editable_build_$(date +'%s').log"
python -u -m pip install -e '.[release]' \
  --no-build-isolation \
  2>&1 | tee "$my_logfile"
retval=${PIPESTATUS[0]}

echo "editable-install pip exit status: ${retval}"
echo "logfile: ${my_logfile}"
```

Do not proceed on a nonzero status. On success, verify that the import resolves
to this checkout:

```bash
python - <<'PY'
from importlib.metadata import version
import pocket_cocktail_party as pcp

print("module:", pcp.__file__)
print("package version:", pcp.__version__)
print("distribution version:", version("pocket-cocktail-party"))
PY
```

After that, run the repository's synthetic smoke test:

```bash
python scripts/run_synthetic_0p0.py
```

Inspect any generated audio and figures, then run the applicable test suite.
Development extras such as JupyterLab can be installed separately so that a
large optional dependency does not obscure whether the package itself works.

## Compact reconstruction recipe

For a fresh Termux installation, the working sequence is:

```bash
cd ~/my_repos_dwb/pocket-cocktail-party

pkg update
pkg install -y python python-numpy python-scipy
pkg install -y clang make cmake ninja pkg-config
pkg install -y libsndfile freetype libpng libffi libjpeg-turbo zlib

python -m venv --system-site-packages .venv_pocketcp_sys
source .venv_pocketcp_sys/bin/activate

python -m pip install --upgrade pip setuptools wheel
python -m pip install \
  meson meson-python Cython joblib threadpoolctl \
  pybind11 setuptools-scm cppy

python -m pip install 'scikit-learn>=1.4' --no-build-isolation
python -m pip install 'soundfile>=0.12'
python -m pip install 'kiwisolver>=1.3.1' --no-build-isolation
python -m pip install 'matplotlib>=3.8' --no-build-isolation

python -m pip check
```

The longer sections above remain the authoritative troubleshooting record; this
compact recipe is only the successful path distilled from it.
