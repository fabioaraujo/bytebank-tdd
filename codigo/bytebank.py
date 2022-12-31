from datetime import date

class Funcionario:
    
    def __init__(self, nome, data_nascimento, salario):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @property
    def salario(self):
        return self.__salario

    def idade(self):
        ano_atual = date.today().year
        return ano_atual - int(self.__data_nascimento)

    def calcular_bonus(self):
        valor = self.__salario * 0.1
        if(valor > 1000):
            valor = 0
        return valor

    def __str__(self):
        return f'Funcionario ({self.__nome}, {self.__data_nascimento}, {self.__salario})'