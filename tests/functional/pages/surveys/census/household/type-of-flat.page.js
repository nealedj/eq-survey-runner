// >>> WARNING THIS PAGE WAS AUTO-GENERATED ON 2016-12-12 22:01:11.831487 - DO NOT EDIT!!! <<<

import MultipleChoiceWithOtherPage from '../../multiple-choice.page'

class TypeOfFlatPage extends MultipleChoiceWithOtherPage {

  clickTypeOfFlatAnswerInAPurposeBuiltBlockOfFlatsOrTenement() {
    browser.element('[id="type-of-flat-answer-1"]').click()
    return this
  }

  clickTypeOfFlatAnswerPartOfAConvertedOrSharedHouseIncludingBedsits() {
    browser.element('[id="type-of-flat-answer-2"]').click()
    return this
  }

  clickTypeOfFlatAnswerInACommercialBuildingForExampleInAnOfficeBuildingHotelOrOverAShop() {
    browser.element('[id="type-of-flat-answer-3"]').click()
    return this
  }

}

export default new TypeOfFlatPage()