/**
 * Mathematical constants - phi, roots, and transcendentals.
 *
 * (c) 2025 Anywave Creations
 * MIT License
 */

// Golden Ratio and derivatives
/** The golden ratio (φ) = (1 + √5) / 2 */
export const PHI: number = 1.618033988749895;

/** Inverse of golden ratio (1/φ) = φ - 1 */
export const PHI_INVERSE: number = 0.6180339887498949;

/** Phi squared (φ²) = φ + 1 */
export const PHI_SQUARED: number = 2.618033988749895;

// Square roots
/** Square root of 2 */
export const SQRT_2: number = 1.4142135623730951;

/** Square root of 3 */
export const SQRT_3: number = 1.7320508075688772;

/** Square root of 5 */
export const SQRT_5: number = 2.23606797749979;

// Transcendental constants
/** Pi (π) */
export const PI: number = 3.141592653589793;

/** Tau (τ) = 2π */
export const TAU: number = 6.283185307179586;

/** Euler's number (e) */
export const E: number = 2.718281828459045;

/**
 * Calculate φ^n using the recurrence relation.
 * @param n The power (can be negative)
 * @returns φ raised to the power n
 */
export function phiPower(n: number): number {
  if (n === 0) return 1.0;
  if (n === 1) return PHI;
  if (n === -1) return PHI_INVERSE;
  if (n > 0) return Math.pow(PHI, n);
  return Math.pow(PHI_INVERSE, -n);
}

/**
 * Calculate the ratio F(n+1)/F(n) which approaches φ.
 * @param n The Fibonacci index (must be >= 1)
 * @returns The ratio of consecutive Fibonacci numbers
 */
export function fibonacciRatio(n: number): number {
  if (n < 1) throw new Error("n must be >= 1");

  let fibPrev = 1;
  let fibCurr = 1;
  for (let i = 0; i < n - 1; i++) {
    [fibPrev, fibCurr] = [fibCurr, fibPrev + fibCurr];
  }

  return fibCurr / fibPrev;
}

/**
 * Check if two values are in golden ratio.
 * @param a First value
 * @param b Second value (should be larger)
 * @param tolerance Acceptable deviation from φ
 * @returns True if b/a is approximately φ
 */
export function isPhiRatio(a: number, b: number, tolerance: number = 0.01): boolean {
  if (a <= 0 || b <= 0) return false;

  const ratio = Math.max(a, b) / Math.min(a, b);
  return Math.abs(ratio - PHI) < tolerance;
}
