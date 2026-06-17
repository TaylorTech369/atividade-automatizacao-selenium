describe('Sistema 1', () => {
  it('Cenário de teste completo', () => {

    cy.visit("https://sistema-1-login.netlify.app ")



    cy.contains('conta').click()

    cy.get('#name').type('joão')
    cy.get('#email').type('joao@gmail.com')
    cy.get('#password').type('123456Ph')

    cy.get('#confirmPassword').type('123456Ph')

    cy.get('#terms').click()


















  });
});