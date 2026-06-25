# Mathematical Details for the Pentagon

```text
        voice
          *
     *         *
 guitar       violin
     *         *
      snare  bass/piano

A regular pentagon is doing quiet geometry duty underneath the
mixing coefficients.
```

## Part 1: Roots of unity and the regular pentagon

The regular pentagon immediately suggests fifth roots of unity: five equally spaced points around the unit circle. Let

$$z = e^{2\pi i/5}.$$

Then

$$z^5 = 1,$$

so

$$z^5 - 1 = 0.$$

We already know that $z=1$ is one of the fifth roots of unity, corresponding to angle $0$. For the nontrivial fifth roots, we divide out the factor $z-1$. The polynomial long division is

```text
                   z^4 +  z^3 +  z^2 +  z + 1
        ------------------------------------
z - 1  )    z^5 + 0z^4 + 0z^3 + 0z^2 + 0z - 1
         - (z^5 -  z^4)
            ----------
                   z^4 + 0z^3
                - (z^4 -  z^3)
                   ----------
                          z^3 + 0z^2
                       - (z^3 -  z^2)
                          ----------
                                 z^2 + 0z
                              - (z^2 -  z)
                                 --------
                                        z - 1
                                     - (z - 1)
                                        -----
                                            0
```

Thus

$$z^5 - 1 = (z-1)(z^4+z^3+z^2+z+1).$$

For the nontrivial fifth roots, $z\ne 1$, so

$$z^4+z^3+z^2+z+1 = 0.$$

Also $z\ne 0$, so we may divide by $z^2$:

$$z^2+z+1+\frac{1}{z}+\frac{1}{z^2} = 0.$$

Now group the $z^2$-terms, the $z$-terms, and the constant term:

$$\left(z^2+\frac{1}{z^2}\right)+\left(z+\frac{1}{z}\right)+1 = 0.$$

Use the standard trick, remembered from some class somewhere:

$$x = z+\frac{1}{z}.$$

Then

$$x^2 = \left(z+\frac{1}{z}\right)^2 = z^2+2+\frac{1}{z^2},$$

so

$$z^2+\frac{1}{z^2} = x^2-2.$$

Substitute this into the grouped equation:

$$(x^2-2)+x+1 = 0.$$

Therefore

$$x^2+x-1 = 0.$$

Solving,

$$x = \frac{-1\pm\sqrt{5}}{2}.$$

Now connect this back to the unit circle. Since

$$z = e^{2\pi i/5},$$

we have

$$\frac{1}{z} = e^{-2\pi i/5}.$$

Therefore

$$z+\frac{1}{z} = e^{2\pi i/5}+e^{-2\pi i/5} = 2\cos\left(\frac{2\pi}{5}\right),$$

by

$$\cos \theta = \frac{e^{i \theta}+e^{-i \theta}}{2}.$$

So

$$x = 2\cos\left(\frac{2\pi}{5}\right).$$

The angle $2\pi/5$ lies in the first quadrant, so its cosine, the real part, is positive. Equivalently, from Euler's formula,

$$e^{i\theta} = \cos\theta+i\sin\theta,$$

we can see the real part of $e^{2\pi i/5}$ is positive. Thus we choose the positive root:

$$x = \frac{-1+\sqrt{5}}{2}.$$

Hence

$$2\cos\left(\frac{2\pi}{5}\right) = \frac{-1+\sqrt{5}}{2},$$

and therefore

$$\cos\left(\frac{2\pi}{5}\right) = \frac{\sqrt{5}-1}{4}.$$

Now compute the corresponding sine value:

$$\sin^2\left(\frac{2\pi}{5}\right) = 1-\cos^2\left(\frac{2\pi}{5}\right) = 1-\left(\frac{\sqrt{5}-1}{4}\right)^2.$$

Since

$$(\sqrt{5}-1)^2 = 5-2\sqrt{5}+1 = 6-2\sqrt{5},$$

we get

$$\sin^2\left(\frac{2\pi}{5}\right) = 1-\frac{6-2\sqrt{5}}{16} = \frac{16-(6-2\sqrt{5})}{16} = \frac{10+2\sqrt{5}}{16}.$$

The important sign is in the subtraction:

$$16-(6-2\sqrt{5}) = 16-6+2\sqrt{5} = 10+2\sqrt{5}.$$

So

$$\sin\left(\frac{2\pi}{5}\right) = \frac{\sqrt{10+2\sqrt{5}}}{4}.$$

In the regular pentagon, the central triangle formed by two circumradii $R$ and one side length $L$ has angles

$$\frac{3\pi}{10},\quad \frac{3\pi}{10},\quad \frac{2\pi}{5}.$$

By the law of sines,

$$\frac{R}{\sin(3\pi/10)} = \frac{L}{\sin(2\pi/5)}.$$

Thus

$$\frac{R}{L} = \frac{\sin(3\pi/10)}{\sin(2\pi/5)}.$$

Since, as shown in Part 2,

$$\sin\left(\frac{3\pi}{10}\right) = \cos\left(\frac{\pi}{5}\right) = \frac{1+\sqrt{5}}{4},$$

we get

$$\frac{R}{L} = \frac{\frac{1+\sqrt{5}}{4}}{\frac{\sqrt{10+2\sqrt{5}}}{4}} = \frac{1+\sqrt{5}}{\sqrt{10+2\sqrt{5}}}.$$

Equivalently, since the original numerator and denominator are positive,

$$\left(\frac{R}{L}\right)^2 = \frac{(1+\sqrt{5})^2}{10+2\sqrt{5}} = \frac{6+2\sqrt{5}}{10+2\sqrt{5}}.$$

Rationalizing,

$$\frac{6+2\sqrt{5}}{10+2\sqrt{5}}\cdot\frac{10-2\sqrt{5}}{10-2\sqrt{5}} = \frac{40+8\sqrt{5}}{80} = \frac{5+\sqrt{5}}{10}.$$

Therefore, taking the positive square root,

$$\frac{R}{L} = \sqrt{\frac{5+\sqrt{5}}{10}} = \frac{1}{10}\sqrt{50+10\sqrt{5}}.$$

So the circumradius of a regular pentagon with side length $L$ is

$$R = \frac{L}{10}\sqrt{50+10\sqrt{5}}.$$

### A rationalization-only route

The repo author, having taught college algebra and remedial math along with physics, physical science, and calculus, prefers to stay away from the "square it, then take its square root at the end" stuff for the sake of his students. The same final result can be reached by direct rationalization.

Go back to the expression

$$\frac{R}{L} = \frac{1+\sqrt{5}}{\sqrt{10+2\sqrt{5}}}.$$

Rationalize the denominator:

$$\frac{1+\sqrt{5}}{\sqrt{10+2\sqrt{5}}}\cdot\frac{\sqrt{10+2\sqrt{5}}}{\sqrt{10+2\sqrt{5}}} = \frac{(1+\sqrt{5})\sqrt{10+2\sqrt{5}}}{10+2\sqrt{5}}.$$

Factor the denominator:

$$10+2\sqrt{5} = 2(5+\sqrt{5}).$$

So

$$\frac{R}{L} = \frac{(1+\sqrt{5})\sqrt{10+2\sqrt{5}}}{2(5+\sqrt{5})}.$$

Now simplify the coefficient:

$$\frac{1+\sqrt{5}}{5+\sqrt{5}}.$$

Rationalize that little piece:

$$\frac{1+\sqrt{5}}{5+\sqrt{5}}\cdot\frac{5-\sqrt{5}}{5-\sqrt{5}} = \frac{(1+\sqrt{5})(5-\sqrt{5})}{25-5}.$$

The numerator is

$$(1+\sqrt{5})(5-\sqrt{5}) = 5-\sqrt{5}+5\sqrt{5}-5 = 4\sqrt{5}.$$

So

$$\frac{1+\sqrt{5}}{5+\sqrt{5}} = \frac{4\sqrt{5}}{20} = \frac{\sqrt{5}}{5}.$$

Therefore

$$\frac{R}{L} = \frac{1}{2}\cdot\frac{\sqrt{5}}{5}\cdot\sqrt{10+2\sqrt{5}}.$$

So

$$\frac{R}{L} = \frac{\sqrt{5}}{10}\sqrt{10+2\sqrt{5}}.$$

Combine the radicals:

$$\frac{R}{L} = \frac{1}{10}\sqrt{5(10+2\sqrt{5})}.$$

Thus

$$\frac{R}{L} = \frac{1}{10}\sqrt{50+10\sqrt{5}}.$$

Radical-expression costume change complete. No dirty tricks. The squaring route was valid because all necessary positivity assumptions were checked, but it still feels dirty.

## Part 2: A geometric and trigonometric route to $\sin(3\pi/10)$

### 2.1. Defining the central triangle

Consider the central isosceles triangle $\triangle ABC$ in the regular pentagon, where:

- $A$ is the center of the pentagon.
- $B$ and $C$ are adjacent vertices of the pentagon.
- $AB=AC=R$ are circumradii.
- $BC=L$ is one side of the pentagon.
- The central angle at $A$ is $2\pi/5$.
- The two base angles at $B$ and $C$ are both $3\pi/10$.

The angle sum is

$$\frac{2\pi}{5}+\frac{3\pi}{10}+\frac{3\pi}{10} = \frac{4\pi}{10}+\frac{3\pi}{10}+\frac{3\pi}{10} = \pi.$$

Bisect the apex angle at $A$ with the line segment $AD$, where $D$ lies on the base segment $BC$. Since $\triangle ABC$ is isosceles, $D$ is the midpoint of $BC$ and $AD$ is perpendicular to $BC$. Thus

$$DC = \frac{L}{2}.$$

The right triangle $\triangle ADC$ contains the following angles:

- $\angle DAC=\pi/5$.
- $\angle ADC=\pi/2$.
- $\angle ACD=3\pi/10$.

### 2.2. Dropping a normal

Drop a normal from $D$ to the line segment $AC$, meeting $AC$ at point $E$. This creates two smaller internal right triangles, $\triangle EDC$ and $\triangle ADE$.

Because the acute angles of a right triangle sum to $\pi/2$, and

$$\frac{\pi}{5}+\frac{3\pi}{10} = \frac{2\pi}{10}+\frac{3\pi}{10} = \frac{\pi}{2},$$

the same complementary angles appear throughout the smaller right triangles.

In $\triangle EDC$, we have

$$\angle DEC = \frac{\pi}{2},\qquad \angle ECD = \frac{3\pi}{10},\qquad \angle EDC = \frac{\pi}{5}.$$

In $\triangle ADE$, we have

$$\angle AED = \frac{\pi}{2},\qquad \angle DAE = \frac{\pi}{5},\qquad \angle ADE = \frac{3\pi}{10}.$$

This confirms that

$$\triangle ADC \sim \triangle EDC \sim \triangle ADE.$$

These similar triangles are a geometric way to see why the angles $\pi/5$ and $3\pi/10$ keep trading sine and cosine roles.

### 2.3. The double-angle bridge

From Part 1, we already found

$$\cos\left(\frac{2\pi}{5}\right) = \frac{\sqrt{5}-1}{4}.$$

Now use the double-angle identity

$$\cos(2\theta) = 2\cos^2(\theta)-1.$$

A unit-circle way to see this is to look at the two unit vectors at angles $+\theta$ and $-\theta$:

$$(\cos\theta,\sin\theta)\qquad \mathrm{and}\qquad (\cos\theta,-\sin\theta).$$

The angle between these two vectors is $2\theta$, so their dot product is

$$\cos(2\theta).$$

But from coordinates, the same dot product is

$$(\cos\theta,\sin\theta)\cdot(\cos\theta,-\sin\theta) = \cos^2\theta-\sin^2\theta.$$

Therefore

$$\cos(2\theta) = \cos^2\theta-\sin^2\theta.$$

Using

$$\sin^2\theta = 1-\cos^2\theta,$$

we get

$$\cos(2\theta) = \cos^2\theta-(1-\cos^2\theta) = 2\cos^2\theta-1.$$

Now set

$$\theta = \frac{\pi}{5}.$$

Then

$$2\theta = \frac{2\pi}{5},$$

so

$$\cos\left(\frac{2\pi}{5}\right) = 2\cos^2\left(\frac{\pi}{5}\right)-1.$$

Using the value from Part 1,

$$\frac{\sqrt{5}-1}{4} = 2\cos^2\left(\frac{\pi}{5}\right)-1.$$

So

$$2\cos^2\left(\frac{\pi}{5}\right) = 1+\frac{\sqrt{5}-1}{4} = \frac{3+\sqrt{5}}{4}.$$

Therefore

$$\cos^2\left(\frac{\pi}{5}\right) = \frac{3+\sqrt{5}}{8}.$$

Now notice that

$$\left(\frac{1+\sqrt{5}}{4}\right)^2 = \frac{1+2\sqrt{5}+5}{16} = \frac{6+2\sqrt{5}}{16} = \frac{3+\sqrt{5}}{8}.$$

Since $\pi/5$ is in the first quadrant, the cosine is positive. Thus

$$\cos\left(\frac{\pi}{5}\right) = \frac{1+\sqrt{5}}{4}.$$

Finally,

$$\frac{3\pi}{10} = \frac{\pi}{2}-\frac{\pi}{5},$$

so by the cofunction identity,

$$\sin\left(\frac{3\pi}{10}\right) = \cos\left(\frac{\pi}{5}\right).$$

Therefore

$$\sin\left(\frac{3\pi}{10}\right) = \frac{1+\sqrt{5}}{4}.$$

At this point, the golden ratio may be introduced as a useful simplification rather than an assumption. Since

$$\phi = \frac{1+\sqrt{5}}{2},$$

we have

$$\sin\left(\frac{3\pi}{10}\right) = \frac{\phi}{2}.$$

## Part 3: Skipping a vertex and the D chord

Just some starting material for now.

```text
side chord L: 
  central angle = 2π/5 
  half-angle = π/5 
  L/2 = R sin(π/5) 
  L = 2R sin(π/5) 
diagonal chord D: 
  central angle = 4π/5 
  half-angle = 2π/5 
  D/2 = R sin(2π/5) 
  D = 2R sin(2π/5) 
therefore: 
  D/L = sin(2π/5) / sin(π/5) 
      = 2 cos(π/5) 
      = φ
```

**Chord-length from a central angle.** (or whatever that angle is called)

- Take two radii from the center to the two endpoints of a chord.
  - Call the chord length $c$.
  - $\theta$ being the angle between the two radii. 
  - That gives an isosceles triangle. 
- Drop the perpendicular from the center to the chord. 
  - In an isosceles triangle, that perpendicular bisects the chord and the central angle. 
  - Then you have a right triangle with: 
    - hypotenuse $R$, 
    - angle $\theta / 2$, and 
    - opposite side $c/2$

SOH CAH TOA, and we have H and O, so SOH means sine.

`>> picture of right triangle in the context of the <<`<br/>
`>> pentagon and the circumscribing circle here     <<`

`>> picture of _just_ the right triangle here       <<`

$$sin\left(\theta / 2 \right) = \frac{c / 2}{R}$$

leads to

$$c = 2 R \sin \left(\theta / 2\right)$$

Side chord uses $\theta = 2 \pi / 5$; diagonal chord uses $\theta = 4 \pi / 5$.

$$D = 2 R \sin \left(\left(\frac{1}{2}\right)\left(\frac{4\pi}{5}\right)\right) = 2 R \sin \left(\frac{2\pi}{5}\right)$$

So I did the law of sines with two crazy angles. I could have used chord length to do the sine of just one angle. I'm not bitter, it's just that now, I know. It was fun to do the roots of unity. Actually, now that I'm looking at it, I would have had to get $R$ anyway, and the $D$ calculation is going to use $\sin\left(\frac{2\pi}{5}\right)$, which is the first one I found. I don't even know that I need to get the sine of $\pi / 5$, but I think I will anyway, or at least I'll follow kamMA while he does. And we'll find whatever mistake I made above ; )

***I'll have to have kamMA take care of the details for the 10 roots of unity, since we're getting the sine of $2 \pi / 10$. Or we can find another way.***


## Code footnotes

### CF.1. Code for roots-of-unity figure

```python
#!/usr/bin/env python3
#############################################################################
'''
@file    make_roots_of_unity_figure()
       OR, more likely, in the repo as a part of
         scripts/make_pentagon_figures.py
@author  Dave Black     GitHub @bballdave025     Signs comments as "DWB"
@since   2026-06-24

Anyone looking at this `pentagon_trig.md` file to see the code will most 
likely have gotten it from the main repo as
    `docs/math/pentagon_trig.md`
in which case, they'll also have a better version of this code, with CF.1 
and CF.2 combined, from
    `scripts/make_pentagon_figures.py`
This version can stand on its own, without the repo. It can also be used
in the repo.
'''
#############################################################################

import pathlib

import matplotlib.pyplot as plt

from matplotlib.axes import Axes
from matplotlib.figure import Figure

import numpy as np


def make_roots_of_unity_figure() -> tuple[Figure, Axes]:
  k = np.array([1, 2, 3, 4, 5])  # all five roots
  angles = 2 * np.pi * k / 5
  x = np.cos(angles)  # real part
  y = np.sin(angles)  # imaginary part

  fig, ax = plt.subplots(figsize=(6, 6)) 

  # Plot the circumradii (lines from the origin to each root/vertex)
  this_idx = 0
  for xi, yi in zip(x, y):
    this_is_2pi_ov_5 = this_idx == 0
    this_linewidth = 3  if this_is_2pi_ov_5  else  2
    ax.plot(
        [0, xi], [0, yi], 
        color='royalblue', 
        linewidth=this_linewidth, 
        zorder=2
    )
    this_idx += 1
  ##endof:  for xi, yi in zip(x, y)

  # Points at roots (pentagon vertices)
  ax.scatter(
      x, y, 
      color='crimson', 
      zorder=5, 
      s=90
  ) 

  # Point at origin
  ax.scatter(
      0, 0, 
      color='black', 
      zorder=5, 
      s=40
  ) 

  labels = [r'$z$', r'$z^2$', r'$z^3$', r'$z^4$', r'$z^5 = 1$'] 
  offsets = [ 
      ( 0.06,  0.04),  # z 
      (-0.15,  0.04),  # z^2 
      (-0.15, -0.09),  # z^3 
      ( 0.06, -0.09),  # z^4 
      ( 0.06,  0.04),  # z^5 = 1 
  ] 

  for  idx, (xi, yi, label) in enumerate(zip(x, y, labels)): 
    ax.text(
        xi + offsets[idx][0], yi + offsets[idx][1], 
        label, 
        fontsize=13, 
        fontweight='bold'
    ) 
  ##endof:  for

  ax.text(
      -0.12, -0.12, 
      r'$0$', 
      fontsize=12, 
      color='black'
  ) 

  ax.axhline(0, color='black', linewidth=0.8, alpha=0.3) 
  ax.axvline(0, color='black', linewidth=0.8, alpha=0.3)
  ax.set_aspect('equal') 
  ax.set_xlim(-1.4, 1.4) 
  ax.set_ylim(-1.4, 1.4) 
  ax.set_xlabel(r'Real Axis (Re)',      fontsize=11) 
  ax.set_ylabel(r'Imaginary Axis (Im)', fontsize=11) 
  ax.set_title(
      r'Circumradii of the Fifth Roots of Unity', 
      fontsize=13, 
      pad=15
  ) 
  ax.grid(True, linestyle=':', alpha=0.3)
  
  return fig, ax
##endof:   make_roots_of_unity_figure()


if __name__ == "__main__":
  '''
  Called when module is called from the command line.
  '''
  
  filename_rou_only = "pentagon_angles_roots_of_unity.png"
  
  ####begin:  Hardcoding, involving the boolean below this begin comment 
    ##          (for anyone wanting to make the figures in CWD, no repo)
  do_in_repo_save = True
  
  if "__file__" not in globals():
    do_in_repo_save = False
  ##endof:  if
  
  output_path_roots_of_unity = pathlib.Path.cwd() / filename_rou_only
    ##
  ####endof:  Hardcoding
  
  if do_in_repo_save:
    #  This assignment assumes that the script is run from
    #+ `scripts/make_pentagon_figures.py`
    repo_root = pathlib.Path(__file__).resolve().parents[1]
  
    output_path_roots_of_unity = repo_root / "figures" / filename_rou_only
  ##endof:  if/else not_do_in_repo_save
  
  output_path_roots_of_unity.parent.mkdir(
        parents=True,
        exist_ok=True,
  )
  
  fig_rou, ax_rou = make_roots_of_unity_figure()

  fig_rou.savefig(
      output_path_roots_of_unity,
      dpi=200,
      bbox_inches="tight",
  )

  plt.show()
##endof:  if
```

### CF.2. Code for similar-triangles figure

This figure shows one central triangle from the regular pentagon. The top subplot highlights the central triangle formed by two radii and one pentagon side. The bottom subplot shows the same triangle with the angle bisector $AD$ and the dropped normal $DE$.

```python
#!/usr/bin/env python3
#############################################################################
'''
@file    make_pentagon_triangle_figure.py
       OR, more likely, in the repo as a part of
         scripts/make_pentagon_figures.py
@author  Dave Black     GitHub @bballdave025     Signs comments as "DWB"
@since   2026-06-24

Anyone looking at this `pentagon_trig.md` file to see the code will most 
likely have gotten it from the main repo as
    `docs/math/pentagon_trig.md`
in which case, they'll also have a better version of this code, with CF.1 
and CF.2 combined, from
    `scripts/make_pentagon_figures.py`
This version can stand on its own, without the repo. It can also be used
in the repo.

Note that the `Point2D` type alias does not enforce “exactly shape (2,)” 
at runtime or even very strongly in static typing. It mostly says, 
“this is a NumPy array of floats.” Make sure to make its shape `(2,)`.
In other words, the expected shape of `Point2D` is `(2,)`, and there will
almost certainly be problems if this isn't the case. `Point2D` is a type
alias for (2D) Numpy points, where the 2D being in parentheses indicates
that the type hint does not specify the 2D nature of what's expected. 
'''
#############################################################################

import matplotlib.pyplot as plt

from matplotlib.patches import Arc
from matplotlib.patches import Polygon
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from numpy.typing import NDArray
import numpy as np

Point2D = NDArray[np.float64]
'''
A NumPy array representing one 2D point or vector.

Expected shape:
  (2,)
'''


def project_point_to_line(
      point: Point2D, 
      line_start: Point2D, 
      line_end: Point2D,
    ) -> Point2D:
  '''
  Project `point` onto the line through `line_start` and `line_end`.
  '''

  line_vector = line_end - line_start
  point_vector = point - line_start

  scale = np.dot(point_vector, line_vector) / np.dot(
      line_vector,
      line_vector,
  )

  projection = line_start + scale * line_vector

  return projection
##endof:  function project_point_to_line


def draw_angle_arc(
      ax: Axes,
      center: Point2D,
      radius: float,
      theta1_deg: float,
      theta2_deg: float,
      label: str,
      label_radius: float | None=None,
      label_angle_deg: float | None=None,
      fontsize: int=11,
    ) -> None:
  '''
  Draw a circular angle arc with a nearby label.
  '''

  if label_radius is None:
    label_radius = 1.25 * radius
  ##endof:  if

  if label_angle_deg is None:
    label_angle_deg = 0.5 * (theta1_deg + theta2_deg)
  ##endof:  if

  arc = Arc(
      center,
      width=2.0 * radius,
      height=2.0 * radius,
      angle=0.0,
      theta1=theta1_deg,
      theta2=theta2_deg,
      linewidth=1.5,
  )

  ax.add_patch(arc)

  label_angle_rad = np.deg2rad(label_angle_deg)
  label_xy = center + label_radius * np.array(
      [
        np.cos(label_angle_rad),
        np.sin(label_angle_rad),
      ]
  )

  ax.text(
      label_xy[0],
      label_xy[1],
      label,
      fontsize=fontsize,
      ha="center",
      va="center",
  )
##endof:  function draw_angle_arc


def draw_right_angle_marker(
      ax: Axes, 
      corner: Point2D, 
      direction_1: Point2D, 
      direction_2: Point2D, 
      size: float=0.06
    ) -> None:
  '''
  Draw a small right-angle marker at `corner`.

  The two direction vectors should point along the perpendicular rays.
  '''

  u = direction_1 / np.linalg.norm(direction_1)
  v = direction_2 / np.linalg.norm(direction_2)

  p0 = corner
  p1 = corner + size * u
  p2 = corner + size * u + size * v
  p3 = corner + size * v

  ax.plot(
      [p0[0], p1[0], p2[0], p3[0]],
      [p0[1], p1[1], p2[1], p3[1]],
      linewidth=1.2,
  )
##endof:  function draw_right_angle_marker


def make_pentagon_triangle_figure() -> tuple[Figure, tuple[Axes, Axes]]:
  '''
  Make a two-panel figure for the pentagon radius/side derivation.

  Top panel:
    regular pentagon with the central triangle highlighted.

  Bottom panel:
    zoomed triangle ABC with angle bisector AD and dropped normal DE.
  '''

  radius = 1.0

  vertex_angles_deg = np.array([36, 108, 180, 252, 324])
  vertex_angles_rad = np.deg2rad(vertex_angles_deg)

  vertices = np.column_stack(
      [
        radius * np.cos(vertex_angles_rad),
        radius * np.sin(vertex_angles_rad),
      ]
  )

  a_point = np.array([0.0, 0.0])
  b_point = vertices[0]
  c_point = vertices[4]
  d_point = 0.5 * (b_point + c_point)
  e_point = project_point_to_line(d_point, a_point, c_point)

  fig, axes = plt.subplots(
      nrows=2,
      ncols=1,
      figsize=(7, 10),
  )

  top_ax = axes[0]
  bottom_ax = axes[1]

  pentagon_patch = Polygon(
      vertices,
      closed=True,
      fill=False,
      linewidth=2.0,
  )

  top_ax.add_patch(pentagon_patch)

  top_ax.plot(
      [a_point[0], b_point[0]],
      [a_point[1], b_point[1]],
      linewidth=2.5,
  )

  top_ax.plot(
      [a_point[0], c_point[0]],
      [a_point[1], c_point[1]],
      linewidth=2.5,
  )

  top_ax.plot(
      [b_point[0], c_point[0]],
      [b_point[1], c_point[1]],
      linewidth=3.5,
  )

  top_ax.scatter(
      vertices[:, 0],
      vertices[:, 1],
      s=70,
      zorder=5,
  )

  top_ax.scatter(
      [a_point[0]],
      [a_point[1]],
      s=55,
      zorder=6,
  )

  top_ax.text(
      a_point[0] - 0.08,
      a_point[1] - 0.10,
      r"$A$",
      fontsize=13,
      fontweight="bold",
  )

  top_ax.text(
      b_point[0] + 0.04,
      b_point[1] + 0.04,
      r"$B$",
      fontsize=13,
      fontweight="bold",
  )

  top_ax.text(
      c_point[0] + 0.04,
      c_point[1] - 0.08,
      r"$C$",
      fontsize=13,
      fontweight="bold",
  )

  top_ax.text(
      0.63,
      0.00,
      r"$L$",
      fontsize=13,
      fontweight="bold",
  )

  top_ax.text(
      0.33,
      0.36,
      r"$R$",
      fontsize=13,
      fontweight="bold",
  )

  draw_angle_arc(
      top_ax,
      a_point,
      0.23,
      -36,
      36,
      r"$2\pi/5$",
      label_radius=0.34,
      fontsize=12,
  )

  top_ax.set_title(
      "Central triangle in a regular pentagon",
      fontsize=13,
  )

  top_ax.set_aspect("equal")
  top_ax.set_xlim(-1.25, 1.25)
  top_ax.set_ylim(-1.25, 1.25)
  top_ax.grid(True, linestyle=":", alpha=0.35)

  triangle_x = [a_point[0], b_point[0], c_point[0], a_point[0]]
  triangle_y = [a_point[1], b_point[1], c_point[1], a_point[1]]

  bottom_ax.plot(
      triangle_x,
      triangle_y,
      linewidth=2.5,
  )

  bottom_ax.plot(
      [a_point[0], d_point[0]],
      [a_point[1], d_point[1]],
      linestyle="--",
      linewidth=2.0,
  )

  bottom_ax.plot(
      [d_point[0], e_point[0]],
      [d_point[1], e_point[1]],
      linestyle=":",
      linewidth=2.5,
  )

  point_names = [
      ("A", a_point, (-0.08, -0.08)),
      ("B", b_point, (0.04, 0.04)),
      ("C", c_point, (0.04, -0.08)),
      ("D", d_point, (0.04, 0.02)),
      ("E", e_point, (-0.02, -0.10)),
  ]

  for name, point, offset in point_names:
    bottom_ax.scatter(
        [point[0]],
        [point[1]],
        s=55,
        zorder=5,
    )

    bottom_ax.text(
        point[0] + offset[0],
        point[1] + offset[1],
        rf"${name}$",
        fontsize=13,
        fontweight="bold",
    )
  ##endof:  for

  draw_angle_arc(
      bottom_ax,
      a_point,
      0.20,
      -36,
      0,
      r"$\pi/5$",
      label_radius=0.30,
      label_angle_deg=-18,
      fontsize=12,
  )

  draw_angle_arc(
      bottom_ax,
      c_point,
      0.20,
      90,
      144,
      r"$3\pi/10$",
      label_radius=0.30,
      label_angle_deg=118,
      fontsize=12,
  )

  draw_right_angle_marker(
      bottom_ax,
      d_point,
      a_point - d_point,
      c_point - d_point,
      size=0.055,
  )

  draw_right_angle_marker(
      bottom_ax,
      e_point,
      d_point - e_point,
      c_point - e_point,
      size=0.045,
  )

  bottom_ax.text(
      0.48,
      0.05,
      r"$AD$ bisects $\angle A$",
      fontsize=11,
  )

  bottom_ax.text(
      0.66,
      -0.28,
      r"$DE \perp AC$",
      fontsize=11,
  )

  bottom_ax.text(
      0.77,
      -0.03,
      r"$DC=L/2$",
      fontsize=11,
  )

  bottom_ax.set_title(
      "Bisected central triangle and dropped normal",
      fontsize=13,
  )

  bottom_ax.set_aspect("equal")
  bottom_ax.set_xlim(-0.15, 1.15)
  bottom_ax.set_ylim(-0.75, 0.75)
  bottom_ax.grid(True, linestyle=":", alpha=0.35)

  fig.tight_layout()

  return fig, (top_ax, bottom_ax)
##endof:  function make_pentagon_triangle_figure


if __name__ == "__main__":
  '''
  Called when module is called from the command line.
  '''
  
  filename_tf_only = "pentagon_triangle_derivation.png"
  
  ####begin:  Hardcoding, involving the boolean below this begin comment 
    ##          (for anyone wanting to make the figures in CWD, no repo)
  do_in_repo_save = True
  
  if "__file__" not in globals():
    do_in_repo_save = False
  ##endof:  if
  
  output_path_triangle_figure = pathlib.Path.cwd() / filename_tf_only
    ##
  ####endof:  Hardcoding
  
  if do_in_repo_save:
    #  This assignment assumes that the script is run from
    #+ `scripts/make_pentagon_figures.py`
    repo_root = pathlib.Path(__file__).resolve().parents[1]
  
    output_path_triangle_figure = repo_root / "figures" / filename_tf_only
  ##endof:  if do_in_repo_save
  
  output_path_triangle_figure.parent.mkdir(
        parents=True,
        exist_ok=True,
  )
  
  fig_tf, (top_ax_tf, bottom_ax_tf) = make_pentagon_triangle_figure()

  fig_tf.savefig(
      output_path_triangle_figure,
      dpi=200,
      bbox_inches="tight",
  )

  plt.show()
##endof:  if
```
