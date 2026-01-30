API Playground – Notes CRUD App

A small educational project to demonstrate how API endpoints connect the frontend, backend, and database using:

Frontend: HTML, CSS, JavaScript

Backend: Python FastAPI

Database: SQLite

This project is designed for teaching API concepts like:

GET

POST

PUT

DELETE
and how frontend and backend communicate.

Project Structure
api-playground/
│
├── backend/
│   ├── main.py
│   ├── db.py
│   ├── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── app.js
│
├── .gitignore
└── README.md

Features

Create notes

View all notes

Update notes

Delete notes

Swagger UI for API testing

Simple UI for frontend demo

API Endpoints
Method	Endpoint	Description
GET	/notes	Get all notes
POST	/notes	Create a new note
PUT	/notes/{id}	Update a note
DELETE	/notes/{id}	Delete a note
GET	/about	About this API
How Frontend & Backend Connect

Frontend sends request using fetch()

Backend receives it via FastAPI endpoint

Backend queries SQLite database

Backend returns JSON

Frontend displays result

Flow:

Browser → API → Database → API → Browser

Setup Instructions
1. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

2. Install backend dependencies
cd backend
pip install -r requirements.txt

3. Run backend server
uvicorn main:app --reload --port 8000


Open API docs:

http://127.0.0.1:8000/docs

4. Run frontend

Open this file in browser:

frontend/index.html

Demo Flow

Open /docs

Test GET → empty list

Test POST → create note

Test PUT → update note

Test DELETE → remove note

Open frontend → repeat same actions with UI

Git Ignore
venv/
*.db
__pycache__/

Teaching Use

This project is ideal for:

Explaining API endpoints

Showing frontend-backend flow

Demonstrating CRUD operations

Understanding HTTP methods
