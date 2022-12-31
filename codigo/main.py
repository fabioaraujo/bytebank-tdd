from bytebank import Funcionario

lucas = Funcionario('Lucas Carvalho', '10/02/2000', 1000)

print(lucas)
print(lucas.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '10/02/2000', 1000)