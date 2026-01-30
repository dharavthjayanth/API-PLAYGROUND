# API Playground – Learn API Endpoints (CRUD Demo)

This project is a simple educational web app that helps students understand:
  What an API endpoint is
  How Frontend → Backend → Database works
  How GET, POST, PUT, DELETE methods behave

Built using:
  Frontend: HTML, CSS, JavaScript
  Backend: Python (FastAPI)
  Database: SQLite

#  How Everything Is Connected

User (Browser)
      ↓
Frontend (HTML + JS)
      ↓ fetch()
Backend API (FastAPI)
      ↓ SQL
SQLite Database
      ↑
Backend sends JSON
      ↑
Frontend displays data

#  API Endpoints
| Method | Endpoint    | What it does      |
| ------ | ----------- | ----------------- |
| GET    | /notes      | Get all notes     |
| POST   | /notes      | Create a new note |
| PUT    | /notes/{id} | Update a note     |
| DELETE | /notes/{id} | Delete a note     |
| GET    | /about      | API description   |

# How the Code Works




