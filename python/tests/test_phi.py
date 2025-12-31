"""Tests for phi module."""

import pytest
from ra_constants import PHI, PHI_INVERSE, PHI_SQUARED
from ra_constants.phi import phi_power, fibonacci_ratio, is_phi_ratio


class TestPhiConstants:
    def test_phi_value(self):
        assert abs(PHI - 1.618033988749895) < 1e-10

    def test_phi_inverse_value(self):
        assert abs(PHI_INVERSE - 0.6180339887498949) < 1e-10

    def test_phi_squared_value(self):
        assert abs(PHI_SQUARED - 2.618033988749895) < 1e-10

    def test_phi_identity(self):
        """Test that φ * (1/φ) = 1"""
        assert abs(PHI * PHI_INVERSE - 1.0) < 1e-10

    def test_phi_squared_identity(self):
        """Test that φ² = φ + 1"""
        assert abs(PHI_SQUARED - PHI - 1.0) < 1e-10


class TestPhiPower:
    def test_phi_power_zero(self):
        assert phi_power(0) == 1.0

    def test_phi_power_one(self):
        assert phi_power(1) == PHI

    def test_phi_power_two(self):
        assert abs(phi_power(2) - PHI_SQUARED) < 1e-10

    def test_phi_power_negative_one(self):
        assert phi_power(-1) == PHI_INVERSE


class TestFibonacciRatio:
    def test_fibonacci_ratio_converges(self):
        """Test that F(n+1)/F(n) approaches φ"""
        ratio = fibonacci_ratio(20)
        assert abs(ratio - PHI) < 1e-6

    def test_fibonacci_ratio_invalid_input(self):
        with pytest.raises(ValueError):
            fibonacci_ratio(0)


class TestIsPhiRatio:
    def test_phi_ratio_true(self):
        assert is_phi_ratio(1.0, PHI)
        assert is_phi_ratio(PHI, PHI_SQUARED)

    def test_phi_ratio_false(self):
        assert not is_phi_ratio(1.0, 2.0)

    def test_phi_ratio_negative_values(self):
        assert not is_phi_ratio(-1.0, 1.0)
        assert not is_phi_ratio(1.0, -1.0)
