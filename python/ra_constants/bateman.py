"""
Wesley H. Bateman's Ra-system values, as printed and verified.

Source: W. H. Bateman, "The Rods of Amon Ra" (1992-1997). Every value here was
checked against the printed page by the lattice's TR node in Aug-Sep 2026; the
comment on each names the lattice post (TR-###) and, where TR gave one, the
archive page id or printed folio.

These are the author's own units and ratios. They are not physics claims: where
he borrows a physics name (H-Bar, Rydberg, fine structure) the value is his and
differs from the physical constant. His spectral tables sit a constant ~545 ppm
from measured hydrogen lines because he used his own Rydberg; that offset is
authorial and must not be "corrected" toward reference data (TR-280, TR-283).

Most of his constants are exact rationals over one numerator,
84823 = round(pi x 27000) (TR-291), or sqrt(2) multiples of small rationals
(TR-300), so they are given here as exact `Fraction` values with float twins.

(c) 2025 Anywave Creations
MIT License
"""

from __future__ import annotations

import math
from fractions import Fraction

_SQRT2 = math.sqrt(2)

# ---------------------------------------------------------------------------
# The 84823 family (TR-291, TR-308, TR-309, TR-329)
# ---------------------------------------------------------------------------

RED_PI_EXACT = Fraction(84823, 27000)
"""Red Pi = 84823/27000 = 3.141592592... Not pi: pi rounded at a base-27 scale (TR-291, TR-349)."""
RED_PI: float = float(RED_PI_EXACT)

HUNAB_EXACT = Fraction(84823, 80000)
"""Hunab (Red) = 1.0602875 (TR-291; volume_1 p.0150; labelled HUNAB 247 times, FP-1399)."""
HUNAB: float = float(HUNAB_EXACT)

RED_SQRT2_EXACT = Fraction(84823, 60000)
"""Red sqrt2 = 1.41371666 (TR-329; supplement p.0002 prints 1.41371666)."""

ANKH_EXACT = Fraction(3 * 84823, 50000)
"""Ankh = 5.08938 = Red Pi x 1.62, the Ankh measuring wheel (volume_1 p.0168; TR-298, TR-329)."""
ANKH: float = float(ANKH_EXACT)

OMEGA_OVER_R_EXACT = Fraction(84823, 84375)
"""Omega / r = 1.005309630, the outer rung of the colour ladder (TR-308, TR-309, TR-312)."""

# ---------------------------------------------------------------------------
# Colour ladder (TR-291, TR-300, TR-301, TR-302, TR-304, TR-308, TR-312)
# ---------------------------------------------------------------------------

COLOUR_RATIO: float = 60000 * _SQRT2 / 84823
"""r = Green/Red = Blue/Green = 1.000351482 (TR-291, TR-300).

Printed "Red Rams x 1.000351482 = Green Rams" at vol2a g00215_src01_p0031 (TR-349).
"""

OMEGA: float = 32 * _SQRT2 / 45
"""Omega Ratio = 32 sqrt2 / 45 = 1.005662978 (TR-304; vol2a prologue, TR-302)."""

GREEN_PI: float = 20 / 9 * _SQRT2
"""Green Pi = (20/9) sqrt2 = 3.142696805.

Named GREEN PI at volume_1 p.0129, procedure 7-3 (TR-300, TR-301).
"""

BLUE_PI: float = GREEN_PI * COLOUR_RATIO
"""Blue Pi = Green Pi x r = 3.143801406 (TR-308; volume_1 p.0122, printed 114)."""

GREEN_HUNAB: float = 0.75 * _SQRT2
"""Green Hunab = (3/4) sqrt2 = Hunab x r exactly (TR-320, FP-1430, TR-327)."""

H_BAR_EXACT = Fraction(135, 128)
"""H-Bar = 1.0546875 = Green Hunab / Omega, the Omega Major window of the Hunab row.

vol2a g00194_src01_p0010, "OMEGA LEVELS: KEY NUMBERS" (TR-304); supplement p.0002 (TR-312).
Bateman's value, not the physical reduced Planck constant.
"""

_COLOUR_STEP: dict[str, int] = {"red": 0, "green": 1, "blue": 2}


def colour_convert(value: float, from_colour: str, to_colour: str, degree: int = 1) -> float:
    """Re-express a value from one colour window (red/green/blue) in another.

    The step between adjacent colours is r, applied once per length in play:
    degree 1 for a length, 2 for an area, 3 for a volume, 0 for no conversion.
    Printed rule: volume_1 p.0117 (printed 109), "Green is separated from Red and from
    Blue by the ratio 1.000703088" on squared quantities (TR-294, TR-301, TR-309).
    """
    try:
        steps = _COLOUR_STEP[to_colour.lower()] - _COLOUR_STEP[from_colour.lower()]
    except KeyError as exc:
        raise ValueError(f"colour must be red, green or blue, got {exc.args[0]!r}") from None
    return value * COLOUR_RATIO ** (steps * degree)


# ---------------------------------------------------------------------------
# Phi - the author's erratum (supplement g00857_src03_p0002)
# ---------------------------------------------------------------------------

PHI_WINDOWS: dict[str, float] = {
    "omega_major": 1.62,
    "red": 1.6286016,
    "green": 1.629174025,
    "blue": 1.629746650,
}
"""RA PHI VALUES as printed on Bateman's erratum sheet (FP-1399, TR-312, TR-316).

Red = 1.62 x 84823/84375 exactly. Volume 1 p.0027 and the vol2a p.0010 master table
call 1.62 the Green Phi; the erratum supersedes them (TR-312). The Omega Minor cell
is blank on the sheet. None of these is the golden ratio (1.618033989).
"""

PHI_RED_WITHDRAWN: float = 1.619430799
"""Red Phi used on every Volume 2 and 3 data form, declared erroneous by the author (FP-1399)."""

# ---------------------------------------------------------------------------
# The 729 family (TR-281, TR-288, TR-320, TR-322, TR-323, TR-331)
# ---------------------------------------------------------------------------

FS_DELTA_EXACT = Fraction(1, 729)
"""Bateman's "fine structure" unit f.s.Delta = 1/729 = Repitan(1)^2 (volume_1 p.0105; TR-323).

1/729 of a degree on volume_1 folio 165 (TR-331). Not the physical fine-structure constant
(0.0072973526). Printed 10x small in the Supplement (TR-281).
"""

RA_RYDBERG_EXACT = Fraction(800, 729)
"""Ra Rydberg = 800/729 = 1.09739369; "Green Rydberg Constant" on volume_1 p.0126 (TR-320).

Reciprocal .91125 = 729/800 on volume_1 p.0130 (TR-322). Not CODATA R_inf.
"""

BALMER_EXACT = Fraction(729, 2)
"""Balmer constant = 364.5, labelled in the cell (TR-288); = pyramid base / RAC 2 (TR-331)."""

LYMAN_M6_ANGSTROM_EXACT = Fraction(6561, 7)
"""Lyman M6 = 937.2857142857 A (TR-280 s7, TR-286).

Volume_1 p.0100 prints 93.72857142 (x10 units); the Supplement's 932.7857142 is a
transposition. The page proves itself: 1093.5 / 93.72857142 = 35/3.
"""

PASCHEN_M6_ANGSTROM: int = 10935
"""Paschen M6 = 10935 A (Supplement; TR-280 s5)."""

# ---------------------------------------------------------------------------
# Repitans and Rac units
# ---------------------------------------------------------------------------


def repitan(n: int) -> Fraction:
    """Repitan n = n/27, exact, for n in 1..27 (TR-276).

    The decimal repeats with period 3 when gcd(n, 3) = 1, period 1 when 3 divides n,
    and terminates at n = 27.
    """
    if not isinstance(n, int) or not 1 <= n <= 27:
        raise ValueError(f"Repitan index must be an int in [1, 27], got {n!r}")
    return Fraction(n, 27)


RAC_UNITS_OF_RED_PI: dict[str, float] = {
    "RAC 1": 81 / 400,
    "RAC 2": 1 / 5,
    "RAC 3": 729 / 4000,
    "RAC 4": 1 / 6,
    "RAC 5": 729 / 5000,
    "RAC 6": 0.09 * _SQRT2,
    "RAC 7": _SQRT2 / 8.64,
    "MIR Rac": 2 / 9,
    "Block Rac 1": 27 / 125,
    "Block Rac 2": 8 / 45,
}
"""The ten Rac units as fractions of Red Pi (TR-298; vol2b g00585_src09_p0038, printed 418).

Each Rac is an arc of Red Pi - a turn of a measuring wheel - not a free-standing length.
Its degree measure depends on the circle: on the Ankh wheel (volume_1 p.0168) RAC 1 is
a 45-degree turn. Bateman's "51.851 (51 23/27) Red Rac 3 units" (vol2a g00343_src02_p0035)
is a count of these arcs, not a face angle (TR-278, TR-290).
"""
