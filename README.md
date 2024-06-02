# Flask To-Do Application

This is a simple To-Do application built with Flask and SQLAlchemy. It allows users to add, update, and delete to-do items. Each to-do item has a title, description, and an optional deadline.

## Features

- Add new to-do items with a title, description, and optional deadline.
- View all to-do items on the home page.
- Update existing to-do items.
- Delete to-do items.

## Installation

### Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy

### Step-by-Step Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/flask-todo-app.git
   cd flask-todo-app
   ```
2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```
3. **Activate the virtual environment:**

   ```bash
   venv\Scripts\activate
   ```
4. **On macOS/Linux**

   ```bash
   source venv/bin/activate
   ```

5. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```
6. **Run application**
   ```bash
   python app.py
   ```

flask-todo-app/
│
├── app.py                 # Main application file
├── templates/
│   ├── home.html          # Home page template
│   ├── add.html           # Add to-do template
│   └── update.html        # Update to-do template
├── requirements.txt       # List of dependencies
└── README.md              # This file
