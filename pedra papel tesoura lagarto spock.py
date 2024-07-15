import random

class Jogada:
    def __init__(self):
        self.opcoes = ["pedra", "papel", "tesoura", "lagarto", "spock"]

    def get_opcao(self, escolha):
        if escolha in self.opcoes:
            return escolha
        else:
            return None

    def get_computador_opcao(self):
        return random.choice(self.opcoes)

    def determinar_vencedor(self, jogador, computador):
        if jogador == computador:
            return "Empate!"
        regras = {
            "pedra": ["tesoura", "lagarto"],
            "papel": ["pedra", "spock"],
            "tesoura": ["papel", "lagarto"],
            "lagarto": ["spock", "papel"],
            "spock": ["tesoura", "pedra"]
        }
        if computador in regras[jogador]:
            return "Você venceu!"
        else:
            return "Computador venceu!"

def jogar():
    jogada = Jogada()
    while True:
        jogador_escolha = input("Escolha: pedra, papel, tesoura, lagarto, spock: ").lower()
        jogador = jogada.get_opcao(jogador_escolha)
        if jogador is None:
            print("Escolha inválida. Tente novamente.")
            continue
        computador = jogada.get_computador_opcao()
        print(f"Computador escolheu: {computador}")
        resultado = jogada.determinar_vencedor(jogador, computador)
        print(resultado)

if __name__ == "__main__":
    print("Chamando a função para jogar..")
    jogar()
