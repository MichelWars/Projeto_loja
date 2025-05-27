/*
Esse arquivo JS define a função adicionarAoCarrinho(produtoId),
que serve para enviar um produto ao carrinho de compras usando AJAX
(via fetch) sem recarregar a página.
*/


// Atualiza o contador de itens no carrinho ao carregar a página
function atualizarContadorCarrinho() {
    fetch("/carrinho/total-itens/")
        .then(response => response.json())
        .then(data => {
            document.getElementById("contador-carrinho").innerText = data.total_itens;
        });
}

// Envia produto ao carrinho via POST e atualiza o contador
function adicionarAoCarrinho(produtoId) {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch("/carrinho/adicionar/", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `produto_id=${produtoId}&quantidade=1`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("contador-carrinho").innerText = data.total_itens;
    });
}



// Executa assim que a página terminar de carregar
document.addEventListener("DOMContentLoaded", atualizarContadorCarrinho);
