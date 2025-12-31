{-|
Module      : Ra.Constants
Description : Universal mathematical constants for harmonic resonance systems
Copyright   : (c) 2025 Anywave Creations
License     : MIT

Ra Constants provides portable mathematical constants for harmonic resonance
systems, including the golden ratio, Schumann frequencies, and coherence
thresholds.
-}

module Ra.Constants
  ( -- * Version
    version
    -- * Mathematical Constants
  , module Ra.Constants.Phi
    -- * Frequency Constants
  , module Ra.Constants.Frequencies
    -- * Coherence Thresholds
  , module Ra.Constants.Thresholds
  ) where

import Ra.Constants.Phi
import Ra.Constants.Frequencies
import Ra.Constants.Thresholds

-- | Library version
version :: String
version = "0.1.0"
