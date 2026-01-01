"""
Coherence thresholds - Generic bands for coherence state classification.

(c) 2025 Anywave Creations
MIT License
"""

from enum import Enum
from typing import NamedTuple


# Generic coherence thresholds (not application-specific)
HIGH_COHERENCE: float = 0.85
"""High coherence threshold (85%)"""

MEDIUM_COHERENCE: float = 0.6
"""Medium coherence threshold (60%)"""

LOW_COHERENCE: float = 0.3
"""Low coherence threshold (30%)"""

MINIMUM_COHERENCE: float = 0.1
"""Minimum detectable coherence (10%)"""


class CoherenceBand(NamedTuple):
    """Definition of a coherence band."""
    lower: float  # Lower bound (inclusive)
    upper: float  # Upper bound (exclusive, except for highest band)
    name: str     # Human-readable name


class CoherenceLevel(Enum):
    """Coherence level classification.

    Generic bands for categorizing coherence values.
    """
    PEAK = CoherenceBand(HIGH_COHERENCE, 1.01, "peak")
    HIGH = CoherenceBand(MEDIUM_COHERENCE, HIGH_COHERENCE, "high")
    MEDIUM = CoherenceBand(LOW_COHERENCE, MEDIUM_COHERENCE, "medium")
    LOW = CoherenceBand(MINIMUM_COHERENCE, LOW_COHERENCE, "low")
    MINIMAL = CoherenceBand(0.0, MINIMUM_COHERENCE, "minimal")

    @property
    def lower(self) -> float:
        """Get lower bound of this band."""
        return self.value.lower

    @property
    def upper(self) -> float:
        """Get upper bound of this band."""
        return self.value.upper

    @classmethod
    def classify(cls, value: float) -> "CoherenceLevel":
        """Classify a coherence value into a level.

        Args:
            value: Coherence value (0-1)

        Returns:
            The appropriate CoherenceLevel
        """
        if value < 0 or value > 1:
            raise ValueError("Coherence must be between 0 and 1")

        for level in cls:
            if level.value.lower <= value < level.value.upper:
                return level

        # Handle edge case of exactly 1.0
        return cls.PEAK

    def contains(self, value: float) -> bool:
        """Check if a value falls within this band.

        Args:
            value: Coherence value to check

        Returns:
            True if value is in this band
        """
        return self.value.lower <= value < self.value.upper


def normalize_coherence(value: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
    """Normalize a value to the 0-1 coherence range.

    Args:
        value: Value to normalize
        min_val: Minimum of input range
        max_val: Maximum of input range

    Returns:
        Normalized value between 0 and 1
    """
    if max_val <= min_val:
        raise ValueError("max_val must be greater than min_val")

    normalized = (value - min_val) / (max_val - min_val)
    return max(0.0, min(1.0, normalized))


def coherence_delta(current: float, previous: float) -> float:
    """Calculate the change in coherence between two measurements.

    Args:
        current: Current coherence value
        previous: Previous coherence value

    Returns:
        Delta (positive = increasing coherence)
    """
    return current - previous


def is_coherence_stable(values: list[float], threshold: float = 0.05) -> bool:
    """Check if a series of coherence values is stable.

    Args:
        values: List of coherence measurements
        threshold: Maximum allowed standard deviation

    Returns:
        True if coherence is stable
    """
    if len(values) < 2:
        return True

    mean = sum(values) / len(values)
    variance = sum((v - mean) ** 2 for v in values) / len(values)
    std_dev = variance ** 0.5

    return std_dev <= threshold
