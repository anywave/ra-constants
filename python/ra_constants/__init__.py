"""
Ra Constants - Universal mathematical constants for harmonic resonance systems.

(c) 2025 Anywave Creations
MIT License
"""

from .frequencies import (
    A432,
    A440,
    SCHUMANN_2ND,
    SCHUMANN_3RD,
    SCHUMANN_4TH,
    SCHUMANN_5TH,
    SCHUMANN_FUNDAMENTAL,
    SCHUMANN_HARMONICS,
    SOLFEGGIO_FA,
    SOLFEGGIO_FREQUENCIES,
    SOLFEGGIO_LA,
    SOLFEGGIO_MI,
    SOLFEGGIO_RE,
    SOLFEGGIO_SOL,
    SOLFEGGIO_UT,
    MaterialFrequency,
)
from .phi import (
    # Core constants
    PHI,
    PHI_INVERSE,
    PHI_SQUARED,
    PI,
    SQRT_2,
    SQRT_3,
    SQRT_5,
    TAU,
    E,
    # Ra System named constants
    GREEN_PHI,
    ANKH,
    RA,
    SCARAB,
    PHI_NEG1,
    PHI_NEG2,
    PHI_NEG3,
    PHI_NEG4,
    # Five φ bands
    PhiBand,
    PhiBandInfo,
    PHI_BANDS,
    PHI_PERIODS,
    PHI_OMEGA,
    PHI_WEIGHTS,
    PHI_BAND_ULTRA,
    PHI_BAND_SLOW,
    PHI_BAND_CORE,
    PHI_BAND_FAST,
    PHI_BAND_RAPID,
    # Functions
    phi_power,
    fibonacci_ratio,
    is_phi_ratio,
    band_frequency_range,
    frequency_to_band,
    compute_multiwave_coherence,
)
from .thresholds import (
    HIGH_COHERENCE,
    LOW_COHERENCE,
    MEDIUM_COHERENCE,
    MINIMUM_COHERENCE,
    CoherenceLevel,
)

__version__ = "0.2.0"
__all__ = [
    # Mathematical core
    "PHI",
    "PHI_INVERSE",
    "PHI_SQUARED",
    "SQRT_2",
    "SQRT_3",
    "SQRT_5",
    "PI",
    "TAU",
    "E",
    # Ra System named powers
    "GREEN_PHI",
    "ANKH",
    "RA",
    "SCARAB",
    "PHI_NEG1",
    "PHI_NEG2",
    "PHI_NEG3",
    "PHI_NEG4",
    # Five φ bands - classes
    "PhiBand",
    "PhiBandInfo",
    "PHI_BAND_ULTRA",
    "PHI_BAND_SLOW",
    "PHI_BAND_CORE",
    "PHI_BAND_FAST",
    "PHI_BAND_RAPID",
    # Five φ bands - dictionaries
    "PHI_BANDS",
    "PHI_PERIODS",
    "PHI_OMEGA",
    "PHI_WEIGHTS",
    # Functions
    "phi_power",
    "fibonacci_ratio",
    "is_phi_ratio",
    "band_frequency_range",
    "frequency_to_band",
    "compute_multiwave_coherence",
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
