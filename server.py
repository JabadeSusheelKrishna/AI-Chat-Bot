from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import time

app = Flask(__name__)

# Sample messages to start with
messages = []

# Initializing Username
UserName = "uuu"

genai.configure(api_key='AIzaSyDn2cA_MQJ4_W0OrsVYtOHY8FqUt3atPGU')
model = genai.GenerativeModel(model_name="gemini-pro")
chat = model.start_chat()

def Gemini_Answer(user_msg):
    response = chat.send_message(user_msg)
    return response.text

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    global messages
    global UserName  # Ensure UserName is global
    global chat

    username = request.form['username']
    text = request.form['text']
    timestamp = f"{time.localtime().tm_hour}:{time.localtime().tm_min}"

    if UserName != username:
        UserName = username
        messages = []
        chat = model.start_chat()

    # Add the user message to the list
    new_message = {"username": username, "timestamp": timestamp, "text": text}
    messages.append(new_message)

    # Print message to terminal
    print(f'{username}: {text}')
    
    random_message = Gemini_Answer(text)

    random_message_data = {"username": "Gemini", "timestamp": timestamp, "text": random_message}
    messages.append(random_message_data)

    return jsonify(messages=messages)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
