// >>> WARNING THIS PAGE WAS AUTO-GENERATED - DO NOT EDIT!!! <<<
const QuestionPage = require('../../surveys/question.page');

class ThirdNumberBlockPage extends QuestionPage {

  constructor() {
    super('third-number-block');
  }

  thirdNumber() {
    return '#third-number-answer';
  }

  thirdNumberLabel() { return '#label-third-number-answer'; }

  thirdNumberNotInTotal() {
    return '#third-number-answer-not-in-total';
  }

  thirdNumberNotInTotalLabel() { return '#label-third-number-answer-not-in-total'; }

}
module.exports = new ThirdNumberBlockPage();
