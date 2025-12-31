"""Tests for thresholds module."""

import pytest
from ra_constants import (
    HIGH_COHERENCE,
    MEDIUM_COHERENCE,
    LOW_COHERENCE,
    MINIMUM_COHERENCE,
    CoherenceLevel,
)
from ra_constants.thresholds import (
    normalize_coherence,
    coherence_delta,
    is_coherence_stable,
)


class TestCoherenceConstants:
    def test_high_coherence(self):
        assert HIGH_COHERENCE == 0.85

    def test_medium_coherence(self):
        assert MEDIUM_COHERENCE == 0.6

    def test_low_coherence(self):
        assert LOW_COHERENCE == 0.3

    def test_minimum_coherence(self):
        assert MINIMUM_COHERENCE == 0.1


class TestCoherenceLevel:
    def test_classify_peak(self):
        assert CoherenceLevel.classify(0.9) == CoherenceLevel.PEAK

    def test_classify_high(self):
        assert CoherenceLevel.classify(0.7) == CoherenceLevel.HIGH

    def test_classify_medium(self):
        assert CoherenceLevel.classify(0.4) == CoherenceLevel.MEDIUM

    def test_classify_low(self):
        assert CoherenceLevel.classify(0.2) == CoherenceLevel.LOW

    def test_classify_minimal(self):
        assert CoherenceLevel.classify(0.05) == CoherenceLevel.MINIMAL

    def test_classify_boundary_high(self):
        assert CoherenceLevel.classify(0.85) == CoherenceLevel.PEAK

    def test_classify_exactly_one(self):
        assert CoherenceLevel.classify(1.0) == CoherenceLevel.PEAK

    def test_classify_invalid_negative(self):
        with pytest.raises(ValueError):
            CoherenceLevel.classify(-0.1)

    def test_classify_invalid_over_one(self):
        with pytest.raises(ValueError):
            CoherenceLevel.classify(1.1)

    def test_contains(self):
        assert CoherenceLevel.PEAK.contains(0.9)
        assert not CoherenceLevel.PEAK.contains(0.5)


class TestNormalizeCoherence:
    def test_normalize_middle(self):
        assert abs(normalize_coherence(50.0, 0.0, 100.0) - 0.5) < 1e-10

    def test_normalize_clamp_low(self):
        assert normalize_coherence(-10.0, 0.0, 100.0) == 0.0

    def test_normalize_clamp_high(self):
        assert normalize_coherence(150.0, 0.0, 100.0) == 1.0

    def test_normalize_invalid_range(self):
        with pytest.raises(ValueError):
            normalize_coherence(50.0, 100.0, 0.0)


class TestCoherenceDelta:
    def test_positive_delta(self):
        assert coherence_delta(0.8, 0.5) == 0.3

    def test_negative_delta(self):
        assert coherence_delta(0.5, 0.8) == -0.3


class TestIsCoherenceStable:
    def test_stable_values(self):
        assert is_coherence_stable([0.5, 0.51, 0.49, 0.5])

    def test_unstable_values(self):
        assert not is_coherence_stable([0.1, 0.9, 0.1, 0.9])

    def test_single_value(self):
        assert is_coherence_stable([0.5])

    def test_empty_list(self):
        assert is_coherence_stable([])
