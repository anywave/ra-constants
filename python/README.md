# ra-constants (Python)

Mathematical constants and reference frequencies for harmonic-resonance modelling.

```bash
pip install ra-constants
```

```python
from ra_constants import PHI, SCHUMANN_FUNDAMENTAL, MaterialFrequency

ratio = PHI * PHI                      # 2.618...
base_freq = SCHUMANN_FUNDAMENTAL       # 7.83 Hz
quartz_freq = MaterialFrequency.QUARTZ # 32768 Hz
```

**Scope.** The mathematical constants are standard. The frequency and material tables are modelling inputs collected
from mixed sources, including traditional and esoteric ones. Their labels describe the tradition a value comes from,
not a measured physical, biological or health effect.

`ra_constants.bateman` holds Wesley H. Bateman's Ra-system values (Red Pi = 84823/27000, Hunab, H-Bar, the colour
ratio, the Rac units) as printed in *The Rods of Amon Ra* and verified page by page. They are his units, not physics
claims.

Source, other language bindings, issues and security reporting: https://github.com/anywave/ra-constants

MIT License - (c) 2025 Anywave Creations.
