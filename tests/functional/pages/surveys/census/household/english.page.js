// >>> WARNING THIS PAGE WAS AUTO-GENERATED - DO NOT EDIT!!! <<<
const QuestionPage = require('../../question.page');

class EnglishPage extends QuestionPage {

  constructor() {
    super('english');
  }

  veryWell() {
    return '#english-answer-0';
  }

  well() {
    return '#english-answer-1';
  }

  notWell() {
    return '#english-answer-2';
  }

  notAtAll() {
    return '#english-answer-3';
  }

}
module.exports = new EnglishPage();
