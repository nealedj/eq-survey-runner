// >>> WARNING THIS PAGE WAS AUTO-GENERATED ON 2016-12-12 22:01:11.927533 - DO NOT EDIT!!! <<<

import MultipleChoiceWithOtherPage from '../../multiple-choice.page'

class JobPendingPage extends MultipleChoiceWithOtherPage {

  clickJobPendingAnswerYes() {
    browser.element('[id="job-pending-answer-1"]').click()
    return this
  }

  clickJobPendingAnswerNo() {
    browser.element('[id="job-pending-answer-2"]').click()
    return this
  }

}

export default new JobPendingPage()