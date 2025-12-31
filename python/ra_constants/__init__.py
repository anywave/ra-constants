"""
Ra Constants - Universal mathematical constants for harmonic resonance systems.

(c) 2025 Anywave Creations
MIT License
"""

from .phi import (
    PHI,
    PHI_INVERSE,
    PHI_SQUARED,
    SQRT_2,
    SQRT_3,
    SQRT_5,
    PI,
    TAU,
    E,
)

from .frequencies import (
    SCHUMANN_FUNDAMENTAL,
    SCHUMANN_2ND,
    SCHUMANN_3RD,
    SCHUMANN_4TH,
    SCHUMANN_5TH,
    SCHUMANN_HARMONICS,
    A432,
    A440,
    SOLFEGGIO_UT,
    SOLFEGGIO_RE,
    SOLFEGGIO_MI,
    SOLFEGGIO_FA,
    SOLFEGGIO_SOL,
    SOLFEGGIO_LA,
    SOLFEGGIO_FREQUENCIES,
    MaterialFrequency,
)

from .thresholds import (
    HIGH_COHERENCE,
    MEDIUM_COHERENCE,
    LOW_COHERENCE,
    MINIMUM_COHERENCE,
    CoherenceLevel,
)

__version__ = "0.1.0"
__all__ = [
    # Mathematical
    "PHI",
    "PHI_INVERSE",
    "PHI_SQUARED",
    "SQRT_2",
    "SQRT_3",
    "SQRT_5",
    "PI",
    "TAU",
    "E",
    # Frequencies
    "SCHUMANN_FUNDAMENTAL",
    "SCHUMANN_2ND",
    "SCHUMANN_3RD",
    "SCHUMANN_4TH",
    "SCHUMANN_5TH",
    "SCHUMANN_HARMONICS",
    "A432",
    "A440",
    "SOLFEGGIO_UT",
    "SOLFEGGIO_RE",
    "SOLFEGGIO_MI",
    "SOLFEGGIO_FA",
    "SOLFEGGIO_SOL",
    "SOLFEGGIO_LA",
    "SOLFEGGIO_FREQUENCIES",
    "MaterialFrequency",
    # Thresholds
    "HIGH_COHERENCE",
    "MEDIUM_COHERENCE",
    "LOW_COHERENCE",
    "MINIMUM_COHERENCE",
    "CoherenceLevel",
]
