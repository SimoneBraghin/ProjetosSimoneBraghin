class JogoTruco:
    def init(self):
        self.cartas = [
            '4 de Paus', '5 de Paus', '6 de Paus', '7 de Paus', 'Q  de Paus', 'J de Paus', 'K de Paus', 'A de Paus',
            '4 de Ouro', '5 de Ouro', '6 de Ouro', '7 de Ouro', 'Q de Ouro', 'J de Ouro', 'K de Ouro', 'A de Ouro',
            '4 de Copas', '5 de Copas', '6 de Copas', '7 de Copas', 'Q de Copas', 'J de Copas', 'K de Copas', 'A de Copas',
            '4 de Espadas', '5 de Espadas', '6 de Espadas', '7 de Espadas', 'Q de Espadas', 'J de Espadas', 'K de Espadas', 'A de Espadas'
        ]
        random.shuffle(self.cartas)
        self.mao_jogador1 = []
        self.mao_jogador2 = []

    def distribuir_cartas(self):
        self.mao_jogador1 = self.cartas[:3]
        self.mao_jogador2 = self.cartas[3:6]

    def mostrar_maos(self):
        print(f"Jogador 1: {self.mao_jogador1}")
        print(f"Jogador 2: {self.mao_jogador2}")

    def jogar(self):
        self.distribuir_cartas()
        print("Início do jogo!")
        self.mostrar_maos()

        for rodada in range(3):
            carta_jogador1 = input("Jogador 1, escolha uma carta para jogar: ")
            carta_jogador2 = random.choice(self.mao_jogador2)

            print(f"Jogador 2 jogou: {carta_jogador2}")

            self.mao_jogador1.remove(carta_jogador1)
            self.mao_jogador2.remove(carta_jogador2)

            self.mostrar_maos()

        print("Fim do jogo!")

"""if name == "main":
    jogo = JogoTruco()
    jogo.jogar()"""