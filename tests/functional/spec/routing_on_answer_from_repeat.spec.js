const helpers = require('../helpers');

const PrimaryNamePage = require('../pages/surveys/routing_on_answer_from_driving_repeating_group/primary-name-block.page.js');
const PrimaryLiveHereBlockPage = require('../pages/surveys/routing_on_answer_from_driving_repeating_group/primary-live-here-block.page.js');
const RepeatingNamePage = require('../pages/surveys/routing_on_answer_from_driving_repeating_group/repeating-name-block.page.js');
const RepeatingAnyoneElsePage = require('../pages/surveys/routing_on_answer_from_driving_repeating_group/repeating-anyone-else-block.page.js');
const SexPage = require('../pages/surveys/routing_on_answer_from_driving_repeating_group/sex-block.page.js');
const SexNoPrimaryPage = require('../pages/surveys/routing_on_answer_from_driving_repeating_group/sex-block-no-primary.page.js');
const RelationshipsPage = require('../pages/surveys/routing_on_answer_from_driving_repeating_group/relationships.page.js');
const RelationshipsNoPrimaryPage = require('../pages/surveys/routing_on_answer_from_driving_repeating_group/relationships-no-primary.page.js');
const SummaryPage = require('../pages/surveys/routing_on_answer_from_driving_repeating_group/summary.page.js');

describe('Routing on Answer from repeat', function() {

  it('Given I am completing a survey where I dont live in the house, When I select I dont live here, Then I should not be asked questions about myself', function() {

    return helpers.openQuestionnaire('test_routing_on_answer_from_driving_repeating_group.json').then(() => {

      return browser
        .setValue(PrimaryNamePage.answer(), 'Bob')
        .click(PrimaryNamePage.submit())

        .click(PrimaryLiveHereBlockPage.no())
        .click(PrimaryLiveHereBlockPage.submit())

        .click(RepeatingAnyoneElsePage.yes())
        .click(RepeatingAnyoneElsePage.submit())

        .setValue(RepeatingNamePage.answer(), 'Alice')
        .click(RepeatingNamePage.submit())

        .click(RepeatingAnyoneElsePage.yes())
        .click(RepeatingAnyoneElsePage.submit())

        .setValue(RepeatingNamePage.answer(), 'Jamie')
        .click(RepeatingNamePage.submit())

        .click(RepeatingAnyoneElsePage.no())
        .click(RepeatingAnyoneElsePage.submit())

        .click(RelationshipsNoPrimaryPage.relationship(0, 'Husband or wife'))
        .click(RelationshipsNoPrimaryPage.submit())

        .getText(SexNoPrimaryPage.questionText()).should.eventually.contain('Alice')
        .click(SexNoPrimaryPage.female())
        .click(SexNoPrimaryPage.submit())

        .getText(SexNoPrimaryPage.questionText()).should.eventually.contain('Jamie')
        .click(SexNoPrimaryPage.male())
        .click(SexNoPrimaryPage.submit())

        .getUrl().should.eventually.contain(SummaryPage.pageName)
        .click(SummaryPage.submit());
    });
  });

});

