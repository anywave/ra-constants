{-# LANGUAGE OverloadedStrings #-}

module Main (main) where

import Test.Hspec
import Ra.Constants
import Ra.Constants.Phi
import Ra.Constants.Frequencies
import Ra.Constants.Thresholds

main :: IO ()
main = hspec $ do
  describe "Phi constants" $ do
    it "phi * phiInverse = 1" $ do
      abs (phi * phiInverse - 1.0) `shouldSatisfy` (< 1e-10)

    it "phiSquared = phi + 1" $ do
      abs (phiSquared - phi - 1.0) `shouldSatisfy` (< 1e-10)

    it "phiPower 0 = 1" $ do
      phiPower 0 `shouldBe` 1.0

    it "phiPower 1 = phi" $ do
      phiPower 1 `shouldBe` phi

    it "fibonacciRatio converges to phi" $ do
      abs (fibonacciRatio 20 - phi) `shouldSatisfy` (< 1e-6)

  describe "Frequency constants" $ do
    it "schumannFundamental = 7.83" $ do
      schumannFundamental `shouldBe` 7.83

    it "a432 = 432.0" $ do
      a432 `shouldBe` 432.0

    it "octaveOf doubles frequency" $ do
      octaveOf 440.0 1 `shouldBe` 880.0

    it "harmonicOf multiplies frequency" $ do
      harmonicOf 100.0 3 `shouldBe` 300.0

    it "materialFrequency Quartz = 32768" $ do
      materialFrequency Quartz `shouldBe` 32768.0

  describe "Threshold constants" $ do
    it "highCoherence = 0.85" $ do
      highCoherence `shouldBe` 0.85

    it "classifyCoherence 0.9 = Peak" $ do
      classifyCoherence 0.9 `shouldBe` Peak

    it "classifyCoherence 0.7 = High" $ do
      classifyCoherence 0.7 `shouldBe` High

    it "normalizeCoherence works correctly" $ do
      abs (normalizeCoherence 50.0 0.0 100.0 - 0.5) `shouldSatisfy` (< 1e-10)

    it "isCoherenceStable detects stable values" $ do
      isCoherenceStable [0.5, 0.51, 0.49, 0.5] 0.05 `shouldBe` True

  describe "Version" $ do
    it "version is 0.1.0" $ do
      version `shouldBe` "0.1.0"
