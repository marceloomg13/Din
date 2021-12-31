import unittest,pytest

from PySide6 import QtCore
from boton_animado import BotonAnimado
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget


@pytest.fixture
def app(qtbot):
    test_button = BotonAnimado()    
    qtbot.addWidget(test_button)
    return test_button


def test_boton(app,qtbot):
    qtbot.mouseClick(app, QtCore.Qt.LeftButton)
    assert app.text() == "pressed"