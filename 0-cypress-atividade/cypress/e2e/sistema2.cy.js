describe('Sistema 2', () => {
  it('Cenário de teste completo', () => {

    cy.visit("https://sistema-2-loja.netlify.app ")

    cy.wait(100)

    cy.get('a').click()

    cy.get('#name').type('joão')
    cy.get('#email').type('joao@gmail.com')
    cy.get('#password').type('123456Ph')

    cy.get("button[type='submit']").click() 

    cy.get('#email').type('joao@gmail.com')
    cy.get('#password').type('123456Ph')

    cy.get("button[type='submit']").click() 

    cy.get('#depositInput').type('100000000000000000000000000004500')

    cy.get('#depositButton').click()

    cy.get('#productsTabButton').click()

    cy.contains('Adicionar').click()

    cy.contains('Carrinho').click()

    cy.contains('Finalizar').click()

    cy.screenshot('print-sistema2')
    
    cy.contains('Confirmar').click()

    cy.contains('Logout').click()
















  });
});