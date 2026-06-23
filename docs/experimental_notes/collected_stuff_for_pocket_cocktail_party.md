


## The basics

pocket-cocktail-party (repo name)


Cocktail Party Problem
    ↓
Blind Source Separation
    ↓
Methods:
  - ICA
  - FastICA
  - NMF
  - Beamforming
  - Deep Learning
  - etc.

Simplification we use.

Using Einstein Notation for tensors:

$$
X^m \left(t\right) = A^m_i S^i \left(t\right)
$$

Where

- $S^i \left(t\right)$ are the unknown sources
- $A^m_i$ is the unknown mixing matrix
- $X^m \left(t\right) are the microphone recordings.

Assumptions:

- $p_S(s^i) &= \prod_i p_i(s^i)$; sources are statistically independent<sup>[1]</sup>.
- $X^m(t)=A^m_iS^i(t)+\varepsilon^m(t), \qquad \|\varepsilon\|\ll\|\mathbf{A}\mathbf{S}\|; mixing is approximately linear<sup>[2]</sup>.
- $X^m(t)=A^m_iS^i(t), \qquad m=1,\ldots,M, \qquad i=1,\ldots,N, \qquad M\ge N.$; Number of microphones ≥ number of sources<sup>[3]</sup>.

## Real Acoustics (living room or car)

$$
X^m\left(t\right) = \int H^m_i\left(\tau\right) S^i \left(t - \tau\right)
$$

This is called a convolutional integral. Note that a sum over $i$ is
enforced by the repetition of the index, i. The convolutional integral
"picks out" something, but I'm going to have to ask kamMA to remember
what it picks out.


## Section

What we are _not_ doing is imagining we have a standard sterio track.

```text
stereo track
=
vocals
+ drums
+ bass
+ guitar
+ violin
+ crowd noise
```

ICA is dead in the water. Modern systems do something different. A simplified version is

```text
Waveform
↓
Spectrogram
↓
CNN / U-Net / Transformer
↓
Estimated source masks
↓
Recovered stems
```

with the network having learned priors such as

```text
Kick drums look like this.
Snare drums look like this.
Vocals look like this.
Bass looks like this.
```

for huge datasets.

In other words, the model finds something like

$$
P\left(\mathrm{sources} | \mathrm{audio})

## Why this is more interesting to me

The progression I'm investigating is:

### Synthetic ICA
-5 sources
-5 microphones (later adding a 6th)
- Linear mixing
- ICA works

### Car Experiment
- 2-4 speakers
- 3-4 microphones
- Echoes
- Road noise
- Real acoustics
- ICA partly works

### While I won't do: Music Separation
- 5 instruments
- 2 channels
- ICA fundamentally insufficient
- Need learned priors

That's a much richer story than:

"I ran FastICA."

It becomes:

"Here is where classical methods work.
Here is where their assumptions fail.
Here is why modern deep methods became necessary."

And that, in my opinion, is exactly the sort of thing that distinguishes a portfolio project from a homework assignment.

I could also put it forward as saying that the question at hand isn't:

> Can I run ICA?

The interesting questions are:

> When and why does ICA stop working? 
> 
> what assumptions did the deep-learning people buy 
> with all those extra joules of computation and all 
> those learned priors?

## Fun and silly phrases for WER calculations

We have I, Daddy, who am doing the research. We have Mommy, the patient one, not a native Engish speaker, but a native-level English speaker. 
We have daughter, who is learning how to read and who introduces reasons to question all assumptions with her alternating high-energy interest and boredom.

For the first 16, I've biased a little toward distinct sounds, unusual words, and recoverability without making it a speech-recognition benchmark.

**First 16 (lightly optimized)**
1. The purple walrus borrowed my bicycle on Tuesday.
2. **Seven sleepy penguins played chess in the bathtub.**
3. A tiny dragon hid inside the cookie jar.
4. The moon taught my goldfish how to whistle.
5. Three squirrels delivered pancakes to the library.
6. **My backpack thinks it is a submarine captain.**
7. The orange octopus lost its homework again.
8. Five pirate ducks sailed across the playground.
9. The cactus orchestra performed a noodle symphony.
10. A banana astronaut visited Jupiter for lunch.
11. **The invisible hamster stole my left sock.**
12. Twelve llamas practiced karate behind the bakery.
13. The jellybean wizard forgot his rubber boots.
14. A cheerful robot planted carrots on Mars.
15. **The pancake volcano erupted with blueberry syrup.**
16. My pet rhinoceros prefers strawberry toothpaste.

**Second 16 (pure funny)**
17. A chicken interviewed a cloud for a newspaper.
18. The grumpy pickle demanded a tiny hat.
19. Two goats opened a detective agency for squirrels.
20. The mayor of the crayons declared Tuesday illegal.
21. A nervous donut challenged a broom to a duel.
22. The spaghetti king lost his crown in a puddle.
23. A squirrel rode a skateboard through a wedding.
24. The queen of the potatoes adopted a dragon.
25. A confused moose ordered seventeen pizzas for breakfast.
26. The marshmallow pirate buried treasure in the dishwasher.
27. A kangaroo taught algebra to a flock of geese.
28. The raccoon orchestra forgot where it parked the tuba.
29. An owl accidentally mailed itself to Nebraska.
30. The dinosaur librarian charged late fees to the moon.
31. A walrus in pajamas won the jellybean Olympics.
32. The world's bravest carrot fought a vacuum cleaner.

**Decisions**

Little One (not so little anymore) chose **2**, but simplified it to

> Seven chicks played chest in the bathtub.

(the word, chest, being in her vocabulary, while the word, chess, is OOV.)

Daddy gets

> Three pirate ducks sailed across the playground.

Mommy gets

> The pancake volcano erupted with blueberry syrup.

**For voice synthesis, so Daughter can memorize**

"""
Julie's funny phrase is:

Seven chicks played chest in the bathtub.

Seven chicks played chest in the bathtub.

Seven chicks played chest in the bathtub.

Seven chicks played chest in the bathtub.

Seven chicks played chest in the bathtub.

Daddy's funny phrase is:

Three pirate ducks sailed across the playground.

Three pirate ducks sailed across the playground.

Three pirate ducks sailed across the playground.

Three pirate ducks sailed across the playground.

Three pirate ducks sailed across the playground.

Mommy's funny phrase is:

The pancake volcano erupted with blueberry syrup.

The pancake volcano erupted with blueberry syrup.

The pancake volcano erupted with blueberry syrup.

The pancake volcano erupted with blueberry syrup.

The pancake volcano erupted with blueberry syrup.
"""

## Thoughts

### The bigger threats [bigger than AC] are:

#### Automatic gain control (AGC)

Every phone decides:
- "This recording is too quiet."
- "Now it's too loud."
- "Now I'll compress it."

independently.

That breaks the simple mixing model.

#### Different clocks

Phone A thinks a second is:

> 1.000000 seconds

Phone B thinks:

> 0.999995 seconds

After a few minutes they drift.

Your director's clap solves alignment at the beginning.

You may want another clap at the end.

## Simple enough, yet real enough strategy

### Geometry

(This section will need formatting, look for consistency in Einstein notation)

Mix audio amplitudes, not perceived loudness.
Human hearing is roughly logarithmic, but the microphone receives pressure waves. In open air, pressure amplitude falls roughly like:

$$
A(r) \propto \frac{1}{r}
$$

Intensity falls like:

$$
I(r)\propto \frac{1}{r^2}
$$	​

So for your synthetic mixer, use amplitude attenuation:

$$
x^m(t) = A^m_i s^i(t)
$$

with something like:

$$
A_i^m = \frac{1}{\left(r^m_i + r_{(0)}\right)}
$$
	​

then normalize each “own mic” to 1.

For your square idea:

own mic:        1.00
adjacent mic:   0.20
diagonal mic:   0.20 / sqrt(2) ≈ 0.141

That is absolutely reasonable for Experiment 0.

For the five-source “Yellowcard-ish” version, use a regular pentagon, not a square/pyramid:

Sources:
- vocal
- violin
- guitar
- bass/piano
- drums

Mics:
- one near each source
- optional 6th mic in the center

In a regular pentagon:
-adjacent distance = $s$
-next-nearest distance = $\phi * s ≈ 1.618 s$
  - where $\phi = \frac{1+sqrt{5}}{2}$ is the golden ratio

So if adjacent bleed is 0.20, next-nearest bleed would be about:

0.20 / 1.618 ≈ 0.124

That gives a nice non-MOOC mixing matrix:

self:         1.000
adjacent:     0.200
next-nearest: 0.124

This is simple and defensible.

For instruments:

vocal: vowel-like tone or spoken phrase
violin: sawtooth-ish tone + vibrato
guitar: plucked harmonic tone
bass/piano: lower notes with sharp attack
drums: kick/snare/noise bursts

And yes, you can send notes or a small sketch of sheet music. Even easier: send something like:

vocal: E4 F#4 G4 A4
violin: B4 A4 G4 F#4
guitar: Em G D A
bass: E2 E2 G2 D2
drums: kick on 1 and 3, snare on 2 and 4

Then we can generate synthetic waveforms with NumPy arrays and overtone patterns.

The key project title idea:
- Bleed Matrix: Synthetic Source Separation with Geometric Microphone Mixing
- Pocket Cocktail Party: blah blah blah

That already sounds much less like a MOOC.

For pentagon, mic in the middle, then mic over the middle;
if the pentagon has circumradius $R$, and the overhead mic is height $h$, 
then every source is the same distance 
from it: $r_{\mathrm{overhead}} = sqrt{R^2 + h^2}$

So the overhead mic becomes a fair “whole-band room mic.”

That is satisfying and defensible:

- not just center mic
- not another close mic
- adds 3D geometry
- captures the ensemble

For synthetic mixing:

$$
A^m_i = \frac{1}{r^m_i + r_{(0)}}
$$

then normalize so each source’s own close mic has weight 1.

For the overhead mic, every source gets the same coefficient:

$$
A_i^{\left(\mathrm{overhead}\right)} = c
$$

overhead bleed from each source: c = 0.25–0.40

depending on how “room mic” you want it.

This gives the project a nice ladder:

- Experiment 0: 5 sources, 5 close mics, pentagon bleed
- Experiment 1: add 6th overhead mic
- Experiment 2: add delay/echo/noise
- Experiment 3: reduce to stereo and show why ICA struggles
  - possible small non-singular, dimension reduction, information loss aside

### Instruments

For source synthesis, your overtone-array idea is perfect:

instrument = {
    "fundamental": f0,
    "partials": [1.0, 0.45, 0.25, 0.12, 0.06],
}

Then each source is:

$$
s^{(i)}(t) = \sum\limits_{k} c^{(i)}_k \sin{\left(2 \pi k f^{(i)}t\right)}
$$

Start deliberately simple:

voice:  [1.00, 0.55, 0.25, 0.10, 0.05]
violin: [1.00, 0.75, 0.55, 0.35, 0.20]
guitar: [1.00, 0.50, 0.30, 0.18, 0.08]
piano:  [1.00, 0.35, 0.18, 0.10, 0.05]
drums:  noise burst / thump, not harmonic first

Send the Fourier-analysis picture if you want. That is exactly the kind of “Dave-owned” source model that makes the project yours.




# Notes

[1]: Technically, statistical independence of the sources is expressed by

$$
p_S(s^i)=\prod_i p_i(s^i),
$$

meaning the joint source distribution factors into the marginal distributions 
of the individual sources. 

Where 
- $p_N is the probability density of N, 
- $s^i$ denotes the whole source-coordinate vector, not a summed index expression,
- $X^m(t)$ is the signal recorded by microphone $m=1,\ldots,M$,
  $S^i(t)$ is source signal $i=1,\ldots,N$, and
  $A^m_i$ is the mixing coefficient from source $i$ into microphone $m$.


This is stronger than merely having diagonal covariance, i.e. a diagonally 
covariant matrix $\mathbf{C}$ satisfies

$$
C^{ij}
=
\operatorname{Cov}(S^i,S^j)
=
\sigma_i^2\delta^{ij},
$$

which only says the sources are uncorrelated. Thus,

$$
C^{ij}\propto\delta^{ij}
\quad\not\Rightarrow\quad
p_S(s^i)=\prod_i p_i(s^i).
$$

ICA needs statistical independence, not just zero cross-covariance.

[2] Mixing is approximately linear when the recordings can be modeled as

$$
X^m(t)=A^m_iS^i(t)+\varepsilon^m(t),
\qquad
\|\varepsilon\|\ll\|\mathbf{A}\mathbf{S}\|.
$$

Here $\varepsilon^m(t)$ collects nonlinearities, echoes, saturation, sensor noise, 
and other modeling errors. $\mathbf{X}$ represents the microphones.

[3] Here $m=1,\ldots,M$ indexes microphones and $i=1,\ldots,N$ indexes sources, so
$\mathbf{X}(t)\in\mathbb{R}^M$, $\mathbf{S}(t)\in\mathbb{R}^N$, and
$\mathbf{A}\in\mathbb{R}^{M\times N}$. The usual determined/overdetermined case assumes
$M\ge N$, meaning there are at least as many microphones as sources.


---

---

Letter for Yellowcard contact form:

https://www.yellowcardband.com/contact?utm_source=chatgpt.com

"""
Hello Yellowcard Team,

My name is David Black. I am a machine-learning practitioner and researcher working on a personal educational portfolio project involving blind source separation (the classic "cocktail party problem"), signal processing, and synthetic audio generation.

The project is entirely non-commercial and intended as a learning and portfolio exercise.

One portion of the project is inspired by Yellowcard's instrumentation—specifically the combination of voice, violin, guitar, bass, and drums that makes the band so distinctive. My current plan is to build a fully synthetic source-separation experiment using those instrument categories and, if appropriate, a few measures inspired by the harmonic structure of "Gifts and Curses" as a test case.

Before doing so, I wanted to ask for explicit permission to:

1. Mention Yellowcard by name in the project documentation.
2. State that the experiment was inspired by Yellowcard's instrumentation and arrangements.
3. Use a small, clearly attributed educational example inspired by "Gifts and Curses."

I would be happy to provide attribution, include links to the band's official website, or make any changes you would prefer.

I've been a fan for many years and have attended many shows over the years. Thank you for the music and for the inspiration behind the project.

Sincerely,

David Black
GitHub: @bballdave025

"""

---

Left:
  Concert / YC side
    - violin silhouette
    - guitar silhouette
    - GAC inspiration (subtle)

Center:
  Dave
    - notebook
    - equations
    - pentagon geometry

Right:
  ICA side
    - microphone pentagon
    - separated waveforms
    - spectrograms
    - recovered sources

Bottom:
  "Pocket Cocktail Party"
  Blind Source Separation through
  Geometry, Harmonics, and Signal Mixing

