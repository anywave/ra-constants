/**
 * Frequency constants - Schumann resonances, musical pitches, and material frequencies.
 *
 * (c) 2025 Anywave Creations
 * MIT License
 */

// Schumann Resonances (Earth's electromagnetic resonant frequencies)
/** Schumann resonance fundamental frequency (Hz) */
export const SCHUMANN_FUNDAMENTAL: number = 7.83;

/** Second Schumann harmonic (Hz) */
export const SCHUMANN_2ND: number = 14.3;

/** Third Schumann harmonic (Hz) */
export const SCHUMANN_3RD: number = 20.8;

/** Fourth Schumann harmonic (Hz) */
export const SCHUMANN_4TH: number = 27.3;

/** Fifth Schumann harmonic (Hz) */
export const SCHUMANN_5TH: number = 33.8;

/** All Schumann harmonics as a tuple */
export const SCHUMANN_HARMONICS: readonly number[] = [
  SCHUMANN_FUNDAMENTAL,
  SCHUMANN_2ND,
  SCHUMANN_3RD,
  SCHUMANN_4TH,
  SCHUMANN_5TH,
] as const;

// Musical Pitch Standards
/** Concert pitch A at 432 Hz (natural/Verdi tuning) */
export const A432: number = 432.0;

/** Concert pitch A at 440 Hz (ISO 16 standard) */
export const A440: number = 440.0;

// Solfeggio Frequencies (ancient scale)
/** Ut (Do) - Liberation from fear and guilt */
export const SOLFEGGIO_UT: number = 396.0;

/** Re - Facilitating change, undoing situations */
export const SOLFEGGIO_RE: number = 417.0;

/** Mi - Transformation, miracles, DNA repair */
export const SOLFEGGIO_MI: number = 528.0;

/** Fa - Connecting relationships, harmony */
export const SOLFEGGIO_FA: number = 639.0;

/** Sol - Awakening intuition, expression */
export const SOLFEGGIO_SOL: number = 741.0;

/** La - Returning to spiritual order */
export const SOLFEGGIO_LA: number = 852.0;

/** All Solfeggio frequencies as a tuple */
export const SOLFEGGIO_FREQUENCIES: readonly number[] = [
  SOLFEGGIO_UT,
  SOLFEGGIO_RE,
  SOLFEGGIO_MI,
  SOLFEGGIO_FA,
  SOLFEGGIO_SOL,
  SOLFEGGIO_LA,
] as const;

/** Properties of a resonant material */
export interface MaterialProperties {
  frequency: number;      // Base frequency in Hz
  alphaAffinity: number;  // Coherence affinity (0-1)
  conductivity: number;   // Electrical/energetic conductivity (0-1)
}

/** Material resonance frequencies and properties */
export const MaterialFrequency = {
  Quartz: { frequency: 32768.0, alphaAffinity: 0.9, conductivity: 0.3 },
  Gold: { frequency: 24576.0, alphaAffinity: 0.95, conductivity: 0.95 },
  Silver: { frequency: 20480.0, alphaAffinity: 0.85, conductivity: 0.9 },
  Copper: { frequency: 16384.0, alphaAffinity: 0.8, conductivity: 0.85 },
  Iron: { frequency: 12288.0, alphaAffinity: 0.6, conductivity: 0.5 },
  Obsidian: { frequency: 8192.0, alphaAffinity: 0.7, conductivity: 0.1 },
  Granite: { frequency: 4096.0, alphaAffinity: 0.5, conductivity: 0.05 },
  Limestone: { frequency: 2048.0, alphaAffinity: 0.4, conductivity: 0.02 },
} as const satisfies Record<string, MaterialProperties>;

export type MaterialName = keyof typeof MaterialFrequency;

/**
 * Calculate frequency shifted by octaves.
 * @param frequency Base frequency in Hz
 * @param octaves Number of octaves to shift (positive = up, negative = down)
 * @returns Shifted frequency
 */
export function octaveOf(frequency: number, octaves: number = 1): number {
  return frequency * Math.pow(2, octaves);
}

/**
 * Calculate the nth harmonic of a frequency.
 * @param frequency Fundamental frequency in Hz
 * @param harmonic Harmonic number (1 = fundamental, 2 = first overtone, etc.)
 * @returns Harmonic frequency
 */
export function harmonicOf(frequency: number, harmonic: number): number {
  if (harmonic < 1) throw new Error("Harmonic must be >= 1");
  return frequency * harmonic;
}

/**
 * Calculate the difference between two frequencies in cents.
 * @param freq1 First frequency
 * @param freq2 Second frequency
 * @returns Difference in cents (100 cents = 1 semitone)
 */
export function centsDifference(freq1: number, freq2: number): number {
  return 1200 * Math.log2(freq2 / freq1);
}
