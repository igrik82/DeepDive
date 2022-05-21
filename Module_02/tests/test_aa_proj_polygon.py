"""
Test poligon class
"""

import aa_proj_polygon as proj
import pytest


@pytest.fixture
def polygon_init():
    """Ficture"""
    return proj.Polygon


def test_polygon_init(polygon_init):
    """Testing init method"""
    polygon = polygon_init(4, 5)
    assert polygon.edges == 4
    assert polygon.circumradius == 5


exeption_value = [(1, 2), ("a", 2), (3, "b"), ("a", "b")]


@pytest.mark.parametrize("edges, circumradius", exeption_value)
def test_poligon_exeption(edges, circumradius, polygon_init):
    """Test ValueError exeptions"""
    with pytest.raises(
        ValueError, match=r"At least 3 edges must be provided || Only integer allowed!"
    ):
        polygon_init(edges, circumradius)


def test_apothem(polygon_init):
    """Test apothem"""
    polygon = polygon_init(4, 5)
    assert polygon.apothem == 3.54


def test_length(polygon_init):
    """Test length"""
    polygon = polygon_init(3, 5)
    assert polygon.length == 8.66


def test_area(polygon_init):
    """Test area"""
    polygon = polygon_init(3, 5)
    assert polygon.area == 32.48


def test_perimetr(polygon_init):
    """Test perimetr"""
    polygon = polygon_init(3, 5)
    assert polygon.perimeter == 25.98


def test_interior_angle(polygon_init):
    """Test interior angle"""
    polygon = polygon_init(3, 5)
    assert polygon.interior_angle == 60


def test_equality(polygon_init):
    """Test equality"""
    polygon1 = polygon_init(5, 5)
    polygon2 = polygon_init(5, 5)
    polygon3 = polygon_init(4, 4)

    assert polygon1 == polygon2
    assert polygon1 != polygon3


def test_compare(polygon_init):
    """Test compare"""
    polygon1 = polygon_init(5, 5)
    polygon2 = polygon_init(6, 5)
    polygon3 = polygon_init(7, 4)

    assert polygon2 > polygon1
    assert polygon3 > polygon2
    assert polygon2 < polygon3


def test_polygons_init(polygon_init):
    """Testing init method for Poligons class"""
    with pytest.raises(
        ValueError, match=r"Must be at least 3"
    ):
        proj.Polygons(1,5)