from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from db import init_db, get_conn

app = FastAPI(title="Notes API")

# allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class NoteIn(BaseModel):
    title: str
    content: str

@app.on_event("startup")
def startup():
    init_db()

@app.get("/about", response_model=dict)
def about():
    return {"message": "This API demonstrates basic CRUD endpoints using FastAPI + SQLite."}

@app.get("/notes")
def list_notes():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM notes ORDER BY id DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]

@app.post("/notes", status_code=201)
def create_note(note: NoteIn):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO notes(title, content) VALUES(?, ?)", (note.title, note.content))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return {"id": new_id, "title": note.title, "content": note.content}

@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteIn):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE notes SET title=?, content=? WHERE id=?", (note.title, note.content, note_id))
    conn.commit()
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Note not found")
    conn.close()
    return {"id": note_id, "title": note.title, "content": note.content}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Note not found")
    conn.close()
    return {"deleted": note_id}
