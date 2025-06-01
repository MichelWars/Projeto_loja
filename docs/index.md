# 🕹️ Loja de Games - E-commerce com Django

Este projeto é uma loja virtual de mídias físicas de videogames, construída com **Django** e **Bootstrap**, com foco tanto em clientes finais quanto na administração de estoque e pedidos.

## 📦 Funcionalidades

### 👤 Usuários (Clientes)
- Cadastro e login de usuários.
- Catálogo de produtos com visual atraente e responsivo.
- Visualização detalhada dos produtos.
- Carrinho de compras baseado em **sessão**, sem necessidade de login prévio.
- Finalização de pedido com preenchimento de dados.
- Histórico de pedidos feitos e visualização detalhada de cada um.

### 🔐 Administrador
- Acesso ao painel administrativo.
- Cadastro, atualização e exclusão de produtos.
- Entrada de mercadorias no estoque.
- Visualização de:
  - Quantidade total de produtos.
  - Valor total em estoque.
  - Lista detalhada de produtos com respectivas quantidades.
- Listagem de todos os pedidos realizados.

### ⚙️ Funcionalidades Extras
- **Geração automática de descrição de produto** com **IA generativa** (Gemini API) caso a descrição não seja fornecida.
- **Imagem genérica automática** adicionada via `signals` caso nenhuma imagem seja enviada.
- Carrinho inteligente com totalizador, atualização de quantidades e persistência por sessão.

---

## 🗂️ Estrutura do Projeto

```bash
Projeto_loja/
├── accounts/             # Gerenciamento de autenticação de usuários
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── templates/
├── app/                  # Arquivos principais da configuração do projeto Django
│   ├── settings.py
│   └── templates/components/  # Templates reutilizáveis (_navbar.html, _footer.html, etc.)
├── carrinho/             # Lógica do carrinho de compras
│   ├── carrinho.py
│   ├── views.py
│   └── templates/ver.html
├── pedidos/              # Finalização e histórico de pedidos
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── templates/
│       ├── finalizar_pedido.html
│       ├── listar_pedidos.html
│       └── ver_pedido.html
├── produtos/             # Gestão de produtos
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── templates/
│       ├── catalogo.html
│       ├── estoque.html
│       ├── cad_prod.html
├── entradas/             # Controle de entrada de mercadorias
│   ├── forms.py
│   ├── models.py
│   └── templates/
├── gemini_api/           # Integração com Gemini (IA generativa)
│   ├── api_key.py
│   └── client.py
├── static/
│   └── js/
│       ├── carrinho.js   # arquivo de atualização dinamica do carrinho
│       └── pedido.js     # arquivo de atualização dinamica do pedido
├── media/                # Uploads de imagens de produtos
├── templates/            # Base e componentes HTML reutilizáveis
├── manage.py
├── requirements.txt      # dependências do projeto
└──  instrucoes.txt       # Instruções de instalação

```