//! Coherence thresholds - Generic bands for coherence state classification.
//!
//! (c) 2025 Anywave Creations
//! MIT License

/// High coherence threshold (85%)
pub const HIGH_COHERENCE: f64 = 0.85;

/// Medium coherence threshold (60%)
pub const MEDIUM_COHERENCE: f64 = 0.6;

/// Low coherence threshold (30%)
pub const LOW_COHERENCE: f64 = 0.3;

/// Minimum detectable coherence (10%)
pub const MINIMUM_COHERENCE: f64 = 0.1;

/// Definition of a coherence band
#[derive(Debug, Clone, Copy, PartialEq)]
pub struct CoherenceBand {
    /// Lower bound (inclusive)
    pub lower: f64,
    /// Upper bound (exclusive, except for highest band)
    pub upper: f64,
    /// Human-readable name
    pub name: &'static str,
}

impl CoherenceBand {
    /// Create a new coherence band
    pub const fn new(lower: f64, upper: f64, name: &'static str) -> Self {
        Self { lower, upper, name }
    }

    /// Check if a value falls within this band
    pub fn contains(&self, value: f64) -> bool {
        self.lower <= value && value < self.upper
    }
}

/// Coherence level classification
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum CoherenceLevel {
    Peak,
    High,
    Medium,
    Low,
    Minimal,
}

impl CoherenceLevel {
    /// Get the band definition for this level
    pub const fn band(&self) -> CoherenceBand {
        match self {
            Self::Peak => CoherenceBand::new(HIGH_COHERENCE, 1.01, "peak"),
            Self::High => CoherenceBand::new(MEDIUM_COHERENCE, HIGH_COHERENCE, "high"),
            Self::Medium => CoherenceBand::new(LOW_COHERENCE, MEDIUM_COHERENCE, "medium"),
            Self::Low => CoherenceBand::new(MINIMUM_COHERENCE, LOW_COHERENCE, "low"),
            Self::Minimal => CoherenceBand::new(0.0, MINIMUM_COHERENCE, "minimal"),
        }
    }

    /// Get lower bound of this band
    pub const fn lower(&self) -> f64 {
        self.band().lower
    }

    /// Get upper bound of this band
    pub const fn upper(&self) -> f64 {
        self.band().upper
    }

    /// Classify a coherence value into a level
    ///
    /// # Arguments
    /// * `value` - Coherence value (0-1)
    ///
    /// # Returns
    /// The appropriate CoherenceLevel
    ///
    /// # Panics
    /// Panics if value is not between 0 and 1
    pub fn classify(value: f64) -> Self {
        if !(0.0..=1.0).contains(&value) {
            panic!("Coherence must be between 0 and 1");
        }

        let levels = [
            Self::Peak,
            Self::High,
            Self::Medium,
            Self::Low,
            Self::Minimal,
        ];

        for level in levels {
            let band = level.band();
            if band.lower <= value && value < band.upper {
                return level;
            }
        }

        // Handle edge case of exactly 1.0
        Self::Peak
    }

    /// Check if a value falls within this level's band
    pub fn contains(&self, value: f64) -> bool {
        self.band().contains(value)
    }
}

/// Normalize a value to the 0-1 coherence range.
///
/// # Arguments
/// * `value` - Value to normalize
/// * `min_val` - Minimum of input range
/// * `max_val` - Maximum of input range
///
/// # Returns
/// Normalized value between 0 and 1
///
/// # Panics
/// Panics if max_val <= min_val
pub fn normalize_coherence(value: f64, min_val: f64, max_val: f64) -> f64 {
    if max_val <= min_val {
        panic!("max_val must be greater than min_val");
    }

    let normalized = (value - min_val) / (max_val - min_val);
    normalized.clamp(0.0, 1.0)
}

/// Calculate the change in coherence between two measurements.
///
/// # Arguments
/// * `current` - Current coherence value
/// * `previous` - Previous coherence value
///
/// # Returns
/// Delta (positive = increasing coherence)
pub fn coherence_delta(current: f64, previous: f64) -> f64 {
    current - previous
}

/// Check if a series of coherence values is stable.
///
/// # Arguments
/// * `values` - Slice of coherence measurements
/// * `threshold` - Maximum allowed standard deviation
///
/// # Returns
/// True if coherence is stable
pub fn is_coherence_stable(values: &[f64], threshold: f64) -> bool {
    if values.len() < 2 {
        return true;
    }

    let mean = values.iter().sum::<f64>() / values.len() as f64;
    let variance = values.iter().map(|v| (v - mean).powi(2)).sum::<f64>() / values.len() as f64;
    let std_dev = variance.sqrt();

    std_dev <= threshold
}

/// Check if a series of coherence values is stable with default threshold of 0.05.
pub fn is_coherence_stable_default(values: &[f64]) -> bool {
    is_coherence_stable(values, 0.05)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_coherence_level_classify() {
        assert_eq!(CoherenceLevel::classify(0.9), CoherenceLevel::Peak);
        assert_eq!(CoherenceLevel::classify(0.7), CoherenceLevel::High);
        assert_eq!(CoherenceLevel::classify(0.4), CoherenceLevel::Medium);
        assert_eq!(CoherenceLevel::classify(0.2), CoherenceLevel::Low);
        assert_eq!(CoherenceLevel::classify(0.05), CoherenceLevel::Minimal);
    }

    #[test]
    fn test_normalize_coherence() {
        assert!((normalize_coherence(50.0, 0.0, 100.0) - 0.5).abs() < 1e-10);
        assert!((normalize_coherence(-10.0, 0.0, 100.0) - 0.0).abs() < 1e-10);
        assert!((normalize_coherence(150.0, 0.0, 100.0) - 1.0).abs() < 1e-10);
    }

    #[test]
    fn test_is_coherence_stable() {
        assert!(is_coherence_stable_default(&[0.5, 0.51, 0.49, 0.5]));
        assert!(!is_coherence_stable_default(&[0.1, 0.9, 0.1, 0.9]));
    }
}
