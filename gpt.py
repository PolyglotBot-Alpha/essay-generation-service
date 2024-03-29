import openai


# Used to ask general question in this task
class OpenAIContentGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def gpt_generate_essay(self, user_input):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant to help write English essay."
                    # can be changed to other system message
                },
                {
                    "role": "user",
                    "content": user_input + " Please write an English essay based on the previous information."
                }
            ],

            # temperature is used to adjust the innovativeness.
            # It ranges from 0 to 1. 0 means most confidence, 1 means most innovativeness.
            temperature=0.2,
            max_tokens=200
        )

        return response["choices"][0]["message"]["content"]  # return the output from gpt
