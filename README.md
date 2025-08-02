# Job-Portal-Web-Application

## 📌 Features

### 👤 User Features:
- Sign up and log in securely
- View and edit user profile
- Browse job listings
- Filter jobs by title, location, salary, etc.
- Apply to jobs

### 🧑‍💼 Admin/Recruiter Features:
- Add/edit/delete job listings
- View applicants per job
- Contact users via email

  Tech Stack

| Frontend   | Backend  | Database | Others |
|------------|----------|----------|--------|
| HTML/CSS   | Django   | SQLite3  | Bootstrap (optional) |
| JavaScript | Python   |          | Pillow (for image handling) |

 🗂️ Project 

1)Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

2)Install Requirements
pip install -r requirements.txt

3)Run Migrations
python manage.py makemigrations
python manage.py migrate

4)Create Superuser
python manage.py createsuperuser

5)Run Development Server
python manage.py runserver

6)Open in Browser
http://127.0.0.1:8000/
