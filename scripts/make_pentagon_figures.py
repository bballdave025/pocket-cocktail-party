#!/usr/bin/env python3
#############################################################################
'''
@file    scripts/make_pentagon_figures.py
@author  Dave Black     GitHub @bballdave025     Signs comments as "DWB"
@since   2026-06-24

Anyone looking at this `pentagon_trig.md` file to see the code will most 
likely have gotten it from the main repo as
    `docs/math/pentagon_trig.md`
in which case, they'll also have a better version of this code, with CF.1 
and CF.2 combined, from
    `scripts/make_pentagon_figures.py`
This version is the combined version, meant to be run in the repo.

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


def make_roots_of_unity_figure() -> tuple[Figure, Axes]:
  '''
  Create a figure showing the relationship between the pentagon and
  the fifth roots of unity, related to $z^5 = 1$
  
  This figureseful for showing the signs of the real parts of
  $z$, $z^2$, $z^3$, $z^4$, $z^5$, and likely for other things.

  It is mainly used to illustrate a document showing the math used
  in the project, which (starting in the repo root) is at
  `docs/math/pentagon_trig.md`  
  '''
  
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
##endof:  method (function) make_roots_of_unity_figure


def make_pentagon_triangle_figure() -> tuple[Figure, tuple[Axes, Axes]]:
  '''
  Make a two-panel figure for the pentagon radius/side derivation.
  
  It is mainly used to illustrate a document showing the math used
  in the project, which (starting in the repo root) is at
  `docs/math/pentagon_trig.md`

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
##endof:  method (function) make_pentagon_triangle_figure



