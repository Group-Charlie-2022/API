# Group Project Discord Bot

A discord bot to take messages from a discord channel and send them to the API

## Running the client

The following command will run the bot locally, and the bot will find the question server running at `http://localhost:3000`
```bash
npm run local
```

On the other hand, the following command will run the bot locally, and the client will find the question server running at `http://groupcharlie.soc.srcf.net:3000/`.
```bash
npm start
```

To build a docker image of the bot:
```bash
docker build -t group-project-discord-bot .
```

To run this image:

``bash
docker run -it group-project-discord-bot
```