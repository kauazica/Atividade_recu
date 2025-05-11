# 🧠 Sistema de Gerenciamento de Projetos com Flask

Este projeto é uma aplicação web simples feita com Python e Flask que permite **gerenciar projetos e tarefas**. Os dados são armazenados em arquivos `.csv`.

---

### 🛠️ Como executar o projeto

### 1. Crie e ative um ambiente virtual

**Windows:**

```bash

python -m venv venv
venv\Scripts\activat

```

### 2. Instale as dependências

```bash
pip install flask

```

---

### ▶️ Rodando o app

Execute o arquivo `app.py`:

```bash
python app.py

```

---

### 🔧 Como funciona o sistema

1. **Página inicial (`/`)**
    - Lista todos os projetos registrados.
    - Permite acessar cada projeto individualmente.
2. **Página de criação de projetos (`/criar`)**
    - Formulário para adicionar novos projetos.
    - Cada projeto contém: `id`, `nome`, `descrição` e `data de criação`.
3. **Página do projeto (`/projeto/<id>`)**
    - Mostra as tarefas ligadas a um projeto específico.
    - Permite adicionar novas tarefas diretamente da página.
    - Cada tarefa possui: `id`, `projeto_id`, `título`, `descrição` e `status`.
4. **Edição de tarefas**
    - As tarefas podem ser editadas diretamente na página do projeto.
    - O status pode ser "Pendente", "Em andamento" ou "Concluída".
5. **Exclusão**
    - Projetos e tarefas podem ser excluídos.
    - Ao excluir um projeto, todas as tarefas ligadas a ele também são removidas automaticamente.

### 🧩 Tecnologias utilizadas

- **Python 3**
- **Flask** (para rotas, renderização e requisições HTTP)
- **CSV** (como forma simples de banco de dados)
- **HTML com Jinja2** (para renderização dinâmica de páginas)
- **Tailwind CSS** (para um visual bonito e moderno)

### 📦 Armazenamento

O projeto **não usa banco de dados tradicional**. Toda a persistência de dados é feita com arquivos `.csv`:

- `projetos.csv` → armazena todos os projetos.
- `tarefas.csv` → armazena todas as tarefas.

### 🌆 Imagens do projeto
