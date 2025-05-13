# 📚 Sistema de Gestão Acadêmica

Este é um projeto desenvolvido em Python como parte de uma atividade acadêmica. O sistema permite o cadastro e gerenciamento de **estudantes, professores, disciplinas, turmas e matrículas**, com persistência de dados em arquivos.

## ✅ Funcionalidades

O sistema oferece as seguintes operações para cada módulo:

* **Estudantes**
* **Professores**
* **Disciplinas**
* **Turmas**
* **Matrículas**

Cada módulo permite:

* Incluir novo registro
* Listar registros
* Atualizar registros
* Excluir registros

Além disso, o sistema conta com:

* Validação de dados (ex: evitar códigos duplicados)
* Manipulação de arquivos para persistência
* Tratamento de exceções com `try/except`
* Organização dos dados em listas e dicionários
* Menus com navegação por `while` e `if/elif`
* Funções modulares reaproveitadas entre os módulos

## 💻 Como executar o projeto

1. Certifique-se de ter o Python 3 instalado.
2. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```
3. Acesse a pasta do projeto:

   ```bash
   cd nome-do-repositorio
   ```
4. Execute o sistema:

   ```bash
   python main.py
   ```

## 🗂 Estrutura do Projeto

```
📁 nome-do-repositorio/
├── main.py
├── estudantes.txt
├── professores.txt
├── disciplinas.txt
├── turmas.txt
├── matriculas.txt
└── ...
```

> Os arquivos `.txt` são utilizados para armazenar os dados de cada módulo.

## 🛠 Tecnologias utilizadas

* Python 3.x
* Manipulação de arquivos (`open`, `read`, `write`)
* Programação estruturada

## 📌 Melhorias futuras

* Implementar interface gráfica
* Aplicar testes automatizados
* Separar os módulos em arquivos distintos para melhor organização
* Criação de autenticação para diferentes perfis (admin/aluno)

## 📄 Licença

Este projeto é de uso acadêmico e não possui uma licença específica. Fique à vontade para usar como base para seus estudos.

---

Se quiser, posso incluir seu nome, print do terminal ou badge do Python. É só me avisar! 😄
