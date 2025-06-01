# Esse arquivo faz gerenciamento de sessões


class Carrinho:
    # Inicializa o carrinho pegando (ou criando) a chave 'carrinho' na sessão
    def __init__(self, request):
        self.session = request.session
        carrinho = self.session.get('carrinho')
        if not carrinho:
            carrinho = self.session['carrinho'] = {}
        self.carrinho = carrinho

    # Adiciona um produto ao carrinho ou incrementa a quantidade
    def adicionar(self, produto_id, quantidade=1):
        produto_id = str(produto_id)
        if produto_id in self.carrinho:
            self.carrinho[produto_id] += quantidade
        else:
            self.carrinho[produto_id] = quantidade
        self.salvar()

    # Remove um produto do carrinho
    def remover(self, produto_id):
        produto_id = str(produto_id)
        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            self.salvar()

    # Atualiza a quantidade de um produto
    def atualizar(self, produto_id, quantidade):
        produto_id = str(produto_id)
        if quantidade > 0:
            self.carrinho[produto_id] = quantidade
        else:
            self.remover(produto_id)
        self.salvar()

    # Limpa completamente o carrinho
    def limpar(self):
        self.session['carrinho'] = {}
        self.salvar()

    # Marca a sessão como modificada, para o Django salvar automaticamente
    def salvar(self):
        self.session.modified = True

    # Retorna uma cópia dos itens do carrinho
    def itens(self):
        return self.carrinho.copy()
