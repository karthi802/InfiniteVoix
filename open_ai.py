import openai
import speech_rec as sr

openai.api_key ="api key"



def processCommand(prompt):

    completion = openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages=[{"role":"user", "content":prompt}]
    )

    response =completion.choices[0].message.content
    print(response)
    return response