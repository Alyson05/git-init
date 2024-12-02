from datetime import datetime

# Classe Evento para representar os eventos
class Evento:
    def __init__(self, nome, local, data, descricao):
        self.nome = nome
        self.local = local
        self.data = data
        self.descricao = descricao

    def __str__(self):
        return f"Nome: {self.nome}\nLocal: {self.local}\nData: {self.data.strftime('%d/%m/%Y')}\nDescrição: {self.descricao}\n"

# Função para exibir o menu de opções
def exibir_menu():
    print("\n---- SISTEMA DE GESTÃO DE EVENTOS ----")
    print("1. Criar evento")
    print("2. Listar eventos")
    print("3. Editar evento")
    print("4. Excluir evento")
    print("5. Sair")

# Função para criar um evento
def criar_evento(eventos):
    nome = input("Digite o nome do evento: ")
    local = input("Digite o local do evento: ")
    data_str = input("Digite a data do evento (formato: dd/mm/aaaa): ")
    descricao = input("Digite a descrição do evento: ")
    
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
    except ValueError:
        print("Formato de data inválido. Tente novamente.")
        return
    
    evento = Evento(nome, local, data, descricao)
    eventos.append(evento)
    print("Evento criado com sucesso!")

# Função para listar todos os eventos
def listar_eventos(eventos):
    if len(eventos) == 0:
        print("Nenhum evento cadastrado.")
    else:
        print("\n--- Eventos Cadastrados ---")
        for i, evento in enumerate(eventos, start=1):
            print(f"\nEvento {i}:\n{evento}")

# Função para editar um evento
def editar_evento(eventos):
    if len(eventos) == 0:
        print("Nenhum evento para editar.")
        return
    
    listar_eventos(eventos)
    try:
        indice = int(input("Digite o número do evento que deseja editar: "))
        if 1 <= indice <= len(eventos):
            evento = eventos[indice - 1]
            print(f"Editando o evento: {evento.nome}")
            nome = input(f"Novo nome (atual: {evento.nome}): ") or evento.nome
            local = input(f"Novo local (atual: {evento.local}): ") or evento.local
            data_str = input(f"Nova data (atual: {evento.data.strftime('%d/%m/%Y')}): ") or evento.data.strftime('%d/%m/%Y')
            descricao = input(f"Nova descrição (atual: {evento.descricao}): ") or evento.descricao
            
            try:
                data = datetime.strptime(data_str, "%d/%m/%Y")
            except ValueError:
                print("Formato de data inválido. Tente novamente.")
                return
            
            evento.nome = nome
            evento.local = local
            evento.data = data
            evento.descricao = descricao
            print("Evento editado com sucesso!")
        else:
            print("Número de evento inválido.")
    except ValueError:
        print("Entrada inválida! Digite um número.")

# Função para excluir um evento
def excluir_evento(eventos):
    if len(eventos) == 0:
        print("Nenhum evento para excluir.")
        return
    
    listar_eventos(eventos)
    try:
        indice = int(input("Digite o número do evento que deseja excluir: "))
        if 1 <= indice <= len(eventos):
            evento_removido = eventos.pop(indice - 1)
            print(f"Evento '{evento_removido.nome}' excluído com sucesso!")
        else:
            print("Número de evento inválido.")
    except ValueError:
        print("Entrada inválida! Digite um número.")

# Função principal para gerenciar o sistema
def main():
    eventos = []  # Lista para armazenar os eventos
    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção (1-5): "))
            if opcao == 1:
                criar_evento(eventos)
            elif opcao == 2:
                listar_eventos(eventos)
            elif opcao == 3:
                editar_evento(eventos)
            elif opcao == 4:
                excluir_evento(eventos)
            elif opcao == 5:
                print("Saindo do sistema... Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número entre 1 e 5.")

# Executa o sistema
if __name__ == "__main__":
    main()
