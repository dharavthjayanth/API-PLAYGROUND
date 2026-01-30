const API = "http://127.0.0.1:8000";

const noteId = document.getElementById("noteId");
const title = document.getElementById("title");
const content = document.getElementById("content");
const notesDiv = document.getElementById("notes");
const output = document.getElementById("output");

const show = (data) => output.textContent = JSON.stringify(data, null, 2);

async function refresh() {
  const res = await fetch(`${API}/notes`);
  const data = await res.json();
  show(data);

  notesDiv.innerHTML = "";
  data.forEach(n => {
    const el = document.createElement("div");
    el.className = "note";
    el.innerHTML = `
      <div class="top">
        <h3>#${n.id} — ${n.title}</h3>
        <button data-id="${n.id}">DELETE</button>
      </div>
      <p>${n.content}</p>
    `;
    el.querySelector("button").onclick = () => del(n.id);
    el.onclick = (e) => {
      if (e.target.tagName.toLowerCase() === "button") return;
      noteId.value = n.id;
      title.value = n.title;
      content.value = n.content;
    };
    notesDiv.appendChild(el);
  });
}

async function createNote() {
  const res = await fetch(`${API}/notes`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ title: title.value, content: content.value })
  });
  const data = await res.json();
  show(data);
  await refresh();
}

async function updateNote() {
  if (!noteId.value) return show({error: "Provide Note ID to update"});
  const res = await fetch(`${API}/notes/${noteId.value}`, {
    method: "PUT",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ title: title.value, content: content.value })
  });
  const data = await res.json();
  show(data);
  await refresh();
}

async function del(id) {
  const res = await fetch(`${API}/notes/${id}`, { method: "DELETE" });
  const data = await res.json();
  show(data);
  await refresh();
}

document.getElementById("refreshBtn").onclick = refresh;
document.getElementById("createBtn").onclick = createNote;
document.getElementById("updateBtn").onclick = updateNote;

refresh();
