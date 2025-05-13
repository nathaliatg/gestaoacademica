# Aluna Nathalia Tianny Gonçalves
# Curso de Análise e Desenvolvimento de Sistemas

import json
import os

# Funções para persistência de dados
def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def carregar_dados(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Funções genéricas
def incluir_registro(lista, campos, validacao=None):
    novo_registro = {}
    for campo, tipo in campos.items():
        while True:
            try:
                valor = input(f"Digite o {campo}: ")
                valor = int(valor) if tipo == int else valor.strip()
                if not valor:
                    raise ValueError("Campo vazio!")
                if campo == 'codigo':
                    if any(item['codigo'] == valor for item in lista):
                        print("Código já existente!")
                        continue
                novo_registro[campo] = valor
                break
            except ValueError as e:
                print(f"Erro: {e}")

    if validacao:
        if not validacao(novo_registro):
            print("Validação falhou! Registro não incluído.")
            return

    lista.append(novo_registro)
    print("Registro incluído com sucesso!")

def listar_registros(lista):
    if not lista:
        print("Nenhum registro encontrado.")
        return
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item}")

def atualizar_registro(lista, chave):
    codigo = input("Digite o código do registro a ser atualizado: ")
    for item in lista:
        if str(item[chave]) == codigo:
            for campo in item:
                novo_valor = input(f"{campo} atual: {item[campo]}. Novo valor (deixe vazio para manter): ")
                if novo_valor:
                    item[campo] = int(novo_valor) if isinstance(item[campo], int) else novo_valor.strip()
            print("Registro atualizado!")
            return
    print("Registro não encontrado!")

def excluir_registro(lista, chave):
    codigo = input("Digite o código do registro a ser excluído: ")
    for i, item in enumerate(lista):
        if str(item[chave]) == codigo:
            del lista[i]
            print("Registro excluído com sucesso!")
            return
    print("Registro não encontrado!")

# Dados principais e arquivos
tabelas = {
    "Estudantes": {"dados": [], "arquivo": "estudantes.json", "campos": {"codigo": int, "nome": str}},
    "Professores": {"dados": [], "arquivo": "professores.json", "campos": {"codigo": int, "nome": str, "cpf": str}},
    "Disciplinas": {"dados": [], "arquivo": "disciplinas.json", "campos": {"codigo": int, "nome": str}},
    "Turmas": {"dados": [], "arquivo": "turmas.json", "campos": {"codigo": int, "codigo_professor": int, "codigo_disciplina": int}},
    "Matriculas": {"dados": [], "arquivo": "matriculas.json", "campos": {"codigo_turma": int, "codigo_estudante": int}},
}

# Carregar dados existentes
for tabela in tabelas.values():
    tabela["dados"] = carregar_dados(tabela["arquivo"])

# Menus
def menu_operacoes(tipo):
    while True:
        print(f"\n--- MENU DE OPERAÇÕES: {tipo.upper()} ---")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")
        dados = tabelas[tipo]['dados']
        campos = tabelas[tipo]['campos']
        arquivo = tabelas[tipo]['arquivo']

        if opcao == "1":
            incluir_registro(dados, campos)
            salvar_dados(arquivo, dados)
        elif opcao == "2":
            listar_registros(dados)
        elif opcao == "3":
            atualizar_registro(dados, 'codigo')
            salvar_dados(arquivo, dados)
        elif opcao == "4":
            excluir_registro(dados, 'codigo')
            salvar_dados(arquivo, dados)
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")

def menu_principal():
    while True:
        print("\nBEM-VINDO AO MENU PRINCIPAL")
        opcoes = list(tabelas.keys()) + ["Sair"]
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i}. {opcao}")
        escolha = input("Escolha uma opção: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            if opcoes[int(escolha)-1] == "Sair":
                print("Encerrando o sistema...")
                break
            else:
                menu_operacoes(opcoes[int(escolha)-1])
        else:
            print("Opção inválida! Tente novamente.")

# Iniciar sistema
menu_principal()
