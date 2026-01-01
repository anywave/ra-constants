from __future__ import annotations

"""
Frequency constants - Schumann resonances, musical pitches, and material frequencies.

(c) 2025 Anywave Creations
MIT License
"""

from enum import Enum
from typing import NamedTuple


# Schumann Resonances (Earth's electromagnetic resonant frequencies)
SCHUMANN_FUNDAMENTAL: float = 7.83
"""Schumann resonance fundamental frequency (Hz)"""

SCHUMANN_2ND: float = 14.3
"""Second Schumann harmonic (Hz)"""

SCHUMANN_3RD: float = 20.8
"""Third Schumann harmonic (Hz)"""

SCHUMANN_4TH: float = 27.3
"""Fourth Schumann harmonic (Hz)"""

SCHUMANN_5TH: float = 33.8
"""Fifth Schumann harmonic (Hz)"""

SCHUMANN_HARMONICS: tuple[float, ...] = (
    SCHUMANN_FUNDAMENTAL,
    SCHUMANN_2ND,
    SCHUMANN_3RD,
    SCHUMANN_4TH,
    SCHUMANN_5TH,
)
"""All Schumann harmonics as a tuple"""


# Musical Pitch Standards
A432: float = 432.0
"""Concert pitch A at 432 Hz (natural/Verdi tuning)"""

A440: float = 440.0
"""Concert pitch A at 440 Hz (ISO 16 standard)"""


# Solfeggio Frequencies (ancient scale)
SOLFEGGIO_UT: float = 396.0
"""Ut (Do) - Liberation from fear and guilt"""

SOLFEGGIO_RE: float = 417.0
"""Re - Facilitating change, undoing situations"""

SOLFEGGIO_MI: float = 528.0
"""Mi - Transformation, miracles, DNA repair"""

SOLFEGGIO_FA: float = 639.0
"""Fa - Connecting relationships, harmony"""

SOLFEGGIO_SOL: float = 741.0
"""Sol - Awakening intuition, expression"""

SOLFEGGIO_LA: float = 852.0
"""La - Returning to spiritual order"""

SOLFEGGIO_FREQUENCIES: tuple[float, ...] = (
    SOLFEGGIO_UT,
    SOLFEGGIO_RE,
    SOLFEGGIO_MI,
    SOLFEGGIO_FA,
    SOLFEGGIO_SOL,
    SOLFEGGIO_LA,
)
"""All Solfeggio frequencies as a tuple"""


class MaterialProperties(NamedTuple):
    """Properties of a resonant material."""
    frequency: float  # Base frequency in Hz
    alpha_affinity: float  # Coherence affinity (0-1)
    conductivity: float  # Electrical/energetic conductivity (0-1)


class MaterialFrequency(Enum):
    """Material resonance frequencies and properties.

    Based on crystallographic and electromagnetic properties.
    """
    QUARTZ = MaterialProperties(32768.0, 0.9, 0.3)
    GOLD = MaterialProperties(24576.0, 0.95, 0.95)
    SILVER = MaterialProperties(20480.0, 0.85, 0.9)
    COPPER = MaterialProperties(16384.0, 0.8, 0.85)
    IRON = MaterialProperties(12288.0, 0.6, 0.5)
    OBSIDIAN = MaterialProperties(8192.0, 0.7, 0.1)
    GRANITE = MaterialProperties(4096.0, 0.5, 0.05)
    LIMESTONE = MaterialProperties(2048.0, 0.4, 0.02)

    @property
    def frequency(self) -> float:
        """Get the base resonance frequency in Hz."""
        return self.value.frequency

    @property
    def alpha_affinity(self) -> float:
        """Get the alpha/coherence affinity (0-1)."""
        return self.value.alpha_affinity

    @property
    def conductivity(self) -> float:
        """Get the conductivity factor (0-1)."""
        return self.value.conductivity

    @classmethod
    def from_name(cls, name: str) -> "MaterialFrequency":
        """Get material by name (case-insensitive)."""
        return cls[name.upper()]


def octave_of(frequency: float, octaves: int = 1) -> float:
    """Calculate frequency shifted by octaves.

    Args:
        frequency: Base frequency in Hz
        octaves: Number of octaves to shift (positive = up, negative = down)

    Returns:
        Shifted frequency
    """
    return frequency * (2 ** octaves)


def harmonic_of(frequency: float, harmonic: int) -> float:
    """Calculate the nth harmonic of a frequency.

    Args:
        frequency: Fundamental frequency in Hz
        harmonic: Harmonic number (1 = fundamental, 2 = first overtone, etc.)

    Returns:
        Harmonic frequency
    """
    if harmonic < 1:
        raise ValueError("Harmonic must be >= 1")
    return frequency * harmonic


def cents_difference(freq1: float, freq2: float) -> float:
    """Calculate the difference between two frequencies in cents.

    Args:
        freq1: First frequency
        freq2: Second frequency

    Returns:
        Difference in cents (100 cents = 1 semitone)
    """
    import math
    return 1200 * math.log2(freq2 / freq1)
