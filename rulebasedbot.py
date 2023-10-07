
import openai
openai.api_key=("paste your api key here")
print("Hello, How can I help you\n")
text=""
while(text!="exit"):
  text = input("\n")
  response=openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {
              "role": "system",
              "content":"You will be asked certain queries regarding codsoft which is an internship platform and you have to answer."
          },
          {
              "role": "user",
              "content":text
          }
        ],
      temperature=0,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
  )
  #print(response)
  generated_text=response.choices[0].message.content.strip()
  print(generated_text)

