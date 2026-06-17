describe('Sistema 3', () => {
  it('Cenário de teste completo', () => {

    cy.visit("https://sistema-3-estoque.netlify.app/")

    const produtos = [
      { "nome": "Teclado Mecânico", "categoria": "Periféricos", "quantidade": "15", "preco": "250" },
      { "nome": "Mouse Gamer", "categoria": "Periféricos", "quantidade": "30", "preco": "120" },
      { "nome": "Monitor 24'", "categoria": "Monitores", "quantidade": "5", "preco": "899" },
      { "nome": "Headset HyperX", "categoria": "Áudio", "quantidade": "12", "preco": "349" },
      { "nome": "Webcam Full HD", "categoria": "Periféricos", "quantidade": "8", "preco": "199" },
      { "nome": "Cadeira Gamer", "categoria": "Móveis", "quantidade": "4", "preco": "1200" },
      { "nome": "Mousepad Extended", "categoria": "Acessórios", "quantidade": "25", "preco": "59" },
      { "nome": "SSD 1TB NVMe", "categoria": "Hardware", "quantidade": "20", "preco": "450" },
      { "nome": "Memória RAM 16GB", "categoria": "Hardware", "quantidade": "18", "preco": "299" },
      { "nome": "Gabinete ATX RGB", "categoria": "Hardware", "quantidade": "6", "preco": "380" }
    ]

    produtos.forEach((produto) => {

    cy.get('#nome-produto').clear().type(produto.nome)
    cy.get('#categoria-produto').clear().type(produto.categoria)
    cy.get('#quantidade-produto').clear().type(produto.quantidade)
    cy.get('#preco-produto').clear().type(produto.preco)

    cy.get('#btn-cadastrar').click()

    })

  });
});