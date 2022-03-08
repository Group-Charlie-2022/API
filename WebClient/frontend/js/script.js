let socket = io(CONFIG.questionServerURL);

socket.on("connection", () => {
    console.log("Connected to socket");
});

socket.on("answer", (payload) => {
    addMessageToChat("Chatbot", payload);
});

function validateMessage() {
    const textBox = document.querySelector("#text-box");
    const valid = !!textBox.value;
    document.querySelector("#send-button").disabled = !valid;
}

async function sendMessage(event) {
    event.preventDefault();
    const textBox = document.querySelector("#text-box");

    addMessageToChat("You", textBox.value);
    socket.emit("question", textBox.value);

    textBox.value = "";
}

function addMessageToChat(sender, body) {
    const chat = document.querySelector("#chat");
    const template = document.querySelector("#message-template");
    const messageDiv = template.cloneNode(true);
    messageDiv.id = "";
    messageDiv.querySelector(".sender").innerText = sender;
    messageDiv.querySelector(".body").innerText = body;
    chat.appendChild(messageDiv);
}