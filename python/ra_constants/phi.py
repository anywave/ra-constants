"""
Mathematical constants - phi, roots, and transcendentals.

(c) 2025 Anywave Creations
MIT License
"""

from typing import Dict, NamedTuple
from enum import Enum


# =============================================================================
# CORE CONSTANTS
# =============================================================================

# Golden Ratio and derivatives
PHI: float = 1.618033988749895
"""The golden ratio (φ) = (1 + √5) / 2"""

PHI_INVERSE: float = 0.6180339887498949
"""Inverse of golden ratio (1/φ) = φ - 1"""

PHI_SQUARED: float = 2.618033988749895
"""Phi squared (φ²) = φ + 1"""

# Square roots
SQRT_2: float = 1.4142135623730951
"""Square root of 2"""

SQRT_3: float = 1.7320508075688772
"""Square root of 3"""

SQRT_5: float = 2.23606797749979
"""Square root of 5"""

# Transcendental constants
PI: float = 3.141592653589793
"""Pi (π)"""

TAU: float = 6.283185307179586
"""Tau (τ) = 2π"""

E: float = 2.718281828459045
"""Euler's number (e)"""


# =============================================================================
# PHI POWER FUNCTION
# =============================================================================

def phi_power(n: int) -> float:
    """Calculate φ^n using the recurrence relation.

    Args:
        n: The power (can be negative)

    Returns:
        φ raised to the power n
    """
    if n == 0:
        return 1.0
    elif n == 1:
        return PHI
    elif n == -1:
        return PHI_INVERSE
    elif n > 0:
        return PHI ** n
    else:
        return PHI_INVERSE ** (-n)


# =============================================================================
# FIVE PHI BANDS - Frequency/Period Hierarchy
# =============================================================================

class PhiBandInfo(NamedTuple):
    """Complete information for a φ-scaled frequency band."""
    index: int          # k in φ^k
    frequency: float    # Hz (φ^k)
    period: float       # seconds (1/φ^k)
    omega: float        # rad/sec (2π × φ^k)
    weight: float       # φ^(-|k|) for amplitude weighting
    name: str           # Human-readable name
    description: str    # Physical/biological interpretation


# Pre-computed band definitions
PHI_BAND_ULTRA = PhiBandInfo(
    index=-2,
    frequency=phi_power(-2),      # 0.382 Hz
    period=1.0 / phi_power(-2),   # 2.618 sec
    omega=TAU * phi_power(-2),    # 2.40 rad/sec
    weight=phi_power(-2),         # 0.382
    name="ULTRA",
    description="Ultra-low: Ultradian rhythms, circadian influence"
)

PHI_BAND_SLOW = PhiBandInfo(
    index=-1,
    frequency=phi_power(-1),      # 0.618 Hz
    period=1.0 / phi_power(-1),   # 1.618 sec
    omega=TAU * phi_power(-1),    # 3.88 rad/sec
    weight=phi_power(-1),         # 0.618
    name="SLOW",
    description="Slow: Baroreflex, Mayer waves, blood pressure oscillations"
)

PHI_BAND_CORE = PhiBandInfo(
    index=0,
    frequency=phi_power(0),       # 1.000 Hz
    period=1.0 / phi_power(0),    # 1.000 sec
    omega=TAU * phi_power(0),     # 6.28 rad/sec
    weight=phi_power(0),          # 1.000
    name="CORE",
    description="Core: Reference baseline, ~60 bpm heart rate"
)

PHI_BAND_FAST = PhiBandInfo(
    index=1,
    frequency=phi_power(1),       # 1.618 Hz
    period=1.0 / phi_power(1),    # 0.618 sec
    omega=TAU * phi_power(1),     # 10.16 rad/sec
    weight=phi_power(-1),         # 0.618
    name="FAST",
    description="Fast: Respiratory sinus arrhythmia, breath coupling"
)

PHI_BAND_RAPID = PhiBandInfo(
    index=2,
    frequency=phi_power(2),       # 2.618 Hz
    period=1.0 / phi_power(2),    # 0.382 sec
    omega=TAU * phi_power(2),     # 16.44 rad/sec
    weight=phi_power(-2),         # 0.382
    name="RAPID",
    description="Rapid: Fast breathing, startle response, acute stress"
)


class PhiBand(Enum):
    """Enumeration of the five φ-scaled frequency bands."""
    ULTRA = PHI_BAND_ULTRA
    SLOW = PHI_BAND_SLOW
    CORE = PHI_BAND_CORE
    FAST = PHI_BAND_FAST
    RAPID = PHI_BAND_RAPID

    @property
    def index(self) -> int:
        return self.value.index

    @property
    def frequency(self) -> float:
        return self.value.frequency

    @property
    def period(self) -> float:
        return self.value.period

    @property
    def omega(self) -> float:
        return self.value.omega

    @property
    def weight(self) -> float:
        return self.value.weight

    @property
    def description(self) -> str:
        return self.value.description

    @classmethod
    def from_index(cls, k: int) -> 'PhiBand':
        """Get band by index (-2 to +2)."""
        for band in cls:
            if band.index == k:
                return band
        raise ValueError(f"Invalid band index: {k}. Must be -2 to +2.")

    @classmethod
    def all_bands(cls) -> list:
        """Return all bands in order from ULTRA to RAPID."""
        return [cls.ULTRA, cls.SLOW, cls.CORE, cls.FAST, cls.RAPID]


# Convenience dictionaries for direct access
PHI_BANDS: Dict[str, float] = {
    'ULTRA': phi_power(-2),   # 0.382
    'SLOW':  phi_power(-1),   # 0.618
    'CORE':  phi_power(0),    # 1.000
    'FAST':  phi_power(1),    # 1.618
    'RAPID': phi_power(2),    # 2.618
}
"""φ-scaled frequencies (Hz) for the five coherence bands."""

PHI_PERIODS: Dict[str, float] = {
    'ULTRA': 1.0 / phi_power(-2),   # 2.618 sec
    'SLOW':  1.0 / phi_power(-1),   # 1.618 sec
    'CORE':  1.0 / phi_power(0),    # 1.000 sec
    'FAST':  1.0 / phi_power(1),    # 0.618 sec
    'RAPID': 1.0 / phi_power(2),    # 0.382 sec
}
"""Period equivalents (seconds) for the five coherence bands."""

PHI_OMEGA: Dict[str, float] = {
    'ULTRA': TAU * phi_power(-2),   # 2.40 rad/sec
    'SLOW':  TAU * phi_power(-1),   # 3.88 rad/sec
    'CORE':  TAU * phi_power(0),    # 6.28 rad/sec
    'FAST':  TAU * phi_power(1),    # 10.16 rad/sec
    'RAPID': TAU * phi_power(2),    # 16.44 rad/sec
}
"""Angular frequencies (rad/sec) for the five coherence bands."""

PHI_WEIGHTS: Dict[str, float] = {
    'ULTRA': phi_power(-2),   # 0.382
    'SLOW':  phi_power(-1),   # 0.618
    'CORE':  phi_power(0),    # 1.000
    'FAST':  phi_power(-1),   # 0.618 (symmetric)
    'RAPID': phi_power(-2),   # 0.382 (symmetric)
}
"""Amplitude weights for band contributions (symmetric around CORE)."""


# =============================================================================
# RA SYSTEM NAMED CONSTANTS
# =============================================================================

# Named powers for the Ra System
GREEN_PHI: float = PHI
"""φ¹ ≈ 1.618 - Base golden ratio (consent threshold: FULL)"""

ANKH: float = phi_power(3)
"""φ³ ≈ 4.236 - Cubic extension"""

RA: float = phi_power(5)
"""φ⁵ ≈ 11.090 - Fifth power"""

SCARAB: float = phi_power(7)
"""φ⁷ ≈ 29.034 - Seventh power"""

# Inverse powers for threshold cascade
PHI_NEG1: float = phi_power(-1)
"""φ⁻¹ ≈ 0.618 - DIMINISHED_CONSENT threshold"""

PHI_NEG2: float = phi_power(-2)
"""φ⁻² ≈ 0.382 - SUSPENDED_CONSENT threshold"""

PHI_NEG3: float = phi_power(-3)
"""φ⁻³ ≈ 0.236 - EMERGENCY_OVERRIDE threshold"""

PHI_NEG4: float = phi_power(-4)
"""φ⁻⁴ ≈ 0.146 - Critical minimum"""


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def fibonacci_ratio(n: int) -> float:
    """Calculate the ratio F(n+1)/F(n) which approaches φ.

    Args:
        n: The Fibonacci index (must be >= 1)

    Returns:
        The ratio of consecutive Fibonacci numbers
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    fib_prev, fib_curr = 1, 1
    for _ in range(n - 1):
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr

    return fib_curr / fib_prev


def is_phi_ratio(a: float, b: float, tolerance: float = 0.01) -> bool:
    """Check if two values are in golden ratio.

    Args:
        a: First value
        b: Second value (should be larger)
        tolerance: Acceptable deviation from φ

    Returns:
        True if b/a is approximately φ
    """
    if a <= 0 or b <= 0:
        return False

    ratio = max(a, b) / min(a, b)
    return abs(ratio - PHI) < tolerance


def band_frequency_range(band: PhiBand) -> tuple:
    """Get the frequency range for a φ band.
    
    Uses geometric mean boundaries: (φ^(k-0.5), φ^(k+0.5))
    
    Args:
        band: The PhiBand to get range for
        
    Returns:
        (lower_hz, upper_hz) tuple
    """
    k = band.index
    lower = phi_power(k) / (PHI ** 0.5)  # φ^(k-0.5)
    upper = phi_power(k) * (PHI ** 0.5)  # φ^(k+0.5)
    return (lower, upper)


def frequency_to_band(freq_hz: float) -> PhiBand:
    """Classify a frequency into its φ band.
    
    Args:
        freq_hz: Frequency in Hz
        
    Returns:
        The PhiBand containing this frequency
    """
    for band in PhiBand.all_bands():
        lower, upper = band_frequency_range(band)
        if lower <= freq_hz < upper:
            return band
    
    # Edge cases
    if freq_hz < band_frequency_range(PhiBand.ULTRA)[0]:
        return PhiBand.ULTRA
    return PhiBand.RAPID


def compute_multiwave_coherence(amplitudes: Dict[str, float],
                                phases: Dict[str, float],
                                reference_phase: float = 0.0) -> float:
    """Compute weighted coherence from band amplitudes and phases.
    
    Formula: C = Σ_k w_k × A_k × cos(ψ_k - ψ_ref)
    
    Args:
        amplitudes: Dict mapping band name to amplitude
        phases: Dict mapping band name to phase (radians)
        reference_phase: Reference phase for alignment (default 0)
        
    Returns:
        Scalar coherence value
    """
    import math
    
    total = 0.0
    for band_name, weight in PHI_WEIGHTS.items():
        if band_name in amplitudes and band_name in phases:
            A = amplitudes[band_name]
            psi = phases[band_name]
            total += weight * A * math.cos(psi - reference_phase)
    
    return max(0.0, min(1.0, total))
