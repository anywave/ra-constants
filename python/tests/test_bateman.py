"""
Tests for ra_constants.bateman: Wesley H. Bateman's Ra-system values as printed
in "The Rods of Amon Ra" and verified page by page by the lattice's TR node
(Aug-Sep 2026). These are the author's values, not physics claims.
"""

import math
import pathlib
import re
from fractions import Fraction

import pytest

import ra_constants
from ra_constants import bateman as b

SQRT2 = math.sqrt(2)


def test_red_pi_is_84823_over_27000_not_pi():
    # TR-291, TR-349
    assert Fraction(84823, 27000) == b.RED_PI_EXACT
    assert pytest.approx(84823 / 27000, abs=1e-15) == b.RED_PI
    assert abs(b.RED_PI - math.pi) > 5e-8
    assert round(math.pi * 27000) == 84823


def test_84823_family():
    # TR-291, TR-308, TR-309, TR-329: Red constants are 84823 over a smooth denominator.
    assert Fraction(84823, 80000) == b.HUNAB_EXACT
    assert Fraction(84823, 60000) == b.RED_SQRT2_EXACT
    assert Fraction(3 * 84823, 50000) == b.ANKH_EXACT
    assert Fraction(84823, 84375) == b.OMEGA_OVER_R_EXACT
    assert float(b.ANKH_EXACT) == 5.08938


def test_colour_ladder():
    # TR-291, TR-300, TR-304, TR-308
    assert pytest.approx(60000 * SQRT2 / 84823, abs=1e-15) == b.COLOUR_RATIO
    assert pytest.approx(1.000351482, abs=1e-9) == b.COLOUR_RATIO
    assert pytest.approx(20 / 9 * SQRT2, abs=1e-15) == b.GREEN_PI
    assert pytest.approx(3.143801406, abs=2e-9) == b.BLUE_PI
    assert pytest.approx(32 * SQRT2 / 45, abs=1e-15) == b.OMEGA
    assert pytest.approx(25 / 8, abs=1e-12) == b.GREEN_PI / b.OMEGA
    assert pytest.approx(256 / 81, abs=1e-12) == b.GREEN_PI * b.OMEGA
    assert pytest.approx(b.HUNAB * b.COLOUR_RATIO, abs=1e-14) == b.GREEN_HUNAB


def test_colour_convert_carries_the_degree():
    # TR-294, TR-301 (volume_1 p.0117): r for lengths, r^2 for areas, identity at d=0.
    assert b.colour_convert(1.0, "red", "green") == pytest.approx(b.COLOUR_RATIO, abs=1e-15)
    assert b.colour_convert(1.0, "red", "blue", degree=2) == pytest.approx(
        b.COLOUR_RATIO**4, abs=1e-14
    )
    assert b.colour_convert(1.0, "red", "green", degree=2) == pytest.approx(1.000703088, abs=1e-9)
    assert b.colour_convert(5.0, "green", "red", degree=0) == 5.0
    with pytest.raises(ValueError):
        b.colour_convert(1.0, "red", "violet")


def test_h_bar_and_729_family():
    # TR-304, TR-320, TR-322, TR-323, TR-331
    assert Fraction(135, 128) == b.H_BAR_EXACT
    assert pytest.approx(float(b.H_BAR_EXACT), abs=1e-14) == b.GREEN_HUNAB / b.OMEGA
    assert Fraction(1, 729) == b.FS_DELTA_EXACT
    assert Fraction(800, 729) == b.RA_RYDBERG_EXACT
    assert Fraction(91125, 100000) == 1 / b.RA_RYDBERG_EXACT
    assert Fraction(729, 2) == b.BALMER_EXACT


def test_phi_erratum():
    # FP-1399, TR-312, TR-316: supplement g00857_src03_p0002.
    assert b.PHI_WINDOWS == {
        "omega_major": 1.62,
        "red": 1.6286016,
        "green": 1.629174025,
        "blue": 1.629746650,
    }
    assert b.PHI_RED_WITHDRAWN == 1.619430799
    assert Fraction("1.62") * b.OMEGA_OVER_R_EXACT == Fraction("1.6286016")


def test_repitans():
    # TR-276: Repitans are exact n/27; period 3 when gcd(n,3)=1, period 1 when 3|n,
    # terminating at 27.
    assert b.repitan(23) == Fraction(23, 27)
    assert b.repitan(27) == 1
    with pytest.raises(ValueError):
        b.repitan(0)
    with pytest.raises(ValueError):
        b.repitan(28)


def test_rac_units():
    # TR-298: vol2b g00585_src09_p0038 (printed 418); each Rac is an arc of Red Pi.
    assert b.RAC_UNITS_OF_RED_PI["RAC 1"] == pytest.approx(81 / 400)
    assert b.RAC_UNITS_OF_RED_PI["RAC 4"] == pytest.approx(1 / 6)
    assert b.RAC_UNITS_OF_RED_PI["RAC 6"] == pytest.approx(0.09 * SQRT2)
    assert len(b.RAC_UNITS_OF_RED_PI) == 10
    assert b.RED_PI * b.RAC_UNITS_OF_RED_PI["RAC 1"] == pytest.approx(0.6361725, abs=1e-12)


def test_spectral_lines():
    # TR-280 s5/s7, TR-286
    assert Fraction(6561, 7) == b.LYMAN_M6_ANGSTROM_EXACT
    assert b.PASCHEN_M6_ANGSTROM == 10935
    # The page proves itself: Paschen/Lyman ratio printed on volume_1 p.0100 (x10 units).
    assert Fraction("1093.5") / (b.LYMAN_M6_ANGSTROM_EXACT / 10) == Fraction(35, 3)


def test_package_ankh_is_not_batemans_ankh():
    # The package-level ANKH is this package's name for phi**3 (4.236...).
    # Bateman's Ankh is 5.08938.
    assert pytest.approx(ra_constants.PHI**3) == ra_constants.ANKH
    assert b.ANKH == 5.08938
    assert "not Bateman's Ankh" in _phi_source()


def test_version_matches_pyproject():
    pyproject = pathlib.Path(__file__).resolve().parents[1] / "pyproject.toml"
    m = re.search(r'^version = "([^"]+)"', pyproject.read_text(encoding="utf-8"), re.M)
    assert m is not None
    assert ra_constants.__version__ == m.group(1)


def test_no_unsourced_face_angle():
    # TR-278 / TR-290: 51.851651 has no source in 863 pages.
    pkg = pathlib.Path(ra_constants.__file__).parent
    for path in pkg.glob("*.py"):
        assert "51.851651" not in path.read_text(encoding="utf-8"), path


def _phi_source() -> str:
    return pathlib.Path(ra_constants.phi.__file__).read_text(encoding="utf-8")
