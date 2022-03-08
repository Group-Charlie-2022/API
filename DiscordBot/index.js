`use strict`
require("dotenv").config({ path: process.env.LOCAL ? "./env/local.env" : "./env/remote.env" });
require("dotenv").config({ path: "./env/secret.env" });
console.log(`Finding server at ${process.env.QUESTION_SERVER_URL}`)

const { Client, Intents } = require("discord.js");
const axios = require("axios");

const client = new Client({
    intents: [
        Intents.FLAGS.GUILDS,
        Intents.FLAGS.GUILD_MESSAGES
    ]
});

client.once("ready", (c) => {
    console.log(`Logged in as ${c.user.tag}!`);
});

client.on("messageCreate", async (msg) => {
    if (msg.author.id === client.user.id) return;
    if (msg.channel.id === process.env.CHANNEL_ID) {
        try {
            const response = await axios.request({
                baseURL: process.env.QUESTION_SERVER_URL,
                url: "/question",
                params: {
                    q: msg.content
                }
            });
            msg.reply(response.data);
        } catch {
            msg.reply("Couldn't connect to question server :(");
        }
    }
});

client.login(process.env.CLIENT_TOKEN);


