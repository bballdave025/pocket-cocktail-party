# Synthetic Experiment 0.0 — Harmonic Five-Source ICA

## Goal

Create a synthetic source-separation experiment that is simple enough to implement quickly, but physically motivated enough that it is not just a classroom ICA demo.

We model five musical sources arranged on a regular pentagon:

1. voice
2. violin
3. acoustic guitar
4. bass part played by piano
5. snare-like drum

Each source has a nearby microphone. Later experiments add either a center microphone or an overhead microphone.

## Musical Setup

For the first test, each source plays one note for one second, then rests for one second.

The first chord should be harmonically pleasant but not totally trivial.

First thought on a chord: **C major add 9**

| Source     |                    Note |         Frequency |
| ---------- | ----------------------: | ----------------: |
| Piano bass |                      C2 |          65.41 Hz |
| Guitar     |                      G3 |         196.00 Hz |
| Voice      |                      E4 |         329.63 Hz |
| Violin     |                      D5 |         587.33 Hz |
| Snare      | C4-centered noise burst | ~261.63 Hz center |

This is deliberately not all unison. The sources have different fundamentals, which may make separation easier. However, because the notes belong to the same harmony, their overtones overlap in structured ways.

For example:

$$
3 \cdot C2 \approx G3
$$

and other partials will land near chord tones. This means the experiment is simple, but not completely artificial.

## Source Model

Each pitched instrument is modeled as a sum of harmonic partials:

$$
s_i(t)=e_i(t)\sum_{k=1}^{K} c^i_k \sin(2\pi k f_i t)
$$

where:

* $s_i(t)$ is source (i),
* $f_i$ is its fundamental frequency,
* $c^i_k$ is the relative strength of partial (k),
* $e_i(t)$ is a simple amplitude envelope.

Initial overtone arrays:

```python
voice  = [1.00, 0.55, 0.25, 0.10, 0.05]
violin = [1.00, 0.75, 0.55, 0.35, 0.20]
guitar = [1.00, 0.50, 0.30, 0.18, 0.08]
piano  = [1.00, 0.35, 0.18, 0.10, 0.05]
```

The snare is not modeled as a harmonic instrument at first. It can be a short noise burst with a simple decay envelope, optionally mixed with a weak C4-centered resonant tone.

## Geometry

The five sources sit at the vertices of a regular pentagon.

The five close microphones also sit near those vertices.

The mixing model is:

$$
x^m(t)=\sum_i A^m_i s_i(t)
$$

where:

* (x^m(t)) is microphone (m),
* (s_i(t)) is source (i),
* (A^m_i) is the attenuation from source (i) to microphone (m).

Use pressure-amplitude attenuation:

$$
A^m_i \propto \frac{1}{r^m_i+r_0}
$$

Then normalize so that each source has amplitude 1.0 in its own close microphone.

For a regular pentagon:

$$
\text{diagonal}=\varphi \cdot \text{side}
$$

where:

$$
\varphi=\frac{1+\sqrt{5}}{2}\approx 1.618
$$

A simple starting bleed matrix is therefore:

| Relationship     | Amplitude |
| ---------------- | --------: |
| own mic          |     1.000 |
| adjacent mic     |     0.200 |
| next-nearest mic |     0.124 |

because:

$$
0.124 \approx \frac{0.200}{1.618}
$$

## Extra Microphone Experiments

### Experiment 0.0.1 — Five Sources, Five Close Mics

Use only the five close microphones.

Hypothesis:

> ICA should perform well because the number of microphones equals the number of sources, the mixing is linear, and each source has a strong nearby microphone.

### Experiment 0.0.2 — Add Center Mic

Add a sixth microphone at the center of the pentagon.

It receives equal contribution from all five sources.

Hypothesis:

> The center mic may help by adding another mixture, but it may also be somewhat redundant because it gives a balanced blend of all sources.

### Experiment 0.0.3 — Add Overhead Mic

Instead of placing the sixth microphone at the center on the floor, place it above the center.

If the pentagon has circumradius (R), and the overhead mic has height (h), then each source is at distance:

$$
r_{\text{overhead}}=\sqrt{R^2+h^2}
$$

from the overhead microphone.

Hypothesis:

> The overhead mic is physically satisfying because it adds a third spatial dimension and behaves like a simplified “room mic.” It may improve separation while also producing a more realistic ensemble recording.

## ICA Question

With five true sources and six microphones, the system is overdetermined.

The sixth ICA component may not correspond to a new real instrument. It may instead capture:

* silence,
* numerical residual,
* shared harmonic structure,
* noise,
* or a small mixture of all sources.

This is part of the experiment.

The question is not only:

> Can ICA recover the instruments?

but also:

> What does ICA do when we give it more microphone channels than true musical sources?

## Why This Is Not Just a MOOC Demo

A simple ICA demo usually starts with arbitrary source signals and an arbitrary mixing matrix.

This experiment instead builds the mixing matrix from:

* source placement,
* microphone placement,
* geometric distances,
* amplitude attenuation,
* harmonic overtone structure,
* and musically meaningful notes.

The experiment is still small, but the assumptions are explicit and testable.

## Motivation

This experiment is partly inspired by the classic cocktail party problem in blind source separation and partly by a practical curiosity:

> If a live band consists of multiple instruments occupying different physical locations, how much information about the individual performers can be recovered from a collection of mixed microphone recordings?

To make the experiment concrete and enjoyable, the synthetic ensemble is loosely inspired by a Yellowcard-style arrangement:

* voice
* violin
* guitar
* bass (initially modeled by piano)
* drums

Go [Yellowcard](https://www.yellowcardband.com)!

The goal is not to reproduce any particular Yellowcard song, but to create a musically meaningful synthetic environment containing the same broad categories of sources. The presence of violin alongside voice, guitar, bass, and drums makes the resulting mixtures more interesting than many introductory source-separation examples.

### Hypothesis: Harmonic Structure

If all instruments play unrelated notes, source separation may become artificially easy.

Instead, the instruments will play harmonically related notes. This creates overlap among overtone series, producing a more realistic challenge.

For example, some partials from the bass note may lie near fundamentals or overtones of the guitar, voice, or violin.

This is one reason harmony sounds pleasant to humans.

It may also make source separation more difficult.

### Hypothesis: Extra Microphones

Two additional microphone configurations will be tested:

1. Center microphone
2. Overhead microphone

Both microphones are equidistant from all sources.

However, the overhead microphone introduces a third spatial dimension and more closely resembles a real-world room microphone.

Hypothesis:

> The overhead microphone will provide more useful information for source separation than the center microphone despite both being symmetric with respect to the source layout.

Testing this hypothesis is one of the goals of the experiment.

