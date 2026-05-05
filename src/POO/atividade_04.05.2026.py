class Reserva:
    def __init__(self, nome_hospede, numero_quarto, quantidade_dias):
        self._nome_hospede = nome_hospede
        self._numero_quarto = numero_quarto
        self._quantidade_dias = quantidade_dias

        if not nome_hospede.strip():
            raise ValueError("O nome do hóspede não pode ser vazio.")
        
        if numero_quarto <= 0:
            raise ValueError("O número do quarto é inválido.")
        
        if quantidade_dias <= 0:
            raise ValueError("Quantidade de dias inválido.")
        
    
    @property
    def nome_hospede(self):
        return self._nome_hospede
    
    @nome_hospede.setter
    def nome_hospede(self, atualizar_nome):
        if not atualizar_nome.strip():
            raise ValueError("O nome do hóspede não pode ser vazio.")
        
        self._nome_hospede = atualizar_nome

    
    @property
    def numero_quarto(self):
        return self._numero_quarto
    
    @property
    def quantidade_dias(self):
        return self._quantidade_dias
    

    @quantidade_dias.setter
    def quantidade_dias(self, atualizar_quantidade_dias):
        if atualizar_quantidade_dias <= 0:
            raise ValueError("A quantidade de dias deve ser maior que zero.")
        
        self._quantidade_dias = atualizar_quantidade_dias

    
    def alterar_quarto(self, atualizar_quarto):
        if atualizar_quarto <= 0:
            raise ValueError("Número de quarto inválido.")
        
        self._numero_quarto = atualizar_quarto
        print("Quarto alterado.")
    
    
    def adicionar_dias(self, mais_dias):
        if mais_dias <= 0:
            print("Quantidade de dias inválidos.")
            return
        
        self._quantidade_dias += mais_dias
        print("Estadia atualizada: ", self._quantidade_dias, "dia(s).")

    def reduzir_dias(self, menos_dias):
        if menos_dias > self._quantidade_dias and menos_dias == 0:
            print("A quantidade deve ser menor ou igual a quantidade de dias já cadastrada e maior que zero.")
            return
        
        self._quantidade_dias -= menos_dias
        print(f"Estadia atualizada: {self._quantidade_dias} dia(s).")


    def mostrar_reserva(self):
        print("\nDados da reserva: ")
        print(f"Hospede: {self._nome_hospede}")
        print(f"Quarto: {self._numero_quarto}")
        print(f"Estadia: {self._quantidade_dias} dia(s).")


reserva1 = Reserva("Henrique", 10, 11)
reserva1.mostrar_reserva()

reserva1.nome_hospede = str(input("Informe o nome para a atualizar o seu cadastro: "))
reserva1.quantidade_dias = 3


reserva1.alterar_quarto(-1)
reserva1.adicionar_dias(-2)
reserva1.reduzir_dias(-3)
# 10.
# Resposta: O risco está na liberdade dada a toda parte do projeto em que qualquer desenvolvedor do projeto pode acessar e alterar esses atributos,
# arriscando a integridade do código e dos dados.
    

    


        
