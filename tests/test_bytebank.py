from codigo.bytebank import Funcionario

class TestClass:
    
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        funcionario_teste = Funcionario('Teste', '10/02/2000', 1000)
        assert funcionario_teste.idade() == 23