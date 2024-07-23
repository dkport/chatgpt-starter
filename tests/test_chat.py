import unittest
from unittest.mock import patch, MagicMock
import os

from chat import Chat


class TestChat(unittest.TestCase):

    def setUp(self):
        """ Set up environment variable and patch the OpenAI client """
        os.environ['OPENAI_API_KEY'] = 'test_api_key'
        self.patcher = patch('chat.OpenAI')
        self.MockOpenAI = self.patcher.start()
        self.mock_client = MagicMock()
        self.MockOpenAI.return_value = self.mock_client
        self.chat = Chat()

    def tearDown(self):
        """ Stop patcher """
        self.patcher.stop()
        del os.environ['OPENAI_API_KEY']

    def test_get_client(self):
        """ Test get_client method """
        client = self.chat.get_client()
        self.assertEqual(client, self.mock_client)

    def test_extract_response(self):
        """ Test extract_response method """
        response = {
            "choices": [
                {
                    "message": {
                        "content": "Test response"
                    }
                }
            ]
        }
        self.assertEqual(self.chat.extract_response(response), "Test response")

    @patch('builtins.input', return_value='Test message')
    @patch('chat.Chat.extract_response', return_value='Test response')
    @patch('chat.Chat.side_effect')
    def test_send_request(self, mock_side_effect, mock_extract_response, mock_input):
        """ Test send_request method """
        self.mock_client.chat.completions.create.return_value.dict.return_value = {
            "choices": [
                {
                    "message": {
                        "content": "Test response"
                    }
                }
            ]
        }
        self.chat.send_request()
        self.assertEqual(self.chat.correspondence[0]["content"], 'Test message')
        self.assertEqual(self.chat.correspondence[1]["content"], 'Test response')
        mock_side_effect.assert_called_once_with('Test response')
        mock_extract_response.assert_called_once()


if __name__ == '__main__':
    unittest.main()

