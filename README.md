# Empathetic Chatbot API

This is the API to which each of the frontends will make requests

## Running the server

To run the server locally:

```bash
python3.9 server.py
```

To build a docker image of the server:

```bash
docker build -t group-project-api .
```

To run that docker image:
```bash
docker run -p 3000:3000 -it group-project-api
```

## Making requests to the server

The server accepts HTTP GET requests of the form:
```
<server>/question?q=<QUESTION>
```

where `<QUESTION>` is the question being asked.

It also accepts websocket requests, listening to the `question` event, where the payload is the string containing the question being asked.