const chatBox = document.getElementById("chat-box");

const input = document.getElementById("message");

const button = document.getElementById("send");

function addMessage(sender, text, isUser) {
  const row = document.createElement("div");

  row.className = isUser ? "flex justify-end" : "flex justify-start";

  const bubble = document.createElement("div");

  bubble.className = isUser
    ? "bg-blue-600 text-white px-4 py-3 rounded-2xl max-w-md"
    : "bg-slate-700 text-white px-4 py-3 rounded-2xl max-w-md";

  bubble.innerHTML = `<b>${sender}</b><br>${text}`;

  row.appendChild(bubble);

  chatBox.appendChild(row);

  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
  const message = input.value.trim();

  if (message === "") return;

  addMessage("You", message, true);

  input.value = "";

  const loading = document.createElement("div");

  loading.className = "text-slate-400";

  loading.innerText = "Gemini is typing...";

  chatBox.appendChild(loading);

  const response = await fetch("/chat", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      message: message,
    }),
  });

  const data = await response.json();

  loading.remove();

  addMessage("Gemini", data.reply, false);
}

button.onclick = sendMessage;

input.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    sendMessage();
  }
});
