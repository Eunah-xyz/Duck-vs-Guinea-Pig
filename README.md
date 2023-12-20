# Duck vs Guinea Pig
A virtual play that generate a conversation between two ChatGPT instances.

One a aggressive duck that bullies the guinea pig.

The other one a frightened guinea pig that is afraid of the duck

## Requirements

- 2 OpenAI API keys
- create a Python virtual environment and `pip install -r requirements.txt`

## How to run

To use this script you need two (possibly from two different OpenAI accounts)  OpenAI API keys and you must set them as environment variables.

1. In command promt, while your virtual environment is activated, set your 2 key and 2 endpoint.

```bash
set AZURE_OPENAI_KEY_1=your_key_here
set AZURE_OPENAI_ENDPOINT_1=your_endpoint_here
set AZURE_OPENAI_KEY_2=your_key_here
set AZURE_OPENAI_ENDPOINT_2=your_endpoint_here
```

2. Run the flask app

```bash
flask run
```

3. Copy the local link and paste it in to your browser
4. Enjoy the conversation

