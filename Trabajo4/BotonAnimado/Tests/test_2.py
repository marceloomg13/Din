import unittest
from boton_animado import BotonAnimado
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget

class NamesTestCase(unittest.TestCase):
   def test_AddsizeHint(self):
       app = QApplication()
       window = QWidget()
       boton = BotonAnimado()
       self.assertEqual(boton.AddsizeHint(20,20),QSize(80,80))
       app.quit()
       window.close()
       
if __name__ == '__main__':
    unittest.main()
    