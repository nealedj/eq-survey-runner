// >>> WARNING THIS PAGE WAS AUTO-GENERATED - DO NOT EDIT!!! <<<
const QuestionPage = require('../../surveys/question.page');

class TotalPlaybackPage extends QuestionPage {

  constructor() {
    super('total-playback');
  }

  firstNumberAnswer() { return '#first-number-answer-answer'; }

  firstNumberAnswerEdit() { return '[data-qa="first-number-answer-edit"]'; }

  secondNumberAnswer() { return '#second-number-answer-answer'; }

  secondNumberAnswerEdit() { return '[data-qa="second-number-answer-edit"]'; }

  secondNumberAnswerNotInTotal() { return '#second-number-answer-not-in-total-answer'; }

  secondNumberAnswerNotInTotalEdit() { return '[data-qa="second-number-answer-not-in-total-edit"]'; }

  secondNumberAnswerAlsoInTotal() { return '#second-number-answer-also-in-total-answer'; }

  secondNumberAnswerAlsoInTotalEdit() { return '[data-qa="second-number-answer-also-in-total-edit"]'; }

  thirdNumberAnswer() { return '#third-number-answer-answer'; }

  thirdNumberAnswerEdit() { return '[data-qa="third-number-answer-edit"]'; }

  thirdNumberAnswerNotInTotal() { return '#third-number-answer-not-in-total-answer'; }

  thirdNumberAnswerNotInTotalEdit() { return '[data-qa="third-number-answer-not-in-total-edit"]'; }

  fourthNumberAnswer() { return '#fourth-number-answer-answer'; }

  fourthNumberAnswerEdit() { return '[data-qa="fourth-number-answer-edit"]'; }

  fourthNumberAnswerAlsoInTotal() { return '#fourth-number-answer-also-in-total-answer'; }

  fourthNumberAnswerAlsoInTotalEdit() { return '[data-qa="fourth-number-answer-also-in-total-edit"]'; }

  fifthNumberAnswer() { return '#fifth-number-answer-answer'; }

  fifthNumberAnswerEdit() { return '[data-qa="fifth-number-answer-edit"]'; }

  calculatedSummaryTitle() { return '[data-qa="calculated-summary-title"]'; }

  calculatedSummaryQuestion() { return '#calculated-summary-question'; }

  calculatedSummaryAnswer() { return '#calculated-summary-answer-answer'; }

  groupTitle() { return '#group'; }

}
module.exports = new TotalPlaybackPage();
