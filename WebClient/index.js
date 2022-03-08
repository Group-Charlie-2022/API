`use strict`
require("dotenv").config({ path: process.env.LOCAL ? "./env/local.env" : "./env/remote.env" });
console.log(`Finding server at ${process.env.QUESTION_SERVER_URL}`)

const express = require("express");
const app = express();
const port = process.env.PORT || 8000;

app.get("/config.js", (_, res) => {
    res.send(`const CONFIG = ${JSON.stringify({
        questionServerURL: process.env.QUESTION_SERVER_URL
    })}`);
});

app.use("/", express.static("./frontend"));

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});