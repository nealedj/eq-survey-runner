// >>> WARNING THIS PAGE WAS AUTO-GENERATED ON 2016-12-12 22:01:11.893043 - DO NOT EDIT!!! <<<

import MultipleChoiceWithOtherPage from '../../multiple-choice.page'

class SexualIdentityPage extends MultipleChoiceWithOtherPage {

  clickSexualIdentityAnswerHeterosexualOrStraight() {
    browser.element('[id="sexual-identity-answer-1"]').click()
    return this
  }

  clickSexualIdentityAnswerGayOrLesbian() {
    browser.element('[id="sexual-identity-answer-2"]').click()
    return this
  }

  clickSexualIdentityAnswerBisexual() {
    browser.element('[id="sexual-identity-answer-3"]').click()
    return this
  }

  clickSexualIdentityAnswerOther() {
    browser.element('[id="sexual-identity-answer-4"]').click()
    return this
  }

}

export default new SexualIdentityPage()