# Pocket Cocktail Party

**Blind Source Separation through Geometry, Harmonics, and Signal Mixing**

`pocket-cocktail-party` is a portfolio and learning project exploring the classic **cocktail party problem**: when several sound sources are mixed together in microphone recordings, how much can we recover about the original sources?

The project begins with classical **Independent Component Analysis (ICA)** and deliberately builds outward from clean synthetic assumptions toward messier real-world recordings.

If such is the nature of your business, you might like to check out some 
[Intellectual Property notes for this project](https://github.com/bballdave025/dwb-ip-notes/blob/main/IP_Plus_Vision_-_Pocket_Cocktail_Party_BSS_ICA_2026-06-24.md). <!-- May Doug have mercy on your soul! -->

## Project arc

1. **Synthetic pentagon band**
   - Five sources: voice, violin, guitar, bass/piano, drums.
   - Five close microphones arranged on a regular pentagon.
   - Optional sixth microphone at the center or above the center.
   - Known sources and known mixing matrix, so recovery quality can be measured.

2. **Father's Day family recording**
   - Three microphones recording Dave, Anastasia, Julie, and room/car noise.
   - Real movement, automatic gain control, microphone bumps, and imperfect claps.
   - Useful because it violates the clean assumptions in interesting ways.

3. **Future family / phone array experiments**
   - More voices.
   - More microphones.
   - Similar voices and overlapping speech.
   - Turn-taking versus chaos.

## Why this is not just an ICA demo

A simple demo usually starts with arbitrary source signals and an arbitrary mixing matrix.

This project makes the assumptions explicit:

- geometry generates the mixing matrix,
- amplitude attenuation is based on distance,
- musical sources have overtone structure,
- real recordings include drift, AGC, movement, and noise,
- failure modes are part of the result.

The point is not merely:

> Can I run FastICA?

The better questions are:

> When does classical ICA work?
>
> When does it break?
>
> Which assumptions did modern learned source-separation systems buy with data, priors, and computation?

## Data Ethics and Consent

This repository contains both synthetic audio experiments and recordings of human participants.

All human recordings included in the project were collected with informed consent. Public versions of consent forms are provided in `docs/consent/`. Original signed forms are retained privately by the project owner and are not included in the repository.

This project is a personal educational and portfolio project rather than an IRB-reviewed academic study. Nevertheless, the project follows basic principles of responsible data collection and participant consent, particularly when working with identifiable voice recordings and recordings involving a minor participant.

## Mathematical model

Using Einstein notation, the simple instantaneous linear model is

$$
X^m(t)=A^m_i S^i(t) + \varepsilon^m(t),
$$

where

- $X^m(t)$ is microphone channel $m$,
- $S^i(t)$ is source signal $i$,
- $A^m_i$ is the mixing coefficient from source $i$ into microphone $m$,
- $\varepsilon^m(t)$ collects noise, echo, nonlinearities, and modeling error.

The classical determined or overdetermined case assumes

$$
M \ge N,
$$

where $M$ is the number of microphones and $N$ is the number of sources.

ICA also assumes statistical independence:

$$
p_S(s^i)=\prod_i p_i(s^i).
$$

That is stronger than zero covariance.

## Synthetic experiment 0.0

The first synthetic test uses a **C major add 9** style chord.

| Source | Note | Frequency |
|---|---:|---:|
| Piano bass | C2 | 65.41 Hz |
| Guitar | G3 | 196.00 Hz |
| Voice | E4 | 329.63 Hz |
| Violin | D5 | 587.33 Hz |
| Snare | C4-centered burst | ~261.63 Hz center |


Each pitched source is generated as harmonic partials:

$$
s^{(i)}(t)=e^{(i)}(t)\sum_{k=1}^{K} c^{(i)}_k \sin(2\pi k f^{(i)} t).
$$

The snare drum is modeled in this Experiment 0.0 experiment as a sort of random pitched source. In further experiments, it is 

The synthetic ensemble is loosely inspired by Yellowcard-style instrumentation: voice, violin, guitar, bass, and drums. Go [Yellowcard](https://www.yellowcardband.com)!

This project is not affiliated with or endorsed by Yellowcard.

## Geometry

Our synthetic band can be represented simply as situation like this:

```text
     voice     guitar


violin             snare

           bass
```

Where our bass part is being played by a piano.

For a regular pentagon, the diagonal is $\varphi$ times the side length:

$$
\varphi=\frac{1+\sqrt{5}}{2}\approx 1.618.
$$

A simple starting bleed matrix is:

| Relationship | Amplitude |
|---|---:|
| own mic | 1.000 |
| adjacent mic | 0.200 |
| next-nearest mic | 0.124 |

because

$$
0.124 \approx \frac{0.200}{1.618}.
$$

**For a microphone at the center of the pentagon and in the same plane**, the distance to any instrument is the circumradius. Dividing the pentagon into five triangles, we get interior triangles, each of which has as a side side length (by definition) a circumradius. Se will denote the distance covered by a circumradius as $R$, and each interior angle is $\frac{2\pi}{5}$. The other two angles of each interior (isosceles) triangle are each $\left(\frac{1}{2}\right)\left(\pi - \frac{2\pi}{5} \right)$, using the fact that the interior angles of a triangle sum to $\pi$ radians. If we take $L$ as the distance between two adjacent instruments, by the law of sines,

$$
\frac{R}{\sin \left(\frac{3\pi}{10}\right)} = \frac{L}{\sin \left(\frac{3\pi}{5}\right)}
$$

Which means<sup>[1]</sup>,

$$
\frac{R}{L} = \frac{\frac{1+\sqrt{5}}{4}}{\frac{\sqrt{10 + 2 \sqrt{5}}}{4}}
$$

**For an overhead microphone above the pentagon center**,

$$
r_{\mathrm{overhead}}=\sqrt{R^2+h^2},
$$

where $h$ is the height of the microphone normal to the plane of the pentagon, so every source is equally distant from that overhead microphone.

## Source-First Modeling

This project intentionally separates source generation from microphone observation.

The synthetic instrument tracks are created first as independent source signals:

```text
sound_bass_piano
sound_snare
sound_guitar
sound_violin
sound_voice
```

These tracks represent the idealized source coordinates (S^i(t)). Each one is generated before any microphone geometry is applied.

The microphone recordings are then generated as mixtures of those sources:

$$
X^m(t)=A^m_iS^i(t)
$$

where $A^m_i$ is a geometry-derived mixing matrix. In other words, the project does not begin with arbitrary mixed signals. It first creates interpretable sources, then places those sources into a spatial microphone model.

For example, a microphone near the bass/piano source might receive:

```text
mic_bass_piano =
    1.000 * sound_bass_piano
  + 0.200 * sound_violin
  + 0.200 * sound_snare
  + 0.124 * sound_voice
  + 0.124 * sound_guitar
```

This explicit form is useful pedagogically because it shows exactly what the mixing model means. In the implementation, the same operation is represented as a matrix multiplication:

$$
\mathbf{X} = \mathbf{A}\mathbf{S}
$$

or, equivalently, in Einstein notation,

$$
X^i{}_j=A^i{}_mS^m{}_j
$$

Here the repeated index $m$ is summed, while $i$ and $j$ remain as the free
indices of the result. Some might be more accustomed to seeing such an operation as

$$
X = [x_{ij}], \qquad A = [a_{im}], \qquad S = [s_{mj}], \\
\mathbf{X} = \mathbf{A}\mathbf{S} \Leftrightarrow x_{ij} = \sum_{m=1}^d a_{im} s_{mj}
$$

where $d$ is the dimensionality of $\mathbf{A}$'s rows as well as that of $\mathbf{S}$'s columns.

All representations of matrix multiplication shown here are equivalent.

### Source type &mdash; harmonic

As they were in Experiment 0.0, the harmonic sources (pitched instruments) is generated as harmonic partials:

$$
s^{(i)}(t)=e^{(i)}(t)\sum_{k=1}^{K} c^{(i)}_k \sin(2\pi k f^{(i)} t)
$$

where the superscript, ${}^{(i)}$ is put in parentheses to show it wonn't participate in any sums.

### Source type &mdash; snare

After Experiment 0.0, the snare source is intentionally modeled differently 
from the pitched instruments. Rather than using a harmonic overtone array, 
it is generated as a short broadband noise burst with exponential decay, 
optionally mixed with a weak C4-centered resonant tone. This makes the snare 
useful as a non-Gaussian, transient-heavy source for ICA.

## Repository layout

```text
pocket-cocktail-party/
├── data/
│   ├── raw/                 # local audio only; not committed
│   ├── interim/             # aligned/resampled files
│   └── processed/           # separated components, metrics
├── docs/
│   ├── consent/             # Public consent documentation
│   ├── dev_notes/           # Development notes
│   ├── experimental_notes/  # Experiment logs and results
│   └── project_admin/
├── figures/
├── notebooks/
├── scripts/
├── src/pocket_cocktail_party/
└── tests/
```

## Motivation




## Quick start

```bash
git clone https://github.com/bballdave025/pocket-cocktail-party.git
cd pocket-cocktail-party

python -m venv .venv
. .venv/bin/activate

pip install -e ".[dev]"
pytest
```

## First planned milestones

- [ ] Generate five synthetic sources.
- [ ] Build pentagon mixing matrix.
- [ ] Run `sklearn.decomposition.FastICA`.
- [ ] Score recovery against known synthetic sources.
- [ ] Import Father's Day recordings.
- [ ] Align channels using clap peaks.
- [ ] Run first real-recording ICA attempt.
- [ ] Write failure-mode notes.
- [ ] Discuss briefly the modern DNN solution approaches.

## Footnotes

[1]: For the calculation of $\sin \left(\frac{2\pi}{5}\right)$, the fact that the goal was to find interior angles of a regular polygon led immediately to the strategy of using methods involving roots of unity. After doing this, I had met 99.9% of the quota of algebra errors allowed by my brain before complete shutdown. Therefore, for the calculation of $sin \left(\frac{3\pi}{10}\right)$, I used what I'm now coining as the Tim Berners-Lee method &mdash; using the internet. You could use double- and triple-angle identities, but from what we've done, it would probably be best to bisect the interior angle of one of our RRL triangles in the interior of the pentagon, notice that we have a right triangle with one complementary angle being $\frac{3\pi}{10}$, drop a normal from the point where the pentagon side, L, was bisected to one of the circumradii... Actually, you can just go to the `bballdave025/pocket-cocktail-party/docs/math/pentagon_trig.md` to get all the details concerning the calculation of both sine values.