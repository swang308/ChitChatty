# app.py

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_message = request.form.get('Body')
    if not incoming_message:
        return 'No message received', 400

    # Call OpenAI API to get a response
    openai_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a generous boyfriend or girlfriend. Give support and guidance to the user."},
            {"role": "user", "content": incoming_message},
        ]
    )

    # Extract the GPT response
    response_message = openai_response.choices[0].message.content

    # Respond via Twilio
    twilio_response = MessagingResponse()
    twilio_response.message(response_message)

    return str(twilio_response)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
