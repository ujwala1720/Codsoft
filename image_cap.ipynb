import openai
import cv2

openai.api_key = "paste your api key here"

print("Hello, How can I help you\n")

while True:
    user_input = input("Enter an image file path or type 'exit' to quit: ")

    if user_input.lower() == "exit":
        break

    try:
        img = cv2.imread(user_input)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "you have to caption the image that is provided by the user"
                },
                {
                    "role": "user",
                    "content": user_input  # Send the user's image input here
                }
            ],
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        generated_text = response['choices'][0]['message']['content']
        print("Generated Caption:", generated_text)

    except Exception as e:
        print("Error:", str(e))

