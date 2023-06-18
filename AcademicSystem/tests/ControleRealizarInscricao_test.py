from AcademicSystem.controller.ControleRealizarInscricao import ControleRealizarInscricao
import pytest
from unittest import TestCase

class RegisterNewInstructor(TestCase):
    
    def test_filtrarOfertas(self):
        controleRealizarInscricao = ControleRealizarInscricao()
        self.assertEqual(controleRealizarInscricao.filtrarOfertas(), 15)
        
    def test_confirmarInscricao(self):
        controleRealizarInscricao = ControleRealizarInscricao()
        self.assertEqual(controleRealizarInscricao.confirmarInscricao(), 9)
        

