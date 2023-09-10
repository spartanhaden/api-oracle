#!/usr/bin/env python3

import os

from dotenv import load_dotenv


import openai


# load from dotenv
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = openai_api_key


system_prompt = "You are GPT4 and help people with coding. there are also some docs available for hnswlib here\n"


# read the hnswlib_docs.json
with open("hnswlib_docs.json", "r") as f:
    hnswlib_docs = f.read()

    system_prompt += hnswlib_docs


while True:
    user_prompt = input("Enter your prompt: ")

    chat_completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
        # {"role": "assistant", "content": "bleep"},
        # {"role": "user", "content": "bloop"}
    ]
)

    product_names = chat_completion["choices"][0]["message"]["content"]
    print()
    print("response:")
    print()
    print(product_names)
    print()
    print()