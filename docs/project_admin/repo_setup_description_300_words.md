# Repository setup description

**Pocket Cocktail Party: Blind Source Separation through Geometry, Harmonics, and Signal Mixing** is a compact portfolio project about the classic cocktail party problem: recovering hidden sound sources from mixed microphone recordings.

The project starts with classical Independent Component Analysis (ICA), then progressively adds the complications that make real source separation interesting. The first experiment is synthetic and fully controlled: five instrument-like sources are arranged on a regular pentagon, with one close microphone per source. The mixing matrix is not arbitrary; it is generated from microphone geometry and distance-based amplitude attenuation. Because the synthetic sources and mixing matrix are known, the project can measure how well FastICA recovers the original signals.

Later synthetic experiments add a sixth microphone at the center or overhead, testing whether overdetermined recordings improve recovery and what ICA does with extra channels. The musical sources are modeled with simple harmonic overtone arrays, beginning with voice, violin, guitar, piano/bass, and snare-like percussion. This keeps the implementation lightweight while making the signal structure more realistic than unrelated sine waves.

The real-data track uses family recordings from three microphones during a Father’s Day matching-card game. These recordings include movement, automatic gain control, microphone bumps, room/car noise, and imperfect synchronization claps. Those problems are treated as valuable data rather than mistakes: they show where textbook ICA assumptions begin to fail.

The repository is designed to demonstrate experiment design, signal-processing judgment, practical Python implementation, and clear analysis of assumptions and failure modes—not merely the ability to call an existing ICA function.
