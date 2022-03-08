# Empathetic Chatbot API

This is the API to which each of the frontends will make requests

## Configuration steps

```bash
cp ./secret/.env.example ./secret/.env
```

Then, replace the `OPENAI_KEY` value with your OpenAI Key, and the `SESSION_KEY` value with password string, in `secret/.env`.

## Running the server

To run the server locally on Linux/Mac:

```bash
PORT=3000 gunicorn wsgi:app
```

On Windows:

```bash
waitress-serve --port 3000 wsgi:app
```

## Making requests to the server

The server accepts HTTP GET requests of the form:
```
<server>/question?q=<QUESTION>
```

where `<QUESTION>` is the question being asked.

It also accepts websocket requests, listening to the `question` event, where the payload is the string containing the question being asked.
