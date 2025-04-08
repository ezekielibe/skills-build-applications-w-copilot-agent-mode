# Octofit Tracker

## Overview
The Octofit Tracker is a Django-based web application designed to help manage and track fitness activities for high school students. This application provides features for logging workouts, tracking progress, and managing user accounts.

## Project Structure
The project is organized as follows:

```
octofit-tracker/
└── backend/
    ├── octofit_tracker/          # Main Django project directory
    │   ├── __init__.py           # Marks the directory as a Python package
    │   ├── asgi.py                # ASGI configuration for handling asynchronous requests
    │   ├── settings.py            # Project settings and configuration
    │   ├── urls.py                # URL routing for the project
    │   └── wsgi.py                # WSGI configuration for serving HTTP requests
    ├── manage.py                   # Command-line utility for interacting with the project
    ├── apps/                       # Directory for Django apps
    │   └── tracker/               # Tracker app for managing fitness activities
    │       ├── __init__.py        # Marks the directory as a Python package
    │       ├── admin.py           # Admin site configuration for the tracker app
    │       ├── apps.py            # Tracker app configuration
    │       ├── migrations/         # Directory for database migrations
    │       │   └── __init__.py    # Marks the migrations directory as a Python package
    │       ├── models.py           # Data models for the tracker app
    │       ├── tests.py            # Test cases for the tracker app
    │       └── views.py            # View functions for handling requests
    └── requirements.txt            # List of project dependencies
```

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd octofit-tracker/backend
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

## Usage
Once the server is running, you can access the application at `http://127.0.0.1:8000/`. You can log in, create accounts, and start tracking fitness activities.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.