# Assignment Submission Portal

## Overview
The **Assignment Submission Portal** is a backend system that facilitates assignment uploads by users and allows admins to accept or reject them. It is built using **FastAPI** and **MongoDB**, ensuring a modular and maintainable architecture. The system includes authentication, role-based access, and comprehensive endpoints for both users and admins.

---

## Features
1. **User Functionality**:
   - Register and log in.
   - Upload assignments tagged to specific admins.
   - Fetch all available admins.

2. **Admin Functionality**:
   - Register and log in.
   - View assignments tagged to them.
   - Accept or reject assignments.

3. **Authentication**:
   - Secure JWT-based authentication for both users and admins.

---

## Requirements
- **Python** 3.9 or above
- **MongoDB** (Installed locally or hosted via MongoDB Atlas)
- **Dependencies**:
  - FastAPI
  - Uvicorn
  - PyMongo
  - Pydantic
  - Python-Jose
  - Passlib
  - python-decouple

---

## Setup Instructions
1. **Clone the Repository**:
```bash
git clone https://github.com/your-repo/assignment-portal.git cd assignment-portal
```

2. **Install Dependencies**:
```bash
pip install Uvicorn PyMongo Pydantic Python-Jose Passlib python-decouple
```

4. **Configure Environment Variables**:
- Create a `.env` file in the root directory with the following contents:

  (Insert environment variable configuration here)

- Replace `MONGO_URI` with your MongoDB connection string (local or hosted).

4. **Start MongoDB**:
- For local MongoDB:

  (Insert MongoDB start command here)

5. **Run the Server**:

```bash
uvicorn app.main:app --reload
```

The server will start on `http://127.0.0.1:8000`.

6. **Test the API**:
- Navigate to the automatically generated **API Documentation** at:
  - Swagger UI: `http://127.0.0.1:8000/docs`
  - ReDoc: `http://127.0.0.1:8000/redoc`

---

## How to Use the System

### 1. User Endpoints
#### Register
- **Endpoint**: `POST /user/register`
- **Payload**: 

 ```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

- **Response**:

```json
{
  "message": "User registered successfully"
}
```

#### Login
- **Endpoint**: `POST /user/login`
- **Payload**: 

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

- **Response**:

```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}

```

#### Upload Assignment
- **Endpoint**: `POST /user/upload`
- **Headers**: 

```json
{
  "Authorization": "Bearer your_jwt_token"
}
```

- **Payload**:

```json
{
  "task": "Hello World",
  "admin": "Alok"
}

```

- **Response**:

```json
{
  "message": "Assignment uploaded successfully",
  "user_id": "user@example.com"
}

```

#### Fetch All Admins
- **Endpoint**: `GET /user/admins`
- **Response**:

 ```json
[
  {
    "id": "admin_id_1",
    "name": "Alok"
  },
  {
    "id": "admin_id_2",
    "name": "Rita"
  }
]

 ```

---

### 2. Admin Endpoints
#### Register
- **Endpoint**: `POST /admin/register`
- **Payload**: 

 ```json
{
  "email": "admin@example.com",
  "password": "securepassword"
}
 ```

- **Response**:

 ```json
{
  "message": "Admin registered successfully"
}

 ```

#### Login
- **Endpoint**: `POST /admin/login`
- **Payload**: 

 ```json
{
  "email": "admin@example.com",
  "password": "securepassword"
}

 ```

- **Response**:

 ```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}

 ```

#### View Assignments
- **Endpoint**: `GET /admin/assignments`
- **Headers**: 

 ```json
{
  "Authorization": "Bearer your_jwt_token"
}

 ```

- **Response**:

 ```json
[
  {
    "id": "assignment_id_1",
    "user_id": "user@example.com",
    "task": "Hello World",
    "status": "pending",
    "created_at": "2024-11-17T10:45:00Z"
  }
]

```

#### Accept Assignment
- **Endpoint**: `POST /admin/assignments/{id}/accept`
- **Headers**: 

 ```json
{
  "Authorization": "Bearer your_jwt_token"
}

```

- **Response**:

 ```json
{
  "message": "Assignment accepted"
}

```

#### Reject Assignment
- **Endpoint**: `POST /admin/assignments/{id}/reject`
- **Headers**: 

```json
{
  "Authorization": "Bearer your_jwt_token"
}

```

- **Response**:

 ```json
{
  "message": "Assignment rejected"
}

```

---

## Future Improvements
- Add pagination for assignments.
- Integrate email notifications for assignment actions.
- Enhance security with role-based access control.
- Deploy to cloud platforms (e.g., AWS, Azure, or Heroku).

---

## License
This project is open-source and available under the MIT License. 

For any questions or suggestions, feel free to open an issue or contact the project maintainers.



