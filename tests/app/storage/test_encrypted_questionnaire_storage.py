import unittest
import json
from jwcrypto import jwe
from jwcrypto.common import base64url_encode

from app.data_model.app_models import QuestionnaireState
from app.data_model.questionnaire_store import QuestionnaireStore
from app.storage import data_access
from app.storage.encrypted_questionnaire_storage import EncryptedQuestionnaireStorage
from tests.app.app_context_test_case import AppContextTestCase


class TestEncryptedQuestionnaireStorage(AppContextTestCase):

    def setUp(self):
        super().setUp()
        self.storage = EncryptedQuestionnaireStorage('user_id', 'user_ik', 'pepper')

    def test_encrypted_storage_requires_user_id(self):
        with self.assertRaises(ValueError):
            EncryptedQuestionnaireStorage(None, 'key', 'pepper')

    def test_encrypted_storage_requires_user_ik(self):
        with self.assertRaises(ValueError):
            EncryptedQuestionnaireStorage('1', None, 'pepper')

    def test_store_and_get(self):
        user_id = '1'
        user_ik = '2'
        encrypted = EncryptedQuestionnaireStorage(user_id, user_ik, 'pepper')
        data = 'test'
        encrypted.add_or_update(data, QuestionnaireStore.LATEST_VERSION)
        # check we can decrypt the data
        self.assertEqual(('test', QuestionnaireStore.LATEST_VERSION), encrypted.get_user_data())

    def test_store(self):
        data = 'test'
        self.assertIsNone(self.storage.add_or_update(data, QuestionnaireStore.LATEST_VERSION))
        self.assertIsNotNone(self.storage.get_user_data())  # pylint: disable=protected-access

    def test_get(self):
        data = 'test'
        self.storage.add_or_update(data, QuestionnaireStore.LATEST_VERSION)
        self.assertEqual((data, QuestionnaireStore.LATEST_VERSION), self.storage.get_user_data())

    def test_delete(self):
        data = 'test'
        self.storage.add_or_update(data, QuestionnaireStore.LATEST_VERSION)
        self.assertEqual((data, QuestionnaireStore.LATEST_VERSION), self.storage.get_user_data())
        self.storage.delete()
        self.assertEqual((None, None), self.storage.get_user_data())  # pylint: disable=protected-access


class TestLegacyEncryptedQuestionnaireStorage(AppContextTestCase):
    """Compression didn't used to be applied to the questionnaire store data. It also
    used to be base64-encoded. For performance reasons the base64 encoding was removed
    and compression applied using the snappy lib
    """
    def setUp(self):
        super().setUp()
        user_id = 'user_id'
        self.storage = EncryptedQuestionnaireStorage(user_id, 'user_ik', 'pepper')
        self._save_legacy_state_data(user_id, 'test')

    def test_get(self):
        """Tests that the legacy data is correctly decrypted
        """
        data = 'test'
        self.assertEqual((data, QuestionnaireStore.LATEST_VERSION), self.storage.get_user_data())

    def _save_legacy_state_data(self, user_id, data):
        protected_header = {
            'alg': 'dir',
            'enc': 'A256GCM',
            'kid': '1,1',
        }

        jwe_token = jwe.JWE(
            plaintext=base64url_encode(data),
            protected=protected_header,
            recipient=self.storage.encrypter.key
        )

        legacy_state_data = json.dumps({'data': jwe_token.serialize(compact=True)})

        questionnaire_state = QuestionnaireState(
            user_id,
            legacy_state_data,
            QuestionnaireStore.LATEST_VERSION
        )
        data_access.put(questionnaire_state)

if __name__ == '__main__':
    unittest.main()
