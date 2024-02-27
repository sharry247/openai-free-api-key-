
---

# Generative AI Chat Server

This project demonstrates how to create a Flask server that interacts with a generative AI model provided by Google's Generative AI service. It allows you to send prompts to the model and receive responses.

## Prerequisites

Before running this project, you need to have Python installed on your system. You also need to have Flask and the `google.generativeai` package installed. You can install them using pip:

```
pip install Flask google-generativeai
```

## Configuration

You need to configure the generative AI model by providing your API key. Replace `"YOUR_API_KEY"` with your actual API key.

```python
genai.configure(api_key="YOUR_API_KEY")
```

## Starting the Server

To start the Flask server, run the `server.py` script:

```
python server.py
```

The server will start on `http://localhost:5850`.

## Sending Requests

You can send POST requests to the `/v1/completions` endpoint with a JSON payload containing a prompt. The server will respond with a JSON object containing the generated text.

Example:

```json
{
  "prompt": "Hello, how are you?"
}
```

## Modifying OpenAI Package

If you want to use OpenAI's package to interact with the server, you need to modify the package to point to your local server. Update `openai.api_base` with the URL of your Flask server.

```python
openai.api_base = 'http://localhost:5850/v1/'
```

## Running OpenAI Requests

You can now use the OpenAI package as usual to interact with your local server. Here's an example:

```python
response = openai.Completion.create(
    model="text-davinci-002",
    prompt="Hello, how are you?",
    max_tokens=10
)

print(response)
```

## Notes

- Make sure to replace `"YOUR_API_KEY"` with your actual API key.
- This project is for demonstration purposes and may require further customization for production use.

