# Ra Constants

Mathematical constants and reference frequencies for harmonic-resonance modelling.

Portable implementations for Python, TypeScript, Rust, and Haskell.

> **Scope.** The mathematical constants (φ, π, e, square roots) are standard. The frequency and material tables are
> modelling inputs collected from mixed sources, including traditional and esoteric ones. Their labels describe the
> tradition a value comes from, not a measured physical, biological or health effect. Treat them as parameters, not facts.

## Installation

### Python
```bash
pip install ra-constants
```

Only the Python package is published (PyPI). The TypeScript, Rust and Haskell bindings are not yet published to npm,
crates.io or Hackage; build them from this repository:

### TypeScript/JavaScript
```bash
cd typescript && npm install && npm run build
```

### Rust
```toml
[dependencies]
ra-constants = { git = "https://github.com/anywave/ra-constants" }
```

### Haskell
```bash
cd haskell && cabal build
```

## Constants

### Mathematical Foundations

| Constant | Symbol | Value | Description |
|----------|--------|-------|-------------|
| PHI | φ | 1.618033988749895 | Golden ratio |
| PHI_INVERSE | 1/φ | 0.6180339887498949 | Inverse golden ratio |
| PHI_SQUARED | φ² | 2.618033988749895 | Phi squared |
| SQRT_2 | √2 | 1.4142135623730951 | Square root of 2 |
| SQRT_3 | √3 | 1.7320508075688772 | Square root of 3 |
| SQRT_5 | √5 | 2.23606797749979 | Square root of 5 |
| PI | π | 3.141592653589793 | Pi |
| TAU | τ | 6.283185307179586 | 2π |
| E | e | 2.718281828459045 | Euler's number |

### Frequency Constants

| Constant | Value (Hz) | Description |
|----------|------------|-------------|
| SCHUMANN_FUNDAMENTAL | 7.83 | Earth resonance fundamental |
| SCHUMANN_2ND | 14.3 | Second Schumann harmonic |
| SCHUMANN_3RD | 20.8 | Third Schumann harmonic |
| SCHUMANN_4TH | 27.3 | Fourth Schumann harmonic |
| SCHUMANN_5TH | 33.8 | Fifth Schumann harmonic |
| A432 | 432.0 | Alternative concert pitch A |
| A440 | 440.0 | Concert pitch A (standard) |
| SOLFEGGIO_UT | 396.0 | Traditional association: liberation from fear |
| SOLFEGGIO_RE | 417.0 | Traditional association: change |
| SOLFEGGIO_MI | 528.0 | Traditional association: transformation (no evidence of biological effect) |
| SOLFEGGIO_FA | 639.0 | Traditional association: relationships |
| SOLFEGGIO_SOL | 741.0 | Traditional association: intuition |
| SOLFEGGIO_LA | 852.0 | Traditional association: spiritual order |

### Material Resonance Frequencies

Modelling values on a power-of-two scale (the quartz value is the common 32.768 kHz watch-crystal frequency). They are
not measured acoustic or electromagnetic resonances of the bulk materials.

| Material | Base Frequency (Hz) | Alpha Affinity | Conductivity |
|----------|---------------------|----------------|--------------|
| Quartz | 32768 | 0.9 | 0.3 |
| Gold | 24576 | 0.95 | 0.95 |
| Silver | 20480 | 0.85 | 0.9 |
| Copper | 16384 | 0.8 | 0.85 |
| Iron | 12288 | 0.6 | 0.5 |
| Obsidian | 8192 | 0.7 | 0.1 |
| Granite | 4096 | 0.5 | 0.05 |
| Limestone | 2048 | 0.4 | 0.02 |

### Coherence Thresholds (Generic)

| Threshold | Value | Description |
|-----------|-------|-------------|
| HIGH_COHERENCE | 0.85 | High coherence state |
| MEDIUM_COHERENCE | 0.6 | Medium coherence state |
| LOW_COHERENCE | 0.3 | Low coherence state |
| MINIMUM_COHERENCE | 0.1 | Minimum detectable coherence |

### Bateman's Ra-System Values (Python: `ra_constants.bateman`)

Wesley H. Bateman's own constants from *The Rods of Amon Ra* (1992-1997), as printed and verified page by page by the
lattice's TR node (2026-08/09). They are his units and ratios, not physics claims; where he borrows a physics name
(H-Bar, Rydberg, fine structure) the value is his, not the physical constant. Exact forms are given as `Fraction`.

| Name | Value | Exact form |
|------|-------|------------|
| Red Pi | 3.141592592... | 84823/27000 (84823 = round(π × 27000); not π) |
| Green Pi | 3.142696805 | (20/9)√2 |
| Blue Pi | 3.143801406 | Green Pi × r |
| Colour ratio r | 1.000351482 | 60000√2/84823 (r² for areas, r³ for volumes) |
| Omega | 1.005662978 | 32√2/45 |
| Hunab | 1.0602875 | 84823/80000 |
| H-Bar | 1.0546875 | 135/128 |
| Ankh | 5.08938 | 3 × 84823/50000 = Red Pi × 1.62 |
| f.s.Δ | 0.0013717421 | 1/729 |
| Ra Rydberg | 1.09739369 | 800/729 |
| Repitan n | n/27 | exact |

The package-level `ANKH`, `RA`, `SCARAB` and `GREEN_PHI` are this package's names for powers of φ, not Bateman's
values of the same name. Bateman's spectral values sit a constant ~545 ppm from measured hydrogen lines because he used
his own Rydberg; that offset is his and is not corrected here.

## Usage

### Python
```python
from ra_constants import PHI, SCHUMANN_FUNDAMENTAL, MaterialFrequency

# Mathematical constants
ratio = PHI * PHI  # 2.618...

# Frequencies
base_freq = SCHUMANN_FUNDAMENTAL  # 7.83 Hz

# Material lookup
quartz_freq = MaterialFrequency.QUARTZ  # 32768 Hz
```

### TypeScript
```typescript
import { PHI, SCHUMANN_FUNDAMENTAL, MaterialFrequency } from '@anywave/ra-constants';

const ratio = PHI * PHI;
const baseFreq = SCHUMANN_FUNDAMENTAL;
const quartzFreq = MaterialFrequency.Quartz;
```

### Rust
```rust
use ra_constants::{PHI, SCHUMANN_FUNDAMENTAL, MaterialFrequency};

let ratio = PHI * PHI;
let base_freq = SCHUMANN_FUNDAMENTAL;
let quartz_freq = MaterialFrequency::Quartz.frequency();
```

### Haskell
```haskell
import Ra.Constants (phi, schumannFundamental, materialFrequency, Material(..))

ratio = phi * phi
baseFreq = schumannFundamental
quartzFreq = materialFrequency Quartz
```

## Attribution

Schumann resonance values follow published geophysics measurements. Solfeggio values and their associations come from
popular and esoteric sources collected in the Rex Research archive; they are not established science. Material values
are modelling choices.

## Citation

See [CITATION.cff](CITATION.cff).

## Security

See [SECURITY.md](SECURITY.md).

## License

MIT License - (c) 2025 Anywave Creations. See [LICENSE](LICENSE).
