# Group Project Web Client

A simple web-based chat box to interface with the API

## Running the client

The following command will run the client locally, and the client will find the question server running at `http://localhost:3000`
```bash
npm run local
```

On the other hand, the following command will run the client locally, and the client will find the question server running at `http://groupcharlie.soc.srcf.net:3000/`.
```bash
npm start
```

To build a docker image of the client:
```bash
docker build -t group-project-webclient .
```

To run this image:

``bash
docker run -p 8000:8000 -it group-project-webclient
```