# Ra Constants

Universal mathematical constants for harmonic resonance systems.

Portable implementations for Python, TypeScript, Rust, and Haskell.

## Installation

### Python
```bash
pip install ra-constants
```

### TypeScript/JavaScript
```bash
npm install @anywave/ra-constants
```

### Rust
```toml
[dependencies]
ra-constants = "0.1"
```

### Haskell
```cabal
build-depends: ra-constants
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
| A432 | 432.0 | Concert pitch A (natural) |
| A440 | 440.0 | Concert pitch A (standard) |
| SOLFEGGIO_UT | 396.0 | Liberation from fear |
| SOLFEGGIO_RE | 417.0 | Facilitating change |
| SOLFEGGIO_MI | 528.0 | Transformation/DNA repair |
| SOLFEGGIO_FA | 639.0 | Connecting relationships |
| SOLFEGGIO_SOL | 741.0 | Awakening intuition |
| SOLFEGGIO_LA | 852.0 | Returning to spiritual order |

### Material Resonance Frequencies

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

## License

MIT License - (c) 2025 Anywave Creations

## Attribution

Frequency values derived from published physics research and the Rex Research archives.
