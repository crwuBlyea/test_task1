import figures
import pytest

circle = figures.Circle()
triag = figures.Triangle()
def test_circle_init_val_check():
    with pytest.raises(ValueError, match="Radius can't be negative or zero"):
        c = figures.Circle(-1)
def test_circle_edge_cases():
    with pytest.raises(ValueError, match="Radius can't be negative or zero"):
        circle.radius = -2
def test_triangle_edge_cases():
    with pytest.raises(ValueError, match="Side1 cannot be negative or zero"):
        triag.side1 = -10000
    with pytest.raises(ValueError, match="Side2 cannot be negative or zero"):
        triag.side2 = 0
    with pytest.raises(ValueError, match="Side3 cannot be negative or zero"):
        triag.side3 = -10
def test_triangle_is_exist():
    triag.side1 = 2
    with pytest.raises(ValueError, match="Triangle with these sides does not exist"):
        triag.calculate_area()
    with pytest.raises(ValueError, match="Triangle with these sides does not exist"):
        triag.is_right_angled()