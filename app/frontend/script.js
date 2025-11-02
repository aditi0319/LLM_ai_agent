document.getElementById("send-btn").addEventListener("click", async () => {
  const query = document.getElementById("user-input").value.trim();
  if (!query) return alert("Please type your query!");

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class="user">🧑‍💬 ${query}</div>`;

  try {
    const response = await fetch("http://127.0.0.1:8000/tickets/classify", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });

    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

    const data = await response.json();
    console.log("DEBUG RESPONSE:", data);

    const category = data.predicted_category || "Unknown";
    const solution = data.solution || "No response generated.";
    chatBox.innerHTML += `<div class="bot typing">🤖 Typing...</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

const typingDiv = document.querySelector(".typing");

setTimeout(() => {
  typingDiv.remove();
    chatBox.innerHTML += `
      <div class="bot">
        🧭 <b>Category:</b> ${category}<br>
        💡 <b>Solution:</b> ${solution}
      </div>
    `;
    chatBox.scrollTop = chatBox.scrollHeight;
},800)

  } catch (err) {
    chatBox.innerHTML += `<div class="error">Error: ${err.message}</div>`;
  }

  document.getElementById("user-input").value = "";
});
