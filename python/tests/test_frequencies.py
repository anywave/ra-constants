"""Tests for frequencies module."""

import pytest

from ra_constants import (
    A432,
    A440,
    SCHUMANN_FUNDAMENTAL,
    SCHUMANN_HARMONICS,
    SOLFEGGIO_MI,
    MaterialFrequency,
)
from ra_constants.frequencies import cents_difference, harmonic_of, octave_of


class TestSchumannFrequencies:
    def test_schumann_fundamental(self):
        assert SCHUMANN_FUNDAMENTAL == 7.83

    def test_schumann_harmonics_length(self):
        assert len(SCHUMANN_HARMONICS) == 5

    def test_schumann_harmonics_first(self):
        assert SCHUMANN_HARMONICS[0] == SCHUMANN_FUNDAMENTAL


class TestMusicalPitch:
    def test_a432(self):
        assert A432 == 432.0

    def test_a440(self):
        assert A440 == 440.0


class TestSolfeggio:
    def test_solfeggio_mi(self):
        """528 Hz - the 'miracle' frequency"""
        assert SOLFEGGIO_MI == 528.0


class TestMaterialFrequency:
    def test_quartz_frequency(self):
        assert MaterialFrequency.QUARTZ.frequency == 32768.0

    def test_gold_affinity(self):
        assert MaterialFrequency.GOLD.alpha_affinity == 0.95

    def test_copper_conductivity(self):
        assert MaterialFrequency.COPPER.conductivity == 0.85

    def test_from_name(self):
        assert MaterialFrequency.from_name("gold") == MaterialFrequency.GOLD
        assert MaterialFrequency.from_name("QUARTZ") == MaterialFrequency.QUARTZ


class TestOctaveOf:
    def test_octave_up(self):
        assert octave_of(440.0, 1) == 880.0

    def test_octave_down(self):
        assert octave_of(440.0, -1) == 220.0

    def test_two_octaves(self):
        assert octave_of(440.0, 2) == 1760.0


class TestHarmonicOf:
    def test_fundamental(self):
        assert harmonic_of(100.0, 1) == 100.0

    def test_second_harmonic(self):
        assert harmonic_of(100.0, 2) == 200.0

    def test_third_harmonic(self):
        assert harmonic_of(100.0, 3) == 300.0

    def test_invalid_harmonic(self):
        with pytest.raises(ValueError):
            harmonic_of(100.0, 0)


class TestCentsDifference:
    def test_octave_is_1200_cents(self):
        assert abs(cents_difference(440.0, 880.0) - 1200.0) < 1e-10

    def test_same_frequency(self):
        assert cents_difference(440.0, 440.0) == 0.0
