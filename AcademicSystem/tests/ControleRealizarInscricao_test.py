from AcademicSystem.controller.ControleRealizarInscricao import ControleRealizarInscricao
import pytest
from unittest import TestCase

class RegisterNewInstructor(TestCase):
    
    def test_filtrarOfertas(self):
        contreleInscricao = ControleRealizarInscricao()
        assert contreleInscricao.filtrarOfertas() == 15
        
    def test_confrimarInscricao(self):
        contreleInscricao = ControleRealizarInscricao()
        assert contreleInscricao.confrimarInscricao() == 9
        

