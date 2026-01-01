import { describe, it, expect } from 'vitest'
import { PHI, PHI_INVERSE, PHI_SQUARED, SCHUMANN_FUNDAMENTAL } from './index'

describe('Phi constants', () => {
  it('PHI should equal golden ratio', () => {
    expect(PHI).toBeCloseTo(1.618033988749895, 10)
  })

  it('PHI_INVERSE should be 1/PHI', () => {
    expect(PHI_INVERSE).toBeCloseTo(1 / PHI, 10)
  })

  it('PHI_SQUARED should be PHI^2', () => {
    expect(PHI_SQUARED).toBeCloseTo(PHI * PHI, 10)
  })

  it('PHI * PHI_INVERSE should equal 1', () => {
    expect(PHI * PHI_INVERSE).toBeCloseTo(1, 10)
  })
})

describe('Frequency constants', () => {
  it('SCHUMANN_FUNDAMENTAL should be 7.83 Hz', () => {
    expect(SCHUMANN_FUNDAMENTAL).toBe(7.83)
  })
})
