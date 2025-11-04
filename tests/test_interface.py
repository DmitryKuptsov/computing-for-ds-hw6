import pytest
from math import pi, isclose
from hw5 import Triangle, Rectangle, Circle, PlaneFigure


# Triangle
def test_triangle_init_and_attrs():
    t = Triangle(3, 4, 5, 2)
    assert (t.base, t.c1, t.c2, t.h) == (3, 4, 5, 2)

def test_triangle_perimeter():
    t = Triangle(3, 4, 5, 2)
    assert t.compute_perimeter() == 12

def test_triangle_surface():
    t = Triangle(10, 6, 8, 4)
    assert t.compute_surface() == 0.5 * 10 * 4

def test_triangle_zero_height():
    t = Triangle(3, 4, 5, 0)
    assert t.compute_surface() == 0.0


# Rectangle
def test_rectangle_init_and_attrs():
    r = Rectangle(4, 6)
    assert (r.a, r.b) == (4, 6)

def test_rectangle_perimeter():
    r = Rectangle(2, 3)
    assert r.compute_perimeter() == 10

def test_rectangle_surface():
    r = Rectangle(2, 3)
    assert r.compute_surface() == 6

def test_rectangle_zero_side():
    r = Rectangle(0, 5)
    assert r.compute_surface() == 0
    assert r.compute_perimeter() == 10 


# Circle
def test_circle_init_and_attr():
    c = Circle(5)
    assert c.radius == 5

def test_circle_perimeter():
    c = Circle(3)
    assert isclose(c.compute_perimeter(), 2 * pi * 3, rel_tol=1e-9)

def test_circle_surface():
    c = Circle(3)
    assert isclose(c.compute_surface(), pi * 3**2, rel_tol=1e-9)

def test_circle_zero_radius():
    c = Circle(0)
    assert c.compute_surface() == 0
    assert c.compute_perimeter() == 0

def test_circle_both_methods_run():
    c = Circle(3)
    p = c.compute_perimeter()
    s = c.compute_surface()
    assert isclose(p, 2 * pi * 3, rel_tol=1e-9)
    assert isclose(s, pi * 3**2, rel_tol=1e-9)

# Abstract class
def test_planefigure_is_abstract():
    with pytest.raises(TypeError):
        PlaneFigure()


# Overall
def test_all_figures_return_numbers():
    t = Triangle(3, 4, 5, 2)
    r = Rectangle(2, 3)
    c = Circle(2)
    for f in (t, r, c):
        assert isinstance(f.compute_perimeter(), (int, float))
        assert isinstance(f.compute_surface(), (int, float))

class DummyFigure(PlaneFigure):
    def compute_perimeter(self): pass
    def compute_surface(self): pass

def test_planefigure_methods_executed():
    d = DummyFigure()
    d.compute_perimeter()
    d.compute_surface()
