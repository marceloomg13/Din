import unittest
from boton_animado import BotonAnimado
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget

class NamesTestCase(unittest.TestCase):

   def test_sizeHint(self):
       app = QApplication()
       window = QWidget()
       boton = BotonAnimado()
       self.assertEqual(boton.sizeHint(),QSize(60,60))
       app.quit()
       window.close()

if __name__ == '__main__':
    unittest.main()
    