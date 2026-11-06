# Student Management System

A web-based Student Management System built using Python, Flask, SQLite, HTML and CSS.

This project is being developed incrementally to practise real-world software engineering concepts and backend development.

## Current Version: V3

### Features

#### V1 - Student Management

- Add student records
- View student records
- Edit student details
- Delete student records

#### V2 - Search and Pagination

- Search by name, roll number, department and email
- Pagination
- Form validation
- Success and error notifications

#### V3 - Authentication and Authorization

- Admin login
- Student login
- Password hashing
- Flask session management
- Role-Based Access Control (RBAC)
- CSRF protection
- Admin-only student management
- Admin-created student accounts
- Separate student dashboard

## Technology Stack

- Python
- Flask
- SQLite
- HTML
- CSS
- Werkzeug
- Flask-WTF

## Project Structure

```text
student-management-system/
├── app.py
├── create_admin.py
├── requirements.txt
├── templates/
├── static/
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/teja-787/student-management-system
```

2. Navigate into the project:

```bash
cd student-management-system
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate it:

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Set your Flask secret key:

```powershell
$env:FLASK_SECRET_KEY="your-secret-key"
```

7. Create an administrator account:

```bash
python create_admin.py
```

8. Run the application:

```bash
python app.py
```

9. Open:

http://127.0.0.1:5000/login

## Future Improvements

- Attendance management
- Course management
- Examination and grading
- Analytics dashboard
- REST APIs
- Automated testing
- Deployment

## Project Status

Under active development.
