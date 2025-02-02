import os
import google.generativeai as genai

genai.configure(api_key=["AIzaSyAooNcS_-7pgX0JbX4rAc3p1pr5ryHJUOQ"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "What is bigger, 9.9 or 9.11?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "9.9 is **bigger** than 9.11. \n\nThink of it like money. 9.90 is nine dollars and ninety cents, while 9.11 is nine dollars and eleven cents.\n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)