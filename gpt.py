import openai

openai.api_key = "" # add API key here

# Used to ask general question in this task

def gpt_generate_essay(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {
            "role": "system",
            "content": "You are an assistant to help write English essay." # can be changed to other system message
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
    # print(response["choices"][0]["message"]["content"])
    return response["choices"][0]["message"]["content"] # return the output from gpt



gpt_generate_essay("我想写一篇关于美国文化的文章。")