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
        data_nascimento_quebrada = self.__data_nascimento.split('/')
        ano_nascimento = data_nascimento_quebrada[-1] # -1 para pegar o último item da lista
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def calcular_bonus(self):
        valor = self.__salario * 0.1
        if(valor > 1000):
            valor = 0
        return valor
    
    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]

    def __eh_socio(self) -> bool:
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return (self.sobrenome() in sobrenomes)

    def decrescimo_salario(self):
        
        if self.__salario >= 100000 and self.__eh_socio():
            self.__salario = self.__salario * 0.9

    def __str__(self):
        return f'Funcionario ({self.__nome}, {self.__data_nascimento}, {self.__salario})'