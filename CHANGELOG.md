# Changelog

All notable changes to this project are recorded here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.2] - 2026-10-10

Version 0.1.1 was reserved for the 2026-10 public cleanup (PR #1), which merged without a version bump. Neither is
on PyPI yet; PyPI has 0.1.0.

### Added

- Python: `ra_constants.bateman`, Wesley H. Bateman's Ra-system values from *The Rods of Amon Ra* (1992-1997), as
  printed and verified page by page by the lattice's TR node in Aug-Sep 2026. Exact `Fraction` forms with float
  twins. Each value cites the lattice post and, where given, the archive page or printed folio:
  - Red Pi = 84823/27000, with 84823 = round(π × 27000); not π (TR-291, TR-349).
  - The 84823 family: Hunab 84823/80000 (volume_1 p.0150), Red √2 84823/60000, Ankh 3 × 84823/50000, Omega/r
    84823/84375 (TR-291, TR-308, TR-309, TR-329).
  - Colour ratio r = 60000√2/84823 (printed 1.000351482, vol2a g00215_src01_p0031), Omega = 32√2/45, Green Pi =
    (20/9)√2, Blue Pi, Green Hunab = (3/4)√2, H-Bar = 135/128 (TR-291, TR-300, TR-304, TR-308, TR-320; vol2a
    g00194_src01_p0010).
  - `colour_convert(value, from_colour, to_colour, degree=1)`: r per step, raised to the number of lengths in play
    (r² for areas; volume_1 p.0117, printed 109; TR-294, TR-301).
  - Phi windows from the author's erratum on supplement g00857_src03_p0002 (Omega Major 1.62, Red 1.6286016, Green
    1.629174025, Blue 1.629746650) and the withdrawn Red Phi 1.619430799 (FP-1399, TR-312, TR-316).
  - The 729 family: f.s.Δ = 1/729 (Bateman's unit, not the physical fine-structure constant; TR-323, TR-331), Ra
    Rydberg = 800/729 (volume_1 p.0126; TR-320, TR-322), Balmer = 729/2 (TR-288).
  - Lyman M6 = 6561/7 Å (volume_1 p.0100; the Supplement's 932.7857142 is a transposition; TR-280 §7, TR-286) and
    Paschen M6 = 10935 Å (TR-280 §5).
  - `repitan(n)` = n/27 exactly (TR-276) and the ten Rac units as fractions of Red Pi (vol2b g00585_src09_p0038,
    printed 418; TR-298).
- Tests for every value above (`python/tests/test_bateman.py`), including a guard that the unsourced "51.851651°
  face angle" never enters the package: that number appears nowhere in the 863 pages, and Bateman's `51.851
  (51 23/27)` on vol2a g00343_src02_p0035 is a count of Red Rac 3 units, not an angle (TR-278, TR-290).
- README: a Bateman section with the scope note.

### Fixed

- `__version__` said 0.2.0 while the package metadata said 0.1.0; both now read 0.1.2, and a test keeps them equal.
- Docstrings: the package-level `ANKH` (φ³ ≈ 4.236) and `GREEN_PHI` (φ ≈ 1.618) are this package's names for powers
  of φ. They now say they are not Bateman's Ankh (5.08938) or his 1.62. Values unchanged.

### Not changed, on purpose

- Bateman's spectral values are not normalised toward reference wavelengths. The constant ~545 ppm offset from
  measured hydrogen lines comes from his own Rydberg and is authorial (TR-280 §7.3, TR-283, TR-349).
- The TypeScript, Rust and Haskell bindings do not yet carry the `bateman` values.
