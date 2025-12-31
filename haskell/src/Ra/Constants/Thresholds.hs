{-|
Module      : Ra.Constants.Thresholds
Description : Coherence thresholds - Generic bands for coherence state classification
Copyright   : (c) 2025 Anywave Creations
License     : MIT
-}

module Ra.Constants.Thresholds
  ( -- * Threshold Constants
    highCoherence
  , mediumCoherence
  , lowCoherence
  , minimumCoherence
    -- * Coherence Bands
  , CoherenceBand(..)
  , CoherenceLevel(..)
  , coherenceBand
  , classifyCoherence
  , bandContains
    -- * Functions
  , normalizeCoherence
  , coherenceDelta
  , isCoherenceStable
  ) where

-- | High coherence threshold (85%)
highCoherence :: Double
highCoherence = 0.85

-- | Medium coherence threshold (60%)
mediumCoherence :: Double
mediumCoherence = 0.6

-- | Low coherence threshold (30%)
lowCoherence :: Double
lowCoherence = 0.3

-- | Minimum detectable coherence (10%)
minimumCoherence :: Double
minimumCoherence = 0.1

-- | Definition of a coherence band
data CoherenceBand = CoherenceBand
  { cbLower :: Double    -- ^ Lower bound (inclusive)
  , cbUpper :: Double    -- ^ Upper bound (exclusive, except for highest band)
  , cbName  :: String    -- ^ Human-readable name
  } deriving (Show, Eq)

-- | Coherence level classification
data CoherenceLevel
  = Peak
  | High
  | Medium
  | Low
  | Minimal
  deriving (Show, Eq, Ord, Enum, Bounded)

-- | Get the band definition for a coherence level
coherenceBand :: CoherenceLevel -> CoherenceBand
coherenceBand Peak    = CoherenceBand highCoherence 1.01 "peak"
coherenceBand High    = CoherenceBand mediumCoherence highCoherence "high"
coherenceBand Medium  = CoherenceBand lowCoherence mediumCoherence "medium"
coherenceBand Low     = CoherenceBand minimumCoherence lowCoherence "low"
coherenceBand Minimal = CoherenceBand 0.0 minimumCoherence "minimal"

-- | Check if a value falls within a band
bandContains :: CoherenceBand -> Double -> Bool
bandContains band value = cbLower band <= value && value < cbUpper band

-- | Classify a coherence value into a level.
-- Value must be between 0 and 1.
classifyCoherence :: Double -> CoherenceLevel
classifyCoherence value
  | value < 0 || value > 1 = error "Coherence must be between 0 and 1"
  | otherwise = case filter (flip bandContains value . coherenceBand) [Peak ..] of
      (level:_) -> level
      []        -> Peak  -- Handle edge case of exactly 1.0

-- | Normalize a value to the 0-1 coherence range.
normalizeCoherence :: Double -> Double -> Double -> Double
normalizeCoherence value minVal maxVal
  | maxVal <= minVal = error "maxVal must be greater than minVal"
  | otherwise = max 0.0 (min 1.0 normalized)
  where
    normalized = (value - minVal) / (maxVal - minVal)

-- | Calculate the change in coherence between two measurements.
-- Positive = increasing coherence
coherenceDelta :: Double -> Double -> Double
coherenceDelta current previous = current - previous

-- | Check if a series of coherence values is stable.
isCoherenceStable :: [Double] -> Double -> Bool
isCoherenceStable values threshold
  | length values < 2 = True
  | otherwise = stdDev <= threshold
  where
    n = fromIntegral (length values)
    mean = sum values / n
    variance = sum (map (\v -> (v - mean) ** 2) values) / n
    stdDev = sqrt variance
