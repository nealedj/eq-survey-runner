from flask import render_template, session
from flask_login import login_required, current_user
from .. import main_blueprint
import logging
from app.main.views.root import load_and_parse_schema, redirect_to_location
from app.submitter.converter import SubmitterConstants

from datetime import datetime


logger = logging.getLogger(__name__)


@main_blueprint.route('/landing-page', methods=['GET', 'POST'])
@login_required
def landing_page():
    # Redirect to thank you page if the questionnaire has already been submitted
    if SubmitterConstants.SUBMITTED_AT_KEY in session:
        return redirect_to_location("submitted")

    logger.debug("Requesting landing page")
    eq_id = current_user.get_eq_id()
    form_type = current_user.get_form_type()
    logger.debug("Requested questionnaire %s for form type %s", eq_id, form_type)

    questionnaire = load_and_parse_schema()

    return render_template('landing-page.html', data={
        "legal": questionnaire.introduction.legal,
        "description": questionnaire.introduction.description,
        "address": {
            "name": current_user.get_ru_name(),
            "trading_as": current_user.get_trad_as()
        },
        "survey_code": questionnaire.survey_id,
        "period_str": current_user.get_period_str(),
        "respondent_id": current_user.get_ru_ref(),
        # You'd think there would be an easier way of doing this...
        "return_by": '{dt.day} {dt:%B} {dt.year}'.format(dt=datetime.strptime(current_user.get_return_by(), "%Y-%m-%d")),
        "start_date": '{dt.day} {dt:%B} {dt.year}'.format(dt=datetime.strptime(current_user.get_ref_p_start_date(), "%Y-%m-%d")),
        "end_date": '{dt.day} {dt:%B} {dt.year}'.format(dt=datetime.strptime(current_user.get_ref_p_end_date(), "%Y-%m-%d"))
    })