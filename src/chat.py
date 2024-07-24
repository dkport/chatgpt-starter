import os
import sys

from openai import OpenAI


class Chat:
    """ Basic operations with ChatGPT """
    
    def __init__(self):
        self.client = self.get_client()
        self.correspondence = []

    def send_request(self):
        """ Send a request to ChatGPT """

        try:
            message = input("\n>> Your message: ")
        except:
            sys.exit(0)

        self.correspondence.append(
            {
                "role": "user",
                "content": message
            }
        )
        raw_response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=self.correspondence,
            temperature=0
        )
        clean_answer = self.extract_response(raw_response.dict())
        self.side_effect(clean_answer)
        self.correspondence.append(
            {
                "role": "assistant",
                "content": clean_answer
            }
        )

    def run(self):
        """ Run program workflow """
        while True:
            self.send_request()
            print("\nPress CTRL + C to finish the app.\n")

    @staticmethod
    def side_effect(text):
        """ Action with the reply """
        print(f"\n<< Reply: {text}")

    @staticmethod
    def extract_response(response):
        """ Get response content """
        return response["choices"][0]["message"]["content"]

    @staticmethod
    def get_client():
        """ Get API key from environment """
        if "OPENAI_API_KEY" not in os.environ:
            quit_or_error("OPENAI_API_KEY is not set in the env. Quiting...")
        return OpenAI()
