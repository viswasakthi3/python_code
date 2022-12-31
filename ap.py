from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Comment(BaseModel):
    id: int
    parent_id: Optional[int] = None
    content: str
    upvotes: int
    downvotes: int

class Reply(BaseModel):
    id: int
    parent_id: int
    content: str
    upvotes: int
    downvotes: int

@app.on_event("startup")
def startup():
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY, parent_id INTEGER, content TEXT, upvotes INTEGER, downvotes INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS replies (id INTEGER PRIMARY KEY, parent_id INTEGER, content TEXT, upvotes INTEGER, downvotes INTEGER)''')
    conn.commit()
    conn.close()

@app.post("/comments")
def create_comment(comment: Comment):
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    c.execute("INSERT INTO comments (id, parent_id, content, upvotes, downvotes) VALUES (?, ?, ?, ?, ?)", (comment.id, comment.parent_id, comment.content, comment.upvotes, comment.downvotes))
    conn.commit()
    conn.close()
    return comment

@app.put("/comments/{id}")
def update_comment(id: int, comment: Comment):
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    c.execute("UPDATE comments SET content = ?, upvotes = ?, downvotes = ? WHERE id = ?", (comment.content, comment.upvotes, comment.downvotes, id))
    conn.commit()
    conn.close()

@app.get("/comments/{id}")
def get_comment(id: int):
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    c.execute("SELECT * FROM comments WHERE id = ?", (id,))
    comment = c.fetchone()
    conn.close()
    if comment:
        return Comment(**dict(comment))
    raise HTTPException(status_code=404, detail="Comment not found")

@app.post("/comments/{parent_id}/replies")
def create_reply(parent_id: int, reply: Reply):
    conn = sqlite3.connect('comments.db')
    c = conn.cursor()
    c.execute("INSERT INTO replies (id, parent_id, content, upvotes, downvotes) VALUES (?, ?, ?, ?, ?)", (reply.id, reply.parent_id, reply.content, reply.upvotes, reply.downvotes))
    conn.commit()
   
