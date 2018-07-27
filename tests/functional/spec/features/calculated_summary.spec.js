const helpers = require('../../helpers');

const FirstNumberBlockPage = require('../../pages/features/calculated_summary/first-number-block.page.js');
const SecondNumberBlockPage = require('../../pages/features/calculated_summary/second-number-block.page.js');
const ThirdNumberBlockPage = require('../../pages/features/calculated_summary/third-number-block.page.js');
const FourthNumberBlockPage = require('../../pages/features/calculated_summary/fourth-number-block.page.js');
const FifthNumberBlockPage = require('../../pages/features/calculated_summary/fifth-number-block.page.js');
const TotalPlaybackPage = require('../../pages/features/calculated_summary/total-playback.page.js');
const SummaryPage = require('../../pages/summary.page.js');
const ThankYouPage = require('../../pages/thank-you.page.js');

describe('Feature: Calculated Summary', function() {

  describe('Given I have a Calculated Summary', function() {

    before('Get to Calculated Summary', function () {
      return helpers.openQuestionnaire('test_calculated_summary.json').then(() => {
        return browser
          .setValue(FirstNumberBlockPage.answer(), 1.23)
        .click(FirstNumberBlockPage.submit())

        .setValue(SecondNumberBlockPage.secondNumber(), 4.56)
        .setValue(SecondNumberBlockPage.secondNumberNotInTotal(), 7.89)
        .setValue(SecondNumberBlockPage.secondNumberAlsoInTotal(), 0.12)
        .click(SecondNumberBlockPage.submit())

        .setValue(ThirdNumberBlockPage.thirdNumber(), 3.45)
        .setValue(ThirdNumberBlockPage.thirdNumberNotInTotal(), 6.78)
        .click(ThirdNumberBlockPage.submit())

        .setValue(FourthNumberBlockPage.fourthNumber(), 9.01)
        .setValue(FourthNumberBlockPage.fourthNumberAlsoInTotal(), 2.34)
        .click(FourthNumberBlockPage.submit())

        .setValue(FifthNumberBlockPage.answer(), 5.67)
        .click(FifthNumberBlockPage.submit())

        .getUrl().should.eventually.contain(TotalPlaybackPage.pageName);
      });
    });

  it('Given I complete every question, When i get to the calculated summary, Then I should see the correct total', function() {
    return browser
      // Totals and titles should be shown
      .getText(TotalPlaybackPage.calculatedSummaryTitle()).should.eventually.contain('We calculate the total of values entered to be £20.71. Is this correct?')
      .getText(TotalPlaybackPage.calculatedSummaryQuestion()).should.eventually.contain('Grand total of previous values')
      .getText(TotalPlaybackPage.calculatedSummaryAnswer()).should.eventually.contain('£20.71')

      // Answers included in calculation should be shown
      .getText(TotalPlaybackPage.firstNumberAnswer()).should.eventually.contain('£1.23')
      .getText(TotalPlaybackPage.secondNumberAnswer()).should.eventually.contain('£4.56')
      .getText(TotalPlaybackPage.secondNumberAnswerAlsoInTotal()).should.eventually.contain('£0.12')
      .getText(TotalPlaybackPage.thirdNumberAnswer()).should.eventually.contain('£3.45')
      .getText(TotalPlaybackPage.fourthNumberAnswer()).should.eventually.contain('£9.01')
      .getText(TotalPlaybackPage.fourthNumberAnswerAlsoInTotal()).should.eventually.contain('£2.34')

      // Answers not included in calculation should not be shown
      .elements(TotalPlaybackPage.secondNumberAnswerNotInTotal()).then(result => result.value).should.eventually.be.empty
      .elements(TotalPlaybackPage.thirdNumberAnswerNotInTotal()).then(result => result.value).should.eventually.be.empty
      .elements(TotalPlaybackPage.fifthNumberAnswer()).then(result => result.value).should.eventually.be.empty;
    });

    it('Given change an answer, When i get to the calculated summary, Then I should see the new total', function() {
      return browser
        .click(TotalPlaybackPage.fourthNumberAnswerEdit())
        .setValue(FourthNumberBlockPage.fourthNumber(), 19.01)
        .setValue(FourthNumberBlockPage.fourthNumberAlsoInTotal(), 12.34)
        .click(FourthNumberBlockPage.submit())

        .click(FifthNumberBlockPage.submit())

        .getUrl().should.eventually.contain(TotalPlaybackPage.pageName)
        .getText(TotalPlaybackPage.calculatedSummaryTitle()).should.eventually.contain('We calculate the total of values entered to be £40.71. Is this correct?')
        .getText(TotalPlaybackPage.calculatedSummaryAnswer()).should.eventually.contain('£40.71');
    });

    it('Given I leave an answer empty, When i get to the calculated summary, Then I should see no answer provided and new total', function() {
      return browser
        .click(TotalPlaybackPage.fourthNumberAnswerEdit())
        .setValue(FourthNumberBlockPage.fourthNumber(), '')
        .setValue(FourthNumberBlockPage.fourthNumberAlsoInTotal(), '')
        .click(FourthNumberBlockPage.submit())

        .click(FifthNumberBlockPage.submit())

        .getUrl().should.eventually.contain(TotalPlaybackPage.pageName)
        .getText(TotalPlaybackPage.calculatedSummaryTitle()).should.eventually.contain('We calculate the total of values entered to be £9.36. Is this correct?')
        .getText(TotalPlaybackPage.calculatedSummaryAnswer()).should.eventually.contain('£9.36')
        .getText(TotalPlaybackPage.fourthNumberAnswer()).should.eventually.contain('No answer provided');
    });

    it('Given I confirm the total, When i get to the summary, Then I can complete the survey', function() {
      return browser
        .click(TotalPlaybackPage.submit())
        .getUrl().should.eventually.contain(SummaryPage.pageName)
        .click(SummaryPage.submit())
        .getUrl().should.eventually.contain(ThankYouPage.pageName);
    });

  });
});
