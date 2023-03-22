
import openai
openai.api_key = "sk-WSZEsRSwl5SoJKXGX3thT3BlbkFJ>

while True:
    model = "text-davinci-003"
    user = input("Enter your Quation here ==> ")
    if "exit" in user:
        break

    completion = openai.Completion.create(model =>
      prompt = user,
      max_tokens = 1024,
      temperature = 0.5,
      n = 1,
      stop = None )

    response = completion.choices[0].text
    print (response)