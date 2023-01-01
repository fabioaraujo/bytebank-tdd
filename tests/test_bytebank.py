from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        funcionario_teste = Funcionario('Teste', '10/02/2000', 1000)
        assert funcionario_teste.idade() == 23
    
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado #Then
    
    def test_quando_diretor_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 #given
        esperado = 90000

        funcionario_teste = Funcionario('Teste Bragança', '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # when
        resultado = funcionario_teste.salario

        assert resultado == esperado

    def test_quando_funcionario_salario_recebe_100000_deve_retornar_100000(self):
        entrada_salario = 100000 #given
        esperado = 100000

        funcionario_teste = Funcionario('Teste Funcionario', '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # when
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # given
        esperado = 100

        funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus() # when

        assert resultado == esperado  # then
    
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000  # given

            funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()  # when

            assert resultado  # then