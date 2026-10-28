import pytest
from app import convertir


def test_celsius_a_fahrenheit():
    assert convertir(0, "C", "F") == 32


def test_celsius_a_kelvin():
    assert convertir(0, "C", "K") == pytest.approx(273.15)


def test_fahrenheit_a_celsius():
    assert convertir(32, "F", "C") == pytest.approx(0)


def test_kelvin_a_celsius():
    assert convertir(273.15, "K", "C") == pytest.approx(0)


def test_escala_invalida():
    with pytest.raises(ValueError):
        convertir(20, "X", "C")


def test_temperatura_inferior_al_cero_absoluto():
    with pytest.raises(ValueError):
        convertir(-300, "C", "K")
