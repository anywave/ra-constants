//! Ra Constants - Universal mathematical constants for harmonic resonance systems.
//!
//! (c) 2025 Anywave Creations
//! MIT License

pub mod frequencies;
pub mod phi;
pub mod thresholds;

// Re-export commonly used items at crate root
pub use frequencies::{
    cents_difference, harmonic_of, octave_of, MaterialFrequency, MaterialProperties,
    A432, A440, SCHUMANN_2ND, SCHUMANN_3RD, SCHUMANN_4TH, SCHUMANN_5TH,
    SCHUMANN_FUNDAMENTAL, SCHUMANN_HARMONICS, SOLFEGGIO_FA, SOLFEGGIO_FREQUENCIES,
    SOLFEGGIO_LA, SOLFEGGIO_MI, SOLFEGGIO_RE, SOLFEGGIO_SOL, SOLFEGGIO_UT,
};

pub use phi::{
    fibonacci_ratio, is_phi_ratio, is_phi_ratio_default, phi_power, E, PHI, PHI_INVERSE,
    PHI_SQUARED, PI, SQRT_2, SQRT_3, SQRT_5, TAU,
};

pub use thresholds::{
    coherence_delta, is_coherence_stable, is_coherence_stable_default, normalize_coherence,
    CoherenceBand, CoherenceLevel, HIGH_COHERENCE, LOW_COHERENCE, MEDIUM_COHERENCE,
    MINIMUM_COHERENCE,
};

/// Library version
pub const VERSION: &str = "0.1.0";
