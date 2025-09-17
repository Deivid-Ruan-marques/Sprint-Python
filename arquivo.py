import json
import os

def carregar_dados(caminho_arquivo):
    """Carrega os dados de um arquivo JSON."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Erro ao ler o arquivo {caminho_arquivo}. O arquivo está vazio ou corrompido.")
        return []

def salvar_dados(dados, caminho_arquivo):
    """Salva os dados em um arquivo JSON."""
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4)
    print(f"Dados salvos em {caminho_arquivo} com sucesso!")

# --- Funções para Gerenciar Atletas ---

def adicionar_atleta():
    try:
        nome = input("Digite o nome da atleta: ").strip()
        idade = int(input("Digite a idade: "))
        posicao = input("Digite a posição (ex: atacante, zagueira): ").strip()

        if not nome or idade <= 0 or not posicao:
            print("Erro: Todos os campos são obrigatórios e a idade deve ser um número positivo.")
            return

        dados = carregar_dados('atletas.json')
        nova_atleta = {
            "nome": nome,
            "idade": idade,
            "posicao": posicao,
            "historico_peneiras": []
        }
        dados.append(nova_atleta)
        salvar_dados(dados, 'atletas.json')
        print(f"Atleta '{nome}' cadastrada com sucesso!")

    except ValueError:
        print("Erro: A idade deve ser um número inteiro. Tente novamente.")

def listar_atletas():
    dados = carregar_dados('atletas.json')
    if not dados:
        print("Nenhuma atleta cadastrada.")
        return

    print("\n--- Lista de Atletas ---")
    for i, atleta in enumerate(dados):
        print(f"ID: {i} | Nome: {atleta['nome']}, Idade: {atleta['idade']}, Posição: {atleta['posicao']}")

def buscar_atleta():
    nome_busca = input("Digite o nome da atleta que deseja buscar: ").strip().lower()
    dados = carregar_dados('atletas.json')
    encontrados = [atleta for atleta in dados if nome_busca in atleta['nome'].lower()]

    if not encontrados:
        print(f"Nenhuma atleta encontrada com o nome '{nome_busca}'.")
    else:
        print("\n--- Atletas Encontradas ---")
        for atleta in encontrados:
            print(f"Nome: {atleta['nome']}, Idade: {atleta['idade']}, Posição: {atleta['posicao']}")

def alterar_atleta():
    listar_atletas()
    try:
        atleta_id = int(input("Digite o ID da atleta que deseja alterar: "))
        dados = carregar_dados('atletas.json')
        
        if 0 <= atleta_id < len(dados):
            atleta = dados[atleta_id]
            print(f"Alterando dados de: {atleta['nome']}")
            
            novo_nome = input(f"Novo nome (atual: {atleta['nome']}): ") or atleta['nome']
            nova_idade = input(f"Nova idade (atual: {atleta['idade']}): ") or str(atleta['idade'])
            nova_posicao = input(f"Nova posição (atual: {atleta['posicao']}): ") or atleta['posicao']
            
            atleta['nome'] = novo_nome
            atleta['posicao'] = nova_posicao
            if nova_idade.isdigit():
                atleta['idade'] = int(nova_idade)

            salvar_dados(dados, 'atletas.json')
            print("Dados da atleta alterados com sucesso!")
        else:
            print("ID inválido. Por favor, escolha um ID da lista.")
    except (ValueError, IndexError):
        print("Erro: Entrada inválida. Certifique-se de digitar um número válido.")

def remover_atleta():
    listar_atletas()
    try:
        atleta_id = int(input("Digite o ID da atleta que deseja remover: "))
        dados = carregar_dados('atletas.json')
        
        if 0 <= atleta_id < len(dados):
            atleta_removida = dados.pop(atleta_id)
            salvar_dados(dados, 'atletas.json')
            print(f"Atleta '{atleta_removida['nome']}' removida com sucesso!")
        else:
            print("ID inválido. Por favor, escolha um ID da lista.")
    except (ValueError, IndexError):
        print("Erro: Entrada inválida. Certifique-se de digitar um número válido.")

# --- Funções para Gerenciar Peneiras ---

def adicionar_peneira():
    print("\n--- Cadastro de Peneira/Oportunidade ---")
    nome = input("Nome da Peneira/Local: ").strip()
    local = input("Localidade (Cidade/Bairro): ").strip()
    tipo = input("Tipo (ex: 'Peneira', 'Escolinha', 'Quadra'): ").strip()
    
    if not nome or not local or not tipo:
        print("Erro: Nome, Localidade e Tipo são campos obrigatórios.")
        return

    dados = carregar_dados('peneiras.json')
    nova_peneira = {
        "nome": nome,
        "local": local,
        "tipo": tipo,
        "requisitos": input("Requisitos (ex: 'Idade 15-18'): ").strip() or "N/A",
        "link": input("Link para mais informações: ").strip() or "N/A"
    }
    dados.append(nova_peneira)
    salvar_dados(dados, 'peneiras.json')
    print(f"Peneira/Oportunidade '{nome}' cadastrada com sucesso!")

def listar_peneiras():
    dados = carregar_dados('peneiras.json')
    if not dados:
        print("Nenhuma peneira ou local cadastrado.")
        return

    print("\n--- Lista de Peneiras e Oportunidades ---")
    for i, peneira in enumerate(dados):
        print(f"ID: {i} | Nome: {peneira['nome']}, Tipo: {peneira['tipo']}, Local: {peneira['local']}")

def buscar_peneira():
    termo_busca = input("Digite o nome ou tipo da peneira que deseja buscar: ").strip().lower()
    dados = carregar_dados('peneiras.json')
    encontrados = [peneira for peneira in dados if termo_busca in peneira['nome'].lower() or termo_busca in peneira['tipo'].lower()]

    if not encontrados:
        print(f"Nenhuma oportunidade encontrada para '{termo_busca}'.")
    else:
        print("\n--- Oportunidades Encontradas ---")
        for peneira in encontrados:
            print(f"Nome: {peneira['nome']}, Tipo: {peneira['tipo']}, Local: {peneira['local']}, Requisitos: {peneira['requisitos']}")

def alterar_peneira():
    listar_peneiras()
    try:
        peneira_id = int(input("Digite o ID da peneira que deseja alterar: "))
        dados = carregar_dados('peneiras.json')
        
        if 0 <= peneira_id < len(dados):
            peneira = dados[peneira_id]
            print(f"Alterando dados de: {peneira['nome']}")
            
            peneira['nome'] = input(f"Novo nome (atual: {peneira['nome']}): ") or peneira['nome']
            peneira['local'] = input(f"Nova localidade (atual: {peneira['local']}): ") or peneira['local']
            peneira['tipo'] = input(f"Novo tipo (atual: {peneira['tipo']}): ") or peneira['tipo']
            
            salvar_dados(dados, 'peneiras.json')
            print("Dados da peneira alterados com sucesso!")
        else:
            print("ID inválido.")
    except (ValueError, IndexError):
        print("Erro: Entrada inválida. Certifique-se de digitar um número válido.")

def remover_peneira():
    listar_peneiras()
    try:
        peneira_id = int(input("Digite o ID da peneira que deseja remover: "))
        dados = carregar_dados('peneiras.json')
        
        if 0 <= peneira_id < len(dados):
            peneira_removida = dados.pop(peneira_id)
            salvar_dados(dados, 'peneiras.json')
            print(f"Peneira '{peneira_removida['nome']}' removida com sucesso!")
        else:
            print("ID inválido.")
    except (ValueError, IndexError):
        print("Erro: Entrada inválida. Certifique-se de digitar um número válido.")

# --- Menus ---

def menu_atletas():
    while True:
        print("\n--- Gerenciar Atletas ---")
        print("1. Adicionar nova atleta")
        print("2. Listar todas as atletas")
        print("3. Buscar atleta por nome")
        print("4. Alterar dados de uma atleta")
        print("5. Remover uma atleta")
        print("6. Voltar ao menu principal")
        
        escolha = input("Digite sua opção: ")
        
        if escolha == '1':
            adicionar_atleta()
        elif escolha == '2':
            listar_atletas()
        elif escolha == '3':
            buscar_atleta()
        elif escolha == '4':
            alterar_atleta()
        elif escolha == '5':
            remover_atleta()
        elif escolha == '6':
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

def menu_peneiras():
    while True:
        print("\n--- Gerenciar Peneiras/Oportunidades ---")
        print("1. Adicionar nova peneira/local")
        print("2. Listar todas as oportunidades")
        print("3. Buscar oportunidade por nome/tipo")
        print("4. Alterar dados de uma oportunidade")
        print("5. Remover uma oportunidade")
        print("6. Voltar ao menu principal")
        
        escolha = input("Digite sua opção: ")

        if escolha == '1':
            adicionar_peneira()
        elif escolha == '2':
            listar_peneiras()
        elif escolha == '3':
            buscar_peneira()
        elif escolha == '4':
            alterar_peneira()
        elif escolha == '5':
            remover_peneira()
        elif escolha == '6':
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

def main():
    while True:
        print("\n=== Sistema de Gestão Futebol Feminino ===")
        print("1. Gerenciar Atletas")
        print("2. Gerenciar Peneiras/Oportunidades")
        print("3. Sair")
        
        escolha = input("Digite sua opção: ")
        
        if escolha == '1':
            menu_atletas()
        elif escolha == '2':
            menu_peneiras()
        elif escolha == '3':
            print("Obrigado por usar o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()