
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import (
    QPropertyAnimation, QRandomGenerator, QSequentialAnimationGroup, QPoint, QSize, Property)
import random
class BotonAnimado(QPushButton):
    def __init__(self):
        super().__init__()
        self._duracion=150
        self.colors = [
            "background-color:#63edff;border-radius:10px;",
            "background-color:#cf3cbd;border-radius:10px;",
            "background-color:#e81c1c;border-radius:10px;",
            "background-color:#26e81c;border-radius:10px;",
            "background-color:#f7df00;border-radius:10px;",
            "background-color:#00ff8c;border-radius:10px;",
        ]       
        self.setBaseSize(self.sizeHint())
        self.setMaximumSize(self.AddsizeHint(5,5)) 

        self.clicked.connect(self.pulsado)

        self.setStyleSheet("background-color:#99ecf7;border-radius:10px;")

        self.anim = QPropertyAnimation(self, b"size")
        self.anim.setEndValue(self.AddsizeHint(5,5))
        self.anim.setDuration(self._duracion)

        self.anim1 = QPropertyAnimation(self, b"size")
        self.anim1.setEndValue(self.sizeHint())
        self.anim1.setDuration(self._duracion)

        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim1)
        
        self.color=random.choice(self.colors)
        self.oldcolor=self.color

    def pulsado(self):
        self.color=random.choice(self.colors)
        while(self.oldcolor==self.color):
            self.color=random.choice(self.colors)
        if self.anim_group.state() != QPropertyAnimation.Running:
            self.setStyleSheet(self.color)
        self.anim_group.start()
        self.oldcolor=self.color
        self.setText("pressed")
    
    def sizeHint(self):
        return QSize(60, 60)

    def AddsizeHint(self,a,b):
        return QSize(60+a, 60+b)
    
    @Property(int)
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, duracion):
        self._duracion = duracion