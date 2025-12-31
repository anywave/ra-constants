{-|
Module      : Ra.Constants.Frequencies
Description : Frequency constants - Schumann resonances, musical pitches, and material frequencies
Copyright   : (c) 2025 Anywave Creations
License     : MIT
-}

module Ra.Constants.Frequencies
  ( -- * Schumann Resonances
    schumannFundamental
  , schumann2nd
  , schumann3rd
  , schumann4th
  , schumann5th
  , schumannHarmonics
    -- * Musical Pitch Standards
  , a432
  , a440
    -- * Solfeggio Frequencies
  , solfeggioUt
  , solfeggioRe
  , solfeggioMi
  , solfeggioFa
  , solfeggioSol
  , solfeggioLa
  , solfeggioFrequencies
    -- * Material Frequencies
  , Material(..)
  , MaterialProperties(..)
  , materialProperties
  , materialFrequency
  , materialAlphaAffinity
  , materialConductivity
    -- * Functions
  , octaveOf
  , harmonicOf
  , centsDifference
  ) where

-- | Schumann resonance fundamental frequency (Hz)
schumannFundamental :: Double
schumannFundamental = 7.83

-- | Second Schumann harmonic (Hz)
schumann2nd :: Double
schumann2nd = 14.3

-- | Third Schumann harmonic (Hz)
schumann3rd :: Double
schumann3rd = 20.8

-- | Fourth Schumann harmonic (Hz)
schumann4th :: Double
schumann4th = 27.3

-- | Fifth Schumann harmonic (Hz)
schumann5th :: Double
schumann5th = 33.8

-- | All Schumann harmonics
schumannHarmonics :: [Double]
schumannHarmonics =
  [ schumannFundamental
  , schumann2nd
  , schumann3rd
  , schumann4th
  , schumann5th
  ]

-- | Concert pitch A at 432 Hz (natural/Verdi tuning)
a432 :: Double
a432 = 432.0

-- | Concert pitch A at 440 Hz (ISO 16 standard)
a440 :: Double
a440 = 440.0

-- | Ut (Do) - Liberation from fear and guilt
solfeggioUt :: Double
solfeggioUt = 396.0

-- | Re - Facilitating change, undoing situations
solfeggioRe :: Double
solfeggioRe = 417.0

-- | Mi - Transformation, miracles, DNA repair
solfeggioMi :: Double
solfeggioMi = 528.0

-- | Fa - Connecting relationships, harmony
solfeggioFa :: Double
solfeggioFa = 639.0

-- | Sol - Awakening intuition, expression
solfeggioSol :: Double
solfeggioSol = 741.0

-- | La - Returning to spiritual order
solfeggioLa :: Double
solfeggioLa = 852.0

-- | All Solfeggio frequencies
solfeggioFrequencies :: [Double]
solfeggioFrequencies =
  [ solfeggioUt
  , solfeggioRe
  , solfeggioMi
  , solfeggioFa
  , solfeggioSol
  , solfeggioLa
  ]

-- | Material types with resonance properties
data Material
  = Quartz
  | Gold
  | Silver
  | Copper
  | Iron
  | Obsidian
  | Granite
  | Limestone
  deriving (Show, Eq, Ord, Enum, Bounded)

-- | Properties of a resonant material
data MaterialProperties = MaterialProperties
  { mpFrequency     :: Double  -- ^ Base frequency in Hz
  , mpAlphaAffinity :: Double  -- ^ Coherence affinity (0-1)
  , mpConductivity  :: Double  -- ^ Electrical/energetic conductivity (0-1)
  } deriving (Show, Eq)

-- | Get the properties for a material
materialProperties :: Material -> MaterialProperties
materialProperties Quartz    = MaterialProperties 32768.0 0.9  0.3
materialProperties Gold      = MaterialProperties 24576.0 0.95 0.95
materialProperties Silver    = MaterialProperties 20480.0 0.85 0.9
materialProperties Copper    = MaterialProperties 16384.0 0.8  0.85
materialProperties Iron      = MaterialProperties 12288.0 0.6  0.5
materialProperties Obsidian  = MaterialProperties 8192.0  0.7  0.1
materialProperties Granite   = MaterialProperties 4096.0  0.5  0.05
materialProperties Limestone = MaterialProperties 2048.0  0.4  0.02

-- | Get the base resonance frequency in Hz
materialFrequency :: Material -> Double
materialFrequency = mpFrequency . materialProperties

-- | Get the alpha/coherence affinity (0-1)
materialAlphaAffinity :: Material -> Double
materialAlphaAffinity = mpAlphaAffinity . materialProperties

-- | Get the conductivity factor (0-1)
materialConductivity :: Material -> Double
materialConductivity = mpConductivity . materialProperties

-- | Calculate frequency shifted by octaves.
octaveOf :: Double -> Int -> Double
octaveOf frequency octaves = frequency * (2 ** fromIntegral octaves)

-- | Calculate the nth harmonic of a frequency.
-- Harmonic must be >= 1
harmonicOf :: Double -> Int -> Double
harmonicOf frequency harmonic
  | harmonic < 1 = error "Harmonic must be >= 1"
  | otherwise    = frequency * fromIntegral harmonic

-- | Calculate the difference between two frequencies in cents.
-- 100 cents = 1 semitone
centsDifference :: Double -> Double -> Double
centsDifference freq1 freq2 = 1200 * logBase 2 (freq2 / freq1)
