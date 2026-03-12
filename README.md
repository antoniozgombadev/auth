# Auth System (Flask + JWT)

Authentication system with Flask backend and React frontend.

This project demonstrates a simple authentication system using JSON Web Tokens (JWT) with a Flask API and a React frontend interface.

---

## Live Demo

Frontend
[https://your-auth-frontend.vercel.app](https://auth-frontend-mauve.vercel.app/)

Backend API
[https://your-auth-backend.onrender.com](https://auth-backend-uxw6.onrender.com)

---

## Features

* User login via web interface
* User registration via API (Postman)
* JWT authentication
* Protected API routes
* Password hashing
* Token validation

---

## Tech Stack

### Backend

* Python
* Flask
* JWT (JSON Web Token)
* SQLite
* REST API

### Frontend

* React
* React Router
* Fetch API

### Deployment

* Backend hosted on Render
* Frontend hosted on Vercel

---

## API Endpoints

### Register (Postman)

User registration is performed via API using Postman.

POST /register

Example request:

```
{
  "email": "test@email.com",
  "password": "password123"
}
```

---

### Login (Frontend)

POST /login

Example request:

```
{
  "email": "test@email.com",
  "password": "password123"
}
```

---

### Protected Route

GET /profile

Requires JWT token in Authorization header.

Example header:

```
Authorization: Bearer YOUR_JWT_TOKEN
```

---

## How to Run Locally

1. Clone repository

```
git clone [https://github.com/yourusername/auth-system.git](https://github.com/antoniozgombadev/auth.git)
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the application

```
python app.py
```

Server runs on:

```
http://localhost:5000
```

---

## Purpose

This project demonstrates backend authentication logic commonly used in modern web applications. It shows how to implement JWT-based authentication with protected routes using Flask and connect it with a React frontend.

## Preview

![LoginPage](./screenshots/login-page.png)
![Login-successful](./screenshots/login-successful.png)
![Postman](./screenshots/postman-register.png)
