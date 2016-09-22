from tests.integration.integration_test_case import IntegrationTestCase
from tests.integration.create_token import create_token

class TestInformationPage(IntegrationTestCase):

    def test_information_page(self):

        resp = self.client.get('/information/multiple-surveys', follow_redirects=False)
        content = resp.get_data(True)
        self.assertRegexpMatches(content, 'Information')
        self.assertRegexpMatches(content, 'Unfortunately you can only complete one survey at a time.')
        self.assertRegexpMatches(content, 'Close this window to continue with your current survey.')

    def test_information_page_missing_message(self):

        resp = self.client.get('/information/test', follow_redirects=False)
        self.assertEquals(resp.status_code, 404)

    def test_different_metadat_store_to_url(self):
        # Get a token for the first questionnaire
        token = create_token('0205', '1')
        response1 = self.client.get('/session?token=' + token.decode(), follow_redirects=True)
        self.assertEquals(response1.status_code, 200)

        content1 = response1.get_data(True)

        self.assertRegexpMatches(content1, '<title>Introduction</title>')
        self.assertRegexpMatches(content1, '>Get Started<')
        self.assertRegexpMatches(content1, 'Monthly Business Survey - Retail Sales Index')

        # Open up a second questionnaire
        token = create_token('star_wars', '0')
        response2 = self.client.get('/session?token=' + token.decode(), follow_redirects=True)
        self.assertEquals(response2.status_code, 200)

        content2 = response2.get_data(True)

        self.assertRegexpMatches(content2, '<title>Introduction</title>')
        self.assertRegexpMatches(content2, '>Get Started<')
        self.assertRegexpMatches(content2, 'Star Wars')

        # We try to post to the wrong questionnaire
        post_data = {
            'action[start_questionnaire]': 'Start Questionnaire'
        }
        response = self.client.post('/questionnaire/1/0203/201604/789/introduction', data=post_data, follow_redirects=True)
        content = response.get_data(True)
        self.assertRegexpMatches(content, 'Information')
        self.assertRegexpMatches(content, 'Unfortunately you can only complete one survey at a time.')
        self.assertRegexpMatches(content, 'Close this window to continue with your current survey.')


