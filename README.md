# Reading Goal Tracker

## Description
This project helps users set and track annual/monthly reading goals and visualize their progress. Users can log books with dates and pages, see progress bars, and track weekly reading stats.

## Features
- Book logging with dates and pages
- Progress bar and weekly reading stats
- Timeline of completed books
- Optional Goodreads API integration

## Tech Stack
- Backend: Django, Django REST Framework
- Database: PostgreSQL
- Testing: pytest, pytest-django

## Project Structure

- reading_goal_tracker/ **_# Django main project_**
- books/ **_# Django app for books and reading goals_**
- manage.py **_# Django management script_**
- requirements.txt **_# Python dependencies_**
- .env **_# Environment variables_**

## Installation & Setup
1. Clone the repository:
```bash
git clone https://github.com/<your-username>/reading_project.git
cd reading_project
```

# Create a virtual environment:
```bash
python -m venv .venv
```
# Activate the virtual environment:
# On Windows (PowerShell):

```bash
.venv\Scripts\activate
```

# On Linux / macOS:
```bash
source .venv/bin/activate
```
# Install dependencies:
```bash
pip install -r requirements.txt
```
# Set environment variables in .env file (example):
```bash
DEBUG=True
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgres://user:password@localhost:5432/your_db_name
```
# Apply migrations:
```bash
python manage.py migrate
```
# Run the development server:
```bash
python manage.py runserver
```

# API Endpoints

## `/books/api/books/` - List and create books

## `/books/api/books/<id>/` - Retrieve, update, delete book

## `/books/api/users/` - List and retrieve users

# Running Tests
```bash
pytest
```