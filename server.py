from flask import Flask, jsonify, request
import google.generativeai as genai

# Configure the generative AI model
genai.configure(api_key="your-google-api-key-of-gemini-pro-model")
model = genai.GenerativeModel('gemini-pro')
chatt = model.start_chat()

app = Flask(__name__)

@app.route('/v1/completions', methods=['POST'])
def completions():
    # Get JSON data from the request
    data = request.get_json()

    # Extract parameters from the JSON data
    prompt = data.get('prompt')

    # Send message to the conversational model
    chattt = chatt.send_message(prompt)

    # Extract the response message from the model's response object
    response = chattt.text

    # Return the response as JSON
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5850)
