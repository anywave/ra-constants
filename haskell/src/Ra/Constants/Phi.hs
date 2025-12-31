{-|
Module      : Ra.Constants.Phi
Description : Mathematical constants - phi, roots, and transcendentals
Copyright   : (c) 2025 Anywave Creations
License     : MIT
-}

module Ra.Constants.Phi
  ( -- * Golden Ratio Constants
    phi
  , phiInverse
  , phiSquared
    -- * Square Roots
  , sqrt2
  , sqrt3
  , sqrt5
    -- * Transcendental Constants
  , piVal
  , tau
  , euler
    -- * Functions
  , phiPower
  , fibonacciRatio
  , isPhiRatio
  ) where

-- | The golden ratio (φ) = (1 + √5) / 2
phi :: Double
phi = 1.618033988749895

-- | Inverse of golden ratio (1/φ) = φ - 1
phiInverse :: Double
phiInverse = 0.6180339887498949

-- | Phi squared (φ²) = φ + 1
phiSquared :: Double
phiSquared = 2.618033988749895

-- | Square root of 2
sqrt2 :: Double
sqrt2 = 1.4142135623730951

-- | Square root of 3
sqrt3 :: Double
sqrt3 = 1.7320508075688772

-- | Square root of 5
sqrt5 :: Double
sqrt5 = 2.23606797749979

-- | Pi (π)
piVal :: Double
piVal = 3.141592653589793

-- | Tau (τ) = 2π
tau :: Double
tau = 6.283185307179586

-- | Euler's number (e)
euler :: Double
euler = 2.718281828459045

-- | Calculate φ^n using the recurrence relation.
phiPower :: Int -> Double
phiPower 0 = 1.0
phiPower 1 = phi
phiPower (-1) = phiInverse
phiPower n
  | n > 0     = phi ** fromIntegral n
  | otherwise = phiInverse ** fromIntegral (negate n)

-- | Calculate the ratio F(n+1)/F(n) which approaches φ.
-- n must be >= 1
fibonacciRatio :: Int -> Double
fibonacciRatio n
  | n < 1     = error "n must be >= 1"
  | otherwise = fromIntegral curr / fromIntegral prev
  where
    (prev, curr) = go n (1, 1)
    go 1 pair = pair
    go k (a, b) = go (k - 1) (b, a + b)

-- | Check if two values are in golden ratio.
isPhiRatio :: Double -> Double -> Double -> Bool
isPhiRatio a b tolerance
  | a <= 0 || b <= 0 = False
  | otherwise = abs (ratio - phi) < tolerance
  where
    ratio = max a b / min a b
