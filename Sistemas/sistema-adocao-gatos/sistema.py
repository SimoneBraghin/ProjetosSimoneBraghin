# Sistema de adoção de gatinhos :)

from abc import ABC, abstractclassmethod
 
class Animal(ABC): 
    def __init__(self, nome, idade, dataNascimento, cor):
        # serve para indicar os desenvolvedores que
        # os atributos podem ou não serem utilizados fora da classe:
            # self._xxxx (1 underline) = privado
            # self.__xxxx (2 underlines) = totalmente privado
            # self.xxxx (sem underline) = público
        self.__nome = nome
        self.__idade = idade
        self.__dataNascimento = dataNascimento
        self.__cor = cor
        # self.__vacinado = True
        # self.__adotado = False
        # tem doenças? 

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade
            
    def get_dataNascimento(self):
        return self.__dataNascimento
            
    def get_cor(self):
        return self.__cor
    
    @abstractclassmethod
    def fazer_som(self): # Herança Múltipla: método abstrato que deve ser implementado nas subclasses
        pass
    

# Herança Simples: é quando pegamos as características da mesma classe
    
class Gato(Animal):
    def __init__(self, nome, idade, dataNascimento, cor, raca):
        super().__init__(nome, idade, dataNascimento, cor)
        self.__raca = raca

    def get_raca(self):
        return self.__raca

    def fazer_som(self):
        return "Miau"

# gato1 = Animal('Zumbi', 5, "03-10-2016", 'Preta', 'SRD') # animal criado
# gato2 = Animal('Ibrik', 5, "03-09-2019", 'Amarela', 'SRD')
# gato3 = Animal('Éclair', 2, "03-03-2022", 'Tricolor', 'SRD')
# gato4 = Gato('Éclair', 2, "03-03-2022", 'Preta', 'SRD')

#print(gato4.get_raca()) 


# Herança Múltipla - é quando pegamos as características de diferentes classes e instanciamos ela em terceira classe

class Adotante:
    def __init__(self, nome):
        self.nome = nome


class AdocaoGatinho:
    def __init__(self, animal, adotante):
        self.animal = animal
        self.adotante = adotante


#animal01 = Animal("Maker", 2, "branco")
#adotante01 = Adotante("Isadora")

# Criar uma instância de adoção
# adocao01 = AdocaoGatinho(Animal("Maker", 2, "branco"), Adotante("Isadora"))


# print("Nome do gatinho:", adocao01.animal.get_nome())
# print("Idade do gatinho adotado:", adocao01.animal.get_idade())
# print("Nome do adotante:", adocao01.adotante.nome)


# gatinho1 = Animal("Bolinha", 2, "branco") # primeiro animal criado
# gatinho2 = Animal("Python", 30, "Verde")
# gatinho3 = Gato("Frajola", 3, "Preto e Branco", "Vira-lata")
# print(gatinho2.get_nome())
# print(gatinho2.get_cor())
# print(gatinho3.get_raca())



# Classe Abstrata: são classes que definem os métodos 
# (características e comportamentos) que as outras classes herdarão (comportamentos genéricos)


@abstractclassmethod
def fazer_som(self): # método abstrato que deve ser implementado nas subclasses
    pass