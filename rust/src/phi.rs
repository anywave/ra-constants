//! Mathematical constants - phi, roots, and transcendentals.
//!
//! (c) 2025 Anywave Creations
//! MIT License

/// The golden ratio (φ) = (1 + √5) / 2
pub const PHI: f64 = 1.618033988749895;

/// Inverse of golden ratio (1/φ) = φ - 1
pub const PHI_INVERSE: f64 = 0.6180339887498949;

/// Phi squared (φ²) = φ + 1
pub const PHI_SQUARED: f64 = 2.618033988749895;

/// Square root of 2
pub const SQRT_2: f64 = std::f64::consts::SQRT_2;

/// Square root of 3
pub const SQRT_3: f64 = 1.7320508075688772;

/// Square root of 5
pub const SQRT_5: f64 = 2.23606797749979;

/// Pi (π)
pub const PI: f64 = std::f64::consts::PI;

/// Tau (τ) = 2π
pub const TAU: f64 = std::f64::consts::TAU;

/// Euler's number (e)
pub const E: f64 = std::f64::consts::E;

/// Calculate φ^n using the recurrence relation.
///
/// # Arguments
/// * `n` - The power (can be negative)
///
/// # Returns
/// φ raised to the power n
pub fn phi_power(n: i32) -> f64 {
    match n {
        0 => 1.0,
        1 => PHI,
        -1 => PHI_INVERSE,
        n if n > 0 => PHI.powi(n),
        n => PHI_INVERSE.powi(-n),
    }
}

/// Calculate the ratio F(n+1)/F(n) which approaches φ.
///
/// # Arguments
/// * `n` - The Fibonacci index (must be >= 1)
///
/// # Returns
/// The ratio of consecutive Fibonacci numbers
///
/// # Panics
/// Panics if n < 1
pub fn fibonacci_ratio(n: u32) -> f64 {
    if n < 1 {
        panic!("n must be >= 1");
    }

    let mut fib_prev: u64 = 1;
    let mut fib_curr: u64 = 1;

    for _ in 0..n.saturating_sub(1) {
        let temp = fib_curr;
        fib_curr = fib_prev.saturating_add(fib_curr);
        fib_prev = temp;
    }

    fib_curr as f64 / fib_prev as f64
}

/// Check if two values are in golden ratio.
///
/// # Arguments
/// * `a` - First value
/// * `b` - Second value (should be larger)
/// * `tolerance` - Acceptable deviation from φ
///
/// # Returns
/// True if b/a is approximately φ
pub fn is_phi_ratio(a: f64, b: f64, tolerance: f64) -> bool {
    if a <= 0.0 || b <= 0.0 {
        return false;
    }

    let ratio = a.max(b) / a.min(b);
    (ratio - PHI).abs() < tolerance
}

/// Check if two values are in golden ratio with default tolerance of 0.01.
pub fn is_phi_ratio_default(a: f64, b: f64) -> bool {
    is_phi_ratio(a, b, 0.01)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_phi_constants() {
        assert!((PHI * PHI_INVERSE - 1.0).abs() < 1e-10);
        assert!((PHI_SQUARED - PHI - 1.0).abs() < 1e-10);
    }

    #[test]
    fn test_phi_power() {
        assert!((phi_power(0) - 1.0).abs() < 1e-10);
        assert!((phi_power(1) - PHI).abs() < 1e-10);
        assert!((phi_power(2) - PHI_SQUARED).abs() < 1e-10);
    }

    #[test]
    fn test_fibonacci_ratio_converges() {
        let ratio = fibonacci_ratio(20);
        assert!((ratio - PHI).abs() < 1e-6);
    }

    #[test]
    fn test_is_phi_ratio() {
        assert!(is_phi_ratio_default(1.0, PHI));
        assert!(is_phi_ratio_default(PHI, PHI_SQUARED));
        assert!(!is_phi_ratio_default(1.0, 2.0));
    }
}
