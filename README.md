# Farm_Management_Dashboard
This application will be used by the modern farmers if they want to keep track of their crops, financial states and also to get live weather feedbacks.

## Frontend Setup
# Clone the repository
git clone https://github.com/yourusername/projectname.git

# Navigate to the project directory
cd projectname

# Install dependencies
npm install

# Start the development server
npm start


## Backend Setup

This section provides instructions on how to set up and run the Django backend for the project.

### Prerequisites

Before you begin, ensure you have Python installed on your system. The project is tested with Python 3.8 or higher. You may also need other dependencies like a database (e.g., PostgreSQL).

- [Python](https://www.python.org/downloads/) (version 3.8 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

### Virtual Environment

It's recommended to use a virtual environment to keep dependencies required by the project separate and consistent. You can use `venv` to create a virtual environment:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On MacOS/Linux
source venv/bin/activate

# Navigate to the backend directory
cd path/to/backend

# Install dependencies from the requirements file
pip install -r requirements.txt

# Apply migrations to the database
python manage.py migrate

# Start the Django development server
python manage.py runserver


