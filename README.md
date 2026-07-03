# 🛡️ Net Guard – DDoS Detection and Secure Cloud Storage

Net Guard is a **Python Flask-based web application** designed to provide secure cloud file storage with **DDoS attack detection**, user authentication, file encryption, and email notifications. The project demonstrates secure file management techniques while integrating database-driven authentication and cloud security concepts.

---

## 🚀 Features

* 👤 User Registration & Login
* 🔑 Secure Authentication
* ☁️ Cloud File Upload & Management
* 🔒 File Encryption for Enhanced Security
* 🛡️ DDoS Detection Module
* 📧 Email Notifications
* 👨‍💼 Admin Dashboard
* 🗄️ MySQL Database Integration

---

## 🛠️ Technologies Used

* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3, JavaScript
* **Database:** MySQL
* **Libraries:**

  * Flask
  * mysql-connector-python
  * cryptography
  * yagmail
  * Werkzeug

---

## 📂 Project Structure

```
Net-Guard/
│── app.py
│── templates/
│── static/
│── requirements.txt
│── README.md
│── 1cloud.sql
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mohamedashar/net-guard.git
cd net-guard
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Import the Database

* Start **XAMPP** (Apache & MySQL).
* Open **phpMyAdmin**.
* Create a database named **1cloud**.
* Import the provided SQL file.

### 5. Configure Database Credentials

Update the MySQL connection details in `app.py` if your MySQL username or password differs from the default configuration.

### 6. Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

Add screenshots of:

* Home Page
* Login Page
* User Dashboard
* Admin Dashboard
* File Upload
* DDoS Detection Results

---

## 🎯 Learning Outcomes

This project demonstrates:

* Flask Web Development
* Secure User Authentication
* MySQL Database Integration
* File Encryption
* Cloud Storage Concepts
* Web Application Security
* DDoS Detection Workflow

---

## 📄 License

This project is intended for educational and learning purposes.
