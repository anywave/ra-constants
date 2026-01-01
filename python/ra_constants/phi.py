"""
Mathematical constants - phi, roots, and transcendentals.

(c) 2025 Anywave Creations
MIT License
"""


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
