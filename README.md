# 💳 Flask ATM Project

A simple web-based ATM simulation application built using Flask.
This project allows users to perform basic banking operations such as account registration, login, deposits, withdrawals, and account deletion through a clean and responsive interface.

## 🚀 Features

### User Registration
- Register with username, email, contact number, and PIN

### Secure Login
- Login using username and PIN

### Dashboard
- View balance and account details

### Deposit Money
- Maximum ₹50,000 per transaction
- Amount must be a multiple of 100

### Withdraw Money
- Maximum ₹10,000 per transaction
- Amount must be a multiple of 100

### Account Deletion
- Permanently delete the user account

### Logout
- Secure logout functionality

### In-Memory Storage
- User data stored using a Python dictionary
- Data resets when the server restarts

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap 5
- **Storage**: In-memory (Python dictionary)

## ✅ Prerequisites

- Python 3.x
- pip (Python package manager)

## ⚙️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jabbar1911/Flask-ATM-Project.git
   cd Flask-ATM-Project
   ```

2. **Create Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**

   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS / Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 🧭 Application Pages

- **Home**: Login / Register
- **Register**: Create a new account
- **Login**: Authenticate user
- **Dashboard**:
  - View balance
  - Deposit money
  - Withdraw money
  - Delete account
  - Logout

## 📁 Project Structure

```
ATM_PROJECT/
├── app.py              # Main Flask application
├── requirements.txt    # Dependencies
├── static/             # CSS and static files
├── templates/          # HTML templates
│   ├── dashboard.html
│   ├── delete.html
│   ├── deposit.html
│   ├── index.html
│   ├── login.html
│   ├── registration.html
│   └── withdraw.html
├── venv/               # Virtual environment (optional)
└── wsgi.py             # WSGI entry point
```

## ⚠️ Important Note

- This project uses **in-memory storage**.
- **All user data will be lost when the server restarts.**
- This project is intended for learning and practice purposes only.

## 🚀 Future Improvements (Optional)

- Database integration (SQLite / MySQL)
- Password hashing
- Session management


## 🌐 Deployment (PythonAnywhere)

This project is deployed using PythonAnywhere.

**Steps Used:**
- Created a PythonAnywhere account
- Uploaded / cloned project files
- Created a virtual environment
- Installed dependencies
- Configured wsgi.py
- Reloaded the web app

### 🔗 Live Demo
[https://yourusername.pythonanywhere.com](https://yourusername.pythonanywhere.com)


## 👨‍💻 Author

**Shaik Abdul Jabbar**

