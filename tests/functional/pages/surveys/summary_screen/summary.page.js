// >>> WARNING THIS PAGE WAS AUTO-GENERATED - DO NOT EDIT!!! <<<
const QuestionPage = require('../question.page');

class SummaryPage extends QuestionPage {

  constructor() {
    super('summary');
  }

  radioAnswer(index = 0) { return '#radio-answer-' + index + '-answer'; }

  radioAnswerEdit(index = 0) { return '[data-qa="radio-answer-' + index + '-edit"]'; }

  otherAnswerMandatory(index = 0) { return '#other-answer-mandatory-' + index + '-answer'; }

  otherAnswerMandatoryEdit(index = 0) { return '[data-qa="other-answer-mandatory-' + index + '-edit"]'; }

  testCurrency(index = 0) { return '#test-currency-' + index + '-answer'; }

  testCurrencyEdit(index = 0) { return '[data-qa="test-currency-' + index + '-edit"]'; }

  squareKilometres(index = 0) { return '#square-kilometres-' + index + '-answer'; }

  squareKilometresEdit(index = 0) { return '[data-qa="square-kilometres-' + index + '-edit"]'; }

  testDecimal(index = 0) { return '#test-decimal-' + index + '-answer'; }

  testDecimalEdit(index = 0) { return '[data-qa="test-decimal-' + index + '-edit"]'; }

  summaryGroupTitle(index = 0) { return '#summary-group-' + index; }

  dessert(index = 0) { return '#dessert-' + index + '-answer'; }

  dessertEdit(index = 0) { return '[data-qa="dessert-' + index + '-edit"]'; }

  dessertGroupTitle(index = 0) { return '#dessert-group-' + index; }

}
module.exports = new SummaryPage();
