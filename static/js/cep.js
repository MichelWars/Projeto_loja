
function buscarEndereco() {
    const cep = document.getElementById("cep").value.replace(/\D/g, '');

    if (cep.length !== 8) {
        alert("CEP inválido!");
        return;
    }

    fetch(`https://viacep.com.br/ws/${cep}/json/`)
        .then(res => res.json())
        .then(data => {
            if (data.erro) {
                alert("CEP não encontrado!");
                return;
            }

            const endereco = `${data.logradouro}, ${data.bairro}, ${data.localidade} - ${data.uf}`;
            document.getElementById("endereco").value = endereco;
        })
        .catch(err => {
            console.error("Erro ao buscar CEP:", err);
            alert("Erro ao buscar endereço!");
        });
}
