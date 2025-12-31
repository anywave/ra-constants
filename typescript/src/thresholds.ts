/**
 * Coherence thresholds - Generic bands for coherence state classification.
 *
 * (c) 2025 Anywave Creations
 * MIT License
 */

// Generic coherence thresholds (not application-specific)
/** High coherence threshold (85%) */
export const HIGH_COHERENCE: number = 0.85;

/** Medium coherence threshold (60%) */
export const MEDIUM_COHERENCE: number = 0.6;

/** Low coherence threshold (30%) */
export const LOW_COHERENCE: number = 0.3;

/** Minimum detectable coherence (10%) */
export const MINIMUM_COHERENCE: number = 0.1;

/** Definition of a coherence band */
export interface CoherenceBand {
  lower: number;  // Lower bound (inclusive)
  upper: number;  // Upper bound (exclusive, except for highest band)
  name: string;   // Human-readable name
}

/** Coherence level classification */
export const CoherenceLevel = {
  PEAK: { lower: HIGH_COHERENCE, upper: 1.01, name: "peak" },
  HIGH: { lower: MEDIUM_COHERENCE, upper: HIGH_COHERENCE, name: "high" },
  MEDIUM: { lower: LOW_COHERENCE, upper: MEDIUM_COHERENCE, name: "medium" },
  LOW: { lower: MINIMUM_COHERENCE, upper: LOW_COHERENCE, name: "low" },
  MINIMAL: { lower: 0.0, upper: MINIMUM_COHERENCE, name: "minimal" },
} as const satisfies Record<string, CoherenceBand>;

export type CoherenceLevelName = keyof typeof CoherenceLevel;

/**
 * Classify a coherence value into a level.
 * @param value Coherence value (0-1)
 * @returns The appropriate CoherenceLevel
 */
export function classifyCoherence(value: number): CoherenceBand {
  if (value < 0 || value > 1) {
    throw new Error("Coherence must be between 0 and 1");
  }

  for (const level of Object.values(CoherenceLevel)) {
    if (level.lower <= value && value < level.upper) {
      return level;
    }
  }

  // Handle edge case of exactly 1.0
  return CoherenceLevel.PEAK;
}

/**
 * Check if a value falls within a specific band.
 * @param band The coherence band to check against
 * @param value Coherence value to check
 * @returns True if value is in this band
 */
export function bandContains(band: CoherenceBand, value: number): boolean {
  return band.lower <= value && value < band.upper;
}

/**
 * Normalize a value to the 0-1 coherence range.
 * @param value Value to normalize
 * @param minVal Minimum of input range
 * @param maxVal Maximum of input range
 * @returns Normalized value between 0 and 1
 */
export function normalizeCoherence(
  value: number,
  minVal: number = 0.0,
  maxVal: number = 1.0
): number {
  if (maxVal <= minVal) {
    throw new Error("maxVal must be greater than minVal");
  }

  const normalized = (value - minVal) / (maxVal - minVal);
  return Math.max(0.0, Math.min(1.0, normalized));
}

/**
 * Calculate the change in coherence between two measurements.
 * @param current Current coherence value
 * @param previous Previous coherence value
 * @returns Delta (positive = increasing coherence)
 */
export function coherenceDelta(current: number, previous: number): number {
  return current - previous;
}

/**
 * Check if a series of coherence values is stable.
 * @param values List of coherence measurements
 * @param threshold Maximum allowed standard deviation
 * @returns True if coherence is stable
 */
export function isCoherenceStable(values: number[], threshold: number = 0.05): boolean {
  if (values.length < 2) return true;

  const mean = values.reduce((a, b) => a + b, 0) / values.length;
  const variance = values.reduce((sum, v) => sum + Math.pow(v - mean, 2), 0) / values.length;
  const stdDev = Math.sqrt(variance);

  return stdDev <= threshold;
}
