# Development Notes

## Near-term target

Get something public on GitHub by the end of the week.

Minimum public artifact:

- README explains the project.
- Synthetic experiment description exists.
- `src/` package imports.
- One script generates synthetic mixtures and runs FastICA.
- Raw family audio is documented but not committed.

## Caution

Do not over-design the first implementation. The value is in the ladder:

1. clean synthetic case,
2. extra microphone variants,
3. messy family recordings,
4. failure-mode analysis.

## Commands

```bash
pip install -e ".[dev]"
pytest
python scripts/run_synthetic_0p0.py
```
