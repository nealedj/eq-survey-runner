// >>> WARNING THIS PAGE WAS AUTO-GENERATED ON 2016-12-12 22:01:11.979443 - DO NOT EDIT!!! <<<

import MultipleChoiceWithOtherPage from '../../multiple-choice.page'

class VisitorUkResidentPage extends MultipleChoiceWithOtherPage {

  clickVisitorUkResidentAnswerYesUsuallyLivesInTheUnitedKingdom() {
    browser.element('[id="visitor-uk-resident-answer-1"]').click()
    return this
  }

  clickVisitorUkResidentAnswerOther() {
    browser.element('[id="visitor-uk-resident-answer-2"]').click()
    return this
  }

}

export default new VisitorUkResidentPage()