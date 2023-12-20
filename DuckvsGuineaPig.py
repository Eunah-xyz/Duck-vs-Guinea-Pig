import openai
from openai import AzureOpenAI
import time
import os
from os import system


client1 = AzureOpenAI(
    api_key = os.getenv("AZURE_OPENAI_KEY_1"),
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT_1"),
    api_version = "2023-12-01-preview"
)

client2 = AzureOpenAI(
    api_key = os.getenv("AZURE_OPENAI_KEY_2"),
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT_2"),
    api_version = "2023-12-01-preview"
)


def conversation(input_text, duck):

    if(duck):
        current_client = client1
        current_content = "Think and write as a aggressive duck that bullied the guinea pig in short sentence. Start and finish your answer with Quack Quack"

    else:
        current_client = client2
        current_content = "Think and write as a frightened guinea pig that is afraid of the duck in short sentence. Start and finish your answer with Pui Pui"


    message = input_text

    response = current_client.chat.completions.create(
        model="GPT-4",
        messages= [
            {"role": "system", "content": current_content},
            {"role": "assistant", "content": message}
        ],
        presence_penalty=0.5,
    )

    input_text = response.choices[0].message.content

    return [response.choices[0].message.content]




