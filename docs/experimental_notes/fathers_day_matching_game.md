# Father's Day Matching-Game Recordings

Date: 2026-06-21  
Participants/sources: Dave, Anastasia, Julie, room/car/AC/noise  
Microphones: Daddy phone, Mommy phone, laptop

These recordings are intentionally messy:

- only three microphones,
- changing geometry,
- automatic gain control,
- microphone bumps,
- Julie movement,
- imperfect claps,
- long COVID auditory sensitivity limiting repeated loud claps,
- real family conversation during a matching-card game.

This is useful because it tests where the simple ICA assumptions fail.

## Audio import policy

Raw audio should stay local under `data/raw/` and should not be committed unless all participants consent and file size/privacy implications are acceptable.

Suggested local filenames:

```text
data/raw/fathers_day_2026/
├── daddy_phone.m4a
├── mommy_phone.mp3
└── laptop.m4a
```

## First analysis questions

1. Can the claps be detected in all channels?
2. How much clock drift exists across the recordings?
3. Can short stable-geometry windows be identified?
4. Does ICA behave differently on:
   - the whole recording,
   - Daddy-alone windows,
   - stable card-game windows,
   - post-mic-move windows?
5. What failure modes are audible or visible in spectrograms?
