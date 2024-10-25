# Todo App

A simple web application for managing tasks and to-do lists. Users can add, edit, and delete tasks, helping them stay organized and productive.

---

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Requirements

- Python 3.8+
- Django 3.2+
- SQLite (default database, can be configured for others)
- Other dependencies listed in `requirements.txt`

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/todo-app.git
cd todo-app
python3 -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

```bash
SECRET_KEY=your-secret-key
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit http://localhost:8000 in your browser
