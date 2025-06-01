  const formaPagamento = document.getElementById('id_forma_pagamento');
  const parcelasContainer = document.getElementById('parcelas-container');
  const parcelasSelect = document.getElementById('parcelas');
  const valorParcela = document.getElementById('valor-parcela');
  const valorTotal = parseFloat(document.getElementById('valor-total').innerText.replace(",", "."));


  // Função para atualizar o container de parcelas
  function atualizarParcelas() {
    if (formaPagamento.value === 'credito') {
      parcelasContainer.style.display = 'block';
    } else {
      parcelasContainer.style.display = 'none';
      valorParcela.innerText = '';
    }
  }
// Função para atualizar o valor por parcela
  parcelasSelect.addEventListener('change', () => {
    const parcelas = parseInt(parcelasSelect.value);
    const valorPorParcela = (valorTotal / parcelas).toFixed(2);
    valorParcela.innerText = `Valor por parcela: R$ ${valorPorParcela}`;
  });

  formaPagamento.addEventListener('change', atualizarParcelas);
  document.addEventListener('DOMContentLoaded', atualizarParcelas);