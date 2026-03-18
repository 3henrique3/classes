# Polimorfismo

class Celular:
    def ligar(self):
        print("Celular ligado.")

    def desligar(self):
        print("Celular desligado.")

    def ativar_modoAviao(self):
        print("Modo avião ativado")

    def desativar_modoAviao(self):
        print("Modo avião desativado")

    def ativar_wifi(self):
        print("Wi-Fi ativado")

    def desativar_wifi(self):
        print("Wi-Fi desativado")

    def ligar_contato(self, nome):
        print(f"Ligando para {nome}...")

    def desligar_ligacao(self):
        print("Ligação encerrada")

c = Celular()

c.ligar()
c.ativar_modoAviao()
c.ligar_contato("Thalyta")
c.desligar_ligacao()
