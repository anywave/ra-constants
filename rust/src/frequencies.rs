//! Frequency constants - Schumann resonances, musical pitches, and material frequencies.
//!
//! (c) 2025 Anywave Creations
//! MIT License

/// Schumann resonance fundamental frequency (Hz)
pub const SCHUMANN_FUNDAMENTAL: f64 = 7.83;

/// Second Schumann harmonic (Hz)
pub const SCHUMANN_2ND: f64 = 14.3;

/// Third Schumann harmonic (Hz)
pub const SCHUMANN_3RD: f64 = 20.8;

/// Fourth Schumann harmonic (Hz)
pub const SCHUMANN_4TH: f64 = 27.3;

/// Fifth Schumann harmonic (Hz)
pub const SCHUMANN_5TH: f64 = 33.8;

/// All Schumann harmonics
pub const SCHUMANN_HARMONICS: [f64; 5] = [
    SCHUMANN_FUNDAMENTAL,
    SCHUMANN_2ND,
    SCHUMANN_3RD,
    SCHUMANN_4TH,
    SCHUMANN_5TH,
];

/// Concert pitch A at 432 Hz (natural/Verdi tuning)
pub const A432: f64 = 432.0;

/// Concert pitch A at 440 Hz (ISO 16 standard)
pub const A440: f64 = 440.0;

/// Ut (Do) - Liberation from fear and guilt
pub const SOLFEGGIO_UT: f64 = 396.0;

/// Re - Facilitating change, undoing situations
pub const SOLFEGGIO_RE: f64 = 417.0;

/// Mi - Transformation, miracles, DNA repair
pub const SOLFEGGIO_MI: f64 = 528.0;

/// Fa - Connecting relationships, harmony
pub const SOLFEGGIO_FA: f64 = 639.0;

/// Sol - Awakening intuition, expression
pub const SOLFEGGIO_SOL: f64 = 741.0;

/// La - Returning to spiritual order
pub const SOLFEGGIO_LA: f64 = 852.0;

/// All Solfeggio frequencies
pub const SOLFEGGIO_FREQUENCIES: [f64; 6] = [
    SOLFEGGIO_UT,
    SOLFEGGIO_RE,
    SOLFEGGIO_MI,
    SOLFEGGIO_FA,
    SOLFEGGIO_SOL,
    SOLFEGGIO_LA,
];

/// Properties of a resonant material
#[derive(Debug, Clone, Copy, PartialEq)]
pub struct MaterialProperties {
    /// Base frequency in Hz
    pub frequency: f64,
    /// Coherence affinity (0-1)
    pub alpha_affinity: f64,
    /// Electrical/energetic conductivity (0-1)
    pub conductivity: f64,
}

impl MaterialProperties {
    /// Create new material properties
    pub const fn new(frequency: f64, alpha_affinity: f64, conductivity: f64) -> Self {
        Self {
            frequency,
            alpha_affinity,
            conductivity,
        }
    }
}

/// Material resonance frequencies and properties
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum MaterialFrequency {
    Quartz,
    Gold,
    Silver,
    Copper,
    Iron,
    Obsidian,
    Granite,
    Limestone,
}

impl MaterialFrequency {
    /// Get the properties for this material
    pub const fn properties(&self) -> MaterialProperties {
        match self {
            Self::Quartz => MaterialProperties::new(32768.0, 0.9, 0.3),
            Self::Gold => MaterialProperties::new(24576.0, 0.95, 0.95),
            Self::Silver => MaterialProperties::new(20480.0, 0.85, 0.9),
            Self::Copper => MaterialProperties::new(16384.0, 0.8, 0.85),
            Self::Iron => MaterialProperties::new(12288.0, 0.6, 0.5),
            Self::Obsidian => MaterialProperties::new(8192.0, 0.7, 0.1),
            Self::Granite => MaterialProperties::new(4096.0, 0.5, 0.05),
            Self::Limestone => MaterialProperties::new(2048.0, 0.4, 0.02),
        }
    }

    /// Get the base resonance frequency in Hz
    pub const fn frequency(&self) -> f64 {
        self.properties().frequency
    }

    /// Get the alpha/coherence affinity (0-1)
    pub const fn alpha_affinity(&self) -> f64 {
        self.properties().alpha_affinity
    }

    /// Get the conductivity factor (0-1)
    pub const fn conductivity(&self) -> f64 {
        self.properties().conductivity
    }
}

/// Calculate frequency shifted by octaves.
///
/// # Arguments
/// * `frequency` - Base frequency in Hz
/// * `octaves` - Number of octaves to shift (positive = up, negative = down)
///
/// # Returns
/// Shifted frequency
pub fn octave_of(frequency: f64, octaves: i32) -> f64 {
    frequency * 2.0_f64.powi(octaves)
}

/// Calculate the nth harmonic of a frequency.
///
/// # Arguments
/// * `frequency` - Fundamental frequency in Hz
/// * `harmonic` - Harmonic number (1 = fundamental, 2 = first overtone, etc.)
///
/// # Returns
/// Harmonic frequency
///
/// # Panics
/// Panics if harmonic < 1
pub fn harmonic_of(frequency: f64, harmonic: u32) -> f64 {
    if harmonic < 1 {
        panic!("Harmonic must be >= 1");
    }
    frequency * harmonic as f64
}

/// Calculate the difference between two frequencies in cents.
///
/// # Arguments
/// * `freq1` - First frequency
/// * `freq2` - Second frequency
///
/// # Returns
/// Difference in cents (100 cents = 1 semitone)
pub fn cents_difference(freq1: f64, freq2: f64) -> f64 {
    1200.0 * (freq2 / freq1).log2()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_schumann_harmonics() {
        assert_eq!(SCHUMANN_HARMONICS.len(), 5);
        assert_eq!(SCHUMANN_HARMONICS[0], SCHUMANN_FUNDAMENTAL);
    }

    #[test]
    fn test_material_frequency() {
        assert_eq!(MaterialFrequency::Quartz.frequency(), 32768.0);
        assert_eq!(MaterialFrequency::Gold.alpha_affinity(), 0.95);
    }

    #[test]
    fn test_octave_of() {
        assert!((octave_of(440.0, 1) - 880.0).abs() < 1e-10);
        assert!((octave_of(440.0, -1) - 220.0).abs() < 1e-10);
    }

    #[test]
    fn test_harmonic_of() {
        assert!((harmonic_of(100.0, 2) - 200.0).abs() < 1e-10);
        assert!((harmonic_of(100.0, 3) - 300.0).abs() < 1e-10);
    }

    #[test]
    fn test_cents_difference() {
        // Octave = 1200 cents
        assert!((cents_difference(440.0, 880.0) - 1200.0).abs() < 1e-10);
    }
}
