/**
 * Ra Constants - Universal mathematical constants for harmonic resonance systems.
 *
 * (c) 2025 Anywave Creations
 * MIT License
 */

// Mathematical constants
export {
  PHI,
  PHI_INVERSE,
  PHI_SQUARED,
  SQRT_2,
  SQRT_3,
  SQRT_5,
  PI,
  TAU,
  E,
  phiPower,
  fibonacciRatio,
  isPhiRatio,
} from './phi';

// Frequency constants
export {
  SCHUMANN_FUNDAMENTAL,
  SCHUMANN_2ND,
  SCHUMANN_3RD,
  SCHUMANN_4TH,
  SCHUMANN_5TH,
  SCHUMANN_HARMONICS,
  A432,
  A440,
  SOLFEGGIO_UT,
  SOLFEGGIO_RE,
  SOLFEGGIO_MI,
  SOLFEGGIO_FA,
  SOLFEGGIO_SOL,
  SOLFEGGIO_LA,
  SOLFEGGIO_FREQUENCIES,
  MaterialFrequency,
  octaveOf,
  harmonicOf,
  centsDifference,
} from './frequencies';
export type { MaterialProperties, MaterialName } from './frequencies';

// Coherence thresholds
export {
  HIGH_COHERENCE,
  MEDIUM_COHERENCE,
  LOW_COHERENCE,
  MINIMUM_COHERENCE,
  CoherenceLevel,
  classifyCoherence,
  bandContains,
  normalizeCoherence,
  coherenceDelta,
  isCoherenceStable,
} from './thresholds';
export type { CoherenceBand, CoherenceLevelName } from './thresholds';

export const VERSION = '0.1.0';
