# Mathematical Details for the Pentagon

\[@TODO: Put some kind of fun ascii art in here involving a regular pentagon and some instruments.\]

# Part 1

### Extended footnote: roots of unity and the regular pentagon

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

For the nontrivial fifth roots, $z\ne1$, so

$$z^4+z^3+z^2+z+1=0.$$

Also $z\ne0$, so we may divide by $z^2$:

$$z^2+z+1+\frac{1}{z}+\frac{1}{z^2}=0.$$

Now group the $z^2$-terms (numerator or denominator,) the $z$-terms (numerator or denominator,) and the constant term:

$$\left(z^2 + \frac{1}{z^2}\right)+\left(z+\frac{1}{z}\right)+1 = 0$$

Now, we use the standard trick (i.e. we remember that we did this once in some class, so we try)

$$x = z+\frac{1}{z}.$$

Then

$$x^2=\left(z+\frac{1}{z}\right)^2=z^2+2+\frac{1}{z^2},$$

so

$$z^2+\frac{1}{z^2}=x^2-2.$$

Substitute this into the grouped equation:

$$(x^2-2)+x+1=0.$$

Therefore

$$x^2+x-1=0.$$

Solving,

$$x=\frac{-1\pm\sqrt{5}}{2}.$$

Now connect this back to the unit circle. Since

$$z=e^{2\pi i/5},$$

we have

$$\frac{1}{z}=e^{-2\pi i/5}.$$

Therefore

$$z+\frac{1}{z}=e^{2\pi i/5}+e^{-2\pi i/5}=2\cos\left(\frac{2\pi}{5}\right).$$

by

$$\cos \theta = \frac{e^{i \theta} + e^{-i \theta}}{2}$$

So

$$x=2\cos\left(\frac{2\pi}{5}\right).$$

The angle, $2\pi / 5$, lies in the first quadrant, so its cosine (real part) is positive. (Remember Euler's Formula — one of many — this Euler's Formula being $e^{i \theta} = \cos \theta + i \sin \theta$ to see why its real part is positive. Or imagine the five spokes coming out to the unit circle, which I might plot and include from the code in Code Footnote, _§ CF.1_.)

$$x=\frac{-1+\sqrt{5}}{2}.$$

Thus

$$2\cos\left(\frac{2\pi}{5}\right)=\frac{-1+\sqrt{5}}{2},$$

and therefore

$$\cos\left(\frac{2\pi}{5}\right)=\frac{\sqrt{5}-1}{4}.$$

Now compute the corresponding sine value:

$$\sin^2\left(\frac{2\pi}{5}\right)=1-\cos^2\left(\frac{2\pi}{5}\right)=1-\left(\frac{\sqrt5-1}{4}\right)^2$$

Since

$$(\sqrt{5}-1)^2=5-2\sqrt{5}+1=6-2\sqrt{5},$$

we get

$$\sin^2\left(\frac{2\pi}{5}\right)=1-\frac{6-2\sqrt5}{16}=\frac{16-(6-2\sqrt5)}{16}=\frac{10+2\sqrt5}{16}.$$

So

$$\sin\left(\frac{2\pi}{5}\right)=\frac{\sqrt{10+2\sqrt5}}{4}.$$

In the regular pentagon, the triangle formed by two circumradii $R$ and one side length $L$ has angles

$$\frac{3\pi}{10},\quad \frac{3\pi}{10},\quad \frac{2\pi}{5}.$$

By the law of sines,

$$  \frac{R}{\sin(3\pi/10)}=\frac{L}{\sin(2\pi/5)}.$$

Thus

$$\frac{R}{L}=\frac{\sin(3\pi/10)}{\sin(2\pi/5)}.$$

Since, as we will more rigorously show in _§ Part 2_,

$$\sin\left(\frac{3\pi}{10}\right)=\cos\left(\frac{\pi}{5}\right)=\frac{1+\sqrt5}{4},$$

we get

$$\frac{R}{L}=\frac{\frac{1+\sqrt5}{4}}{\frac{\sqrt{10+2\sqrt5}}{4}}=\frac{1+\sqrt5}{\sqrt{10+2\sqrt5}}.$$

Equivalently (and take notice that not only are the numerator and denominator positive &mdash; all that we need to use this square the expression and then take its positive square root &mdash; but all parts of numerator and denominator are positive,)

$$\left(\frac{R}{L}\right)^2=\frac{(1+\sqrt5)^2}{10+2\sqrt5}=\frac{6+2\sqrt5}{10+2\sqrt5}.$$

Rationalizing,

$$\frac{6+2\sqrt5}{10+2\sqrt5}\cdot\frac{10-2\sqrt5}{10-2\sqrt5}=\frac{40+8\sqrt5}{80}=\frac{5+\sqrt5}{10}.$$

Therefore, since, as we said, the original numerator and denominator were positive, we can simply take the positive square root,

$$\frac{R}{L}=\sqrt{\frac{5+\sqrt5}{10}}=\frac{1}{10}\sqrt{50+10\sqrt5}.$$

So the circumradius of a regular pentagon with side length (L) is

$$R=\frac{L}{10}\sqrt{50+10\sqrt5}.$$

---

The repo author, having taught college algebra and remedial math along with physics, physical science, and calculus, prefers to stay away from the "square it, then take its square root at the end" stuff, for the sake of his students, will also get to the final result thusly.

Go back to the expression:

$$
\frac{R}{L} = \frac{1+\sqrt5}{\sqrt{10+2\sqrt5}}.
$$

Rationalize the denominator:

$$
\frac{1+\sqrt5}{\sqrt{10+2\sqrt5}}
\cdot
\frac{\sqrt{10+2\sqrt5}}{\sqrt{10+2\sqrt5}} = \frac{(1+\sqrt5)\sqrt{10+2\sqrt5}}{10+2\sqrt5}.
$$

Factor the denominator:

$$
10+2\sqrt5=2(5+\sqrt5).
$$

So:

$$
\frac{R}{L} = \frac{(1+\sqrt5)\sqrt{10+2\sqrt5}}{2(5+\sqrt5)}.
$$

Now simplify the coefficient:

$$
\frac{1+\sqrt5}{5+\sqrt5}.
$$

Rationalize that little piece:

$$
\frac{1+\sqrt5}{5+\sqrt5}
\cdot
\frac{5-\sqrt5}{5-\sqrt5} = \frac{(1+\sqrt5)(5-\sqrt5)}{25-5}.
$$

The numerator is:

$$
(1+\sqrt5)(5-\sqrt5) = 5-\sqrt5+5\sqrt5-5 = 4\sqrt5.
$$

So:

$$
\frac{1+\sqrt5}{5+\sqrt5} = \frac{4\sqrt5}{20} = \frac{\sqrt5}{5}.
$$

Therefore:

$$
\frac{R}{L} = \frac{1}{2}
\cdot
\frac{\sqrt5}{5}
\cdot
\sqrt{10+2\sqrt5}.
$$

So:

$$
\frac{R}{L} = \frac{\sqrt5}{10}\sqrt{10+2\sqrt5}.
$$

Combine the radicals:

$$
\frac{R}{L} = \frac{1}{10}\sqrt{5(10+2\sqrt5)}.
$$

Thus:

$$
\frac{R}{L} = \frac{1}{10}\sqrt{50+10\sqrt5}.
$$

---

Radical-expression costume change complete. No dirty <sub>(I already acknowledged that all necessary assumptions were checked for the squaring and then square root at the end, but it still feels dirty.)</sub> tricks. Just rationalization.


---

---

# Part 2 

## Extended footnote: Geometric Derivation of $\ \  \sin\left(\frac{3\pi}{10}\right)$

### 2.1. Defining the Triangle Properties

I will eventually get some nice Python code in _§ CF.2_ written (or, more likely, get an AI assistant to do so) which will show one interior triangle from the regular pentagon probably like the figure from _§ CF.1_ with a highlighted triangle in the top subplot, then the described bisecting of an interior angle and dropping a normal from the point at the bisection of the edge. For now, words and \*TeX will have to do.

Consider one of the interior triangles for the pentagon we discussed before, an isosceles triangle $\triangle ABC$ where:
* The apex vertex $A$ has an interior angle of $\frac{2\pi}{5}$ and the length of the side opposite is $L$.
* The clockwise base vertices $B$ and $C$ both have interior angles of $\frac{3\pi}{10}$ and the lengths of the sides opposite each of these are .
* The side length is $L$.

The sum of the angles is verified by:
$$\frac{2\pi}{5} + \frac{3\pi}{10} + \frac{3\pi}{10} = \frac{4\pi}{10} + \frac{3\pi}{10} + \frac{3\pi}{10} = \pi$$

We bisect the apex angle $A$ with the line segment $AD$, where $D$ lies on the base segment $BC$. Since $\triangle ABC$ is isosceles, $AD$ is perpendicular to $BC$ ($D$ is the midpoint of $BC$). Let the base length $BC = L$, making $DC = \frac{L}{2}$. 

The right triangle $\triangle ADC$ contains the following interior angles:
* $\angle DAC = \frac{\pi}{5}$ (the bisected apex)
* $\angle ADC = \frac{\pi}{2}$ (the right angle)
* $\angle ACD = \frac{3\pi}{10}$ (the base angle)

## 2. Setting Up the Dropped Normal
We then drop a normal from point $D$ to the line segment $AC$, meeting at point $E$. This creates two smaller internal right triangles, $\triangle EDC$ and $\triangle ADE$. 

Because the acute angles of a right triangle must sum to $\frac{\pi}{2}$ (meaning $\frac{\pi}{5}$ and $\frac{3\pi}{10}$ are complementary):
* In $\triangle EDC$: $\angle DEC = \frac{\pi}{2}$ and $\angle ECD = \frac{3\pi}{10}$, forcing $\angle EDC = \frac{\pi}{5}$.
* In $\triangle ADE$: $\angle AED = \frac{\pi}{2}$ and $\angle DAE = \frac{\pi}{5}$, forcing $\angle ADE = \frac{3\pi}{10}$.

This confirms that $\triangle ADC \sim \triangle EDC \sim \triangle ADE$.

Using basic right-triangle definitions across these similar structures:
1. From $\triangle ADC$: $AC = \frac{DC}{\cos(3\pi/10)} = \frac{L}{2\cos(3\pi/10)}$
2. From $\triangle EDC$: $EC = DC \cdot \cos\left(\frac{3\pi}{10}\right) = \frac{L}{2}\cos\left(\frac{3\pi}{10}\right)$
3. From $\triangle ADE$: $AE = AD \cdot \cos\left(\frac{\pi}{5}\right)$

Since $AC = AE + EC$, substituting the trigonometric definitions into this line segment sum results in a standard circular identity ($1 = \sin^2\theta + \cos^2\theta$). To solve uniquely for the exact value of the angle without an infinite loop, we must anchor these ratios to a concrete geometric constant.

## 3. Connecting to the Standard Golden Triangle
To fix the system, we introduce a **standard golden triangle configuration**. A standard golden triangle is an isosceles triangle with base angles of $\frac{2\pi}{5}$ and an apex angle of $\frac{\pi}{5}$. If we scale its base to $1$, its legs match the golden ratio $\phi$:
$$\phi = \frac{\sqrt{5}+1}{2}$$

If you drop an altitude from one of the base vertices of a standard golden triangle to its opposite leg, it isolates a right triangle with exactly the same interior angles as our $\triangle ADC$ ($\frac{\pi}{5}, \frac{\pi}{2}, \frac{3\pi}{10}$). 

In that standard configuration, the hypotenuse is the base of the golden triangle ($1$), and the leg adjacent to the angle $\frac{\pi}{5}$ is known by fundamental golden ratio proportions to be:
$$\cos\left(\frac{\pi}{5}\right) = \frac{\phi}{2} = \frac{\sqrt{5}+1}{4}$$

## 4. Final Calculation
Because $\frac{\pi}{5}$ and $\frac{3\pi}{10}$ are strictly complementary ($\frac{\pi}{5} + \frac{3\pi}{10} = \frac{\pi}{2}$), we apply the co-function identity $\sin(\theta) = \cos\left(\frac{\pi}{2} - \theta\right)$:

$$\sin\left(\frac{3\pi}{10}\right) = \cos\left(\frac{\pi}{5}\right)$$

Substituting our known value of $\cos\left(\frac{\pi}{5}\right)$ gives the exact value:
$$\sin\left(\frac{3\pi}{10}\right) = \frac{\sqrt{5}+1}{4}$$




## Code footnotes

### CF.1. Code for roots-of-unity figure

```python
import matplotlib.pyplot as plt 
import numpy as np 

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
    ( 0.06,  0.04)   # z^5 = 1 
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

plt.show()
```


### CF.2. Code for similar-triangles figure

kamMA, I hope the description above, which I will repeat here, is sufficient to describe what I'd like.

> I will eventually get some nice Python code in _§ FC.2_ written (or, more likely, get an AI assistant to do so) which will show one interior triangle from a regular pentagon probably created similarly to the spokes in the figure from _§ FC.1_ with a highlighted triangle in the top subplot. The bottom subplot will then the described bisecting of an interior angle and dropping a normal from the point at the bisection of the edge with all the A, B, C, D, and E stuff as well as some angle values.