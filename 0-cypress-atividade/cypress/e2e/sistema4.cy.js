describe('Sistema 4', () => {
  it('Cenário de teste completo', () => {

    cy.visit("https://sistema-4-urna-v2.netlify.app/")

    // cy.contains('6').click()
    // cy.contains('4').click()

    cy.contains('1').click()
    cy.contains('2').click()

    cy.get('.btn-confirma').click()

    cy.screenshot('print-sistema2')

  });
});