import openai


class OpenAIContentGenerator:
    def __init__(self, api_key):
        """
        Initializes the essay generator with the given OpenAI API key.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_essay(self, user_input):
        """
        Generates an essay based on the user input provided.
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant to help write English essay."
                },
                {
                    "role": "user",
                    "content": user_input + " Please write an English essay based on the previous information."
                }
            ],
            temperature=0.2,
            max_tokens=200
        )
        return response["choices"][0]["message"]["content"]
