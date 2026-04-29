# 🎓 EduTrack – Role-Based Academic Management System

![Django](https://img.shields.io/badge/Django-6.0-green?style=for-the-badge\&logo=django)
![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge\&logo=python)
![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

EduTrack is a **role-based academic management system** built using Django, enabling Admins, Teachers, and Students to manage and access academic data efficiently.

---

## 🚀 Live Demo

🔗 https://studenthub-4fsq.onrender.com/

👉 Use demo credentials below to explore all roles.

---

## 🔐 Demo Credentials

| Role    | Username | Password   |
| ------- | -------- | ---------- |
| Admin   | admin1   | admin123   |
| Teacher | teacher1 | teacher123 |
| Student | student1 | student123 |

---

## 📸 Screenshots

* Login Page

<img width="1920" height="1080" alt="Screenshot (43)" src="https://github.com/user-attachments/assets/0cc97885-234b-4709-acbf-a921d3ecdb48" />
* Teacher Dashboard

  <img width="1920" height="1080" alt="Screenshot (47)" src="https://github.com/user-attachments/assets/8d9a135c-5a82-44e7-b822-1c4f6e164d8b" />

* Student Dashboard
<img width="1920" height="1080" alt="Screenshot (44)" src="https://github.com/user-attachments/assets/455b2214-e970-4e59-a283-f3d96ab665bf" />

* my students
<img width="1920" height="1080" alt="Screenshot (48)" src="https://github.com/user-attachments/assets/f12a3ea7-f1ff-4a7a-bcf0-27ce466b5387" />

* Results Page
<img width="1920" height="1080" alt="Screenshot (46)" src="https://github.com/user-attachments/assets/61a2099d-243d-41ee-8c39-e2b880c7c8e7" />


---

## 🎯 Features

### 👨‍💼 Admin

* Manage teachers and students
* Assign students to teachers
* View system-wide data
* Full control via Django Admin

### 👨‍🏫 Teacher

* View assigned students
* Edit student details
* Mark daily attendance
* Add subject-wise marks
* Search students

### 🎓 Student

* View profile
* Check attendance records
* View attendance percentage
* Access subject-wise results

---

## 📊 Core Functionalities

* ✅ Role-Based Authentication
* ✅ Secure Login System
* ✅ Student–Teacher Assignment
* ✅ Daily Attendance Tracking
* ✅ Attendance Percentage Calculation
* ✅ Marks Management System
* ✅ Automatic Pass/Fail Logic (Marks < 35)
* ✅ Overall Result Calculation

---

## 🛠️ Tech Stack

| Category   | Technology                      |
| ---------- | ------------------------------- |
| Backend    | Django                          |
| Frontend   | HTML, CSS           |
| Database   | SQLite (Dev), PostgreSQL (Prod) |
| Deployment | Render                          |
| Static     | WhiteNoise                      |

---

## 📁 Project Structure

```text
studenthub/
├── accounts/
├── students/
├── attendance/
├── results/
├── templates/
├── static/
├── Procfile
├── build.sh
├── requirements.txt
└── manage.py
```

---

## ⚙️ Local Setup

```bash
git clone https://github.com/sai0566/studenthub.git
cd your-repo

python -m venv env
env\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## 🌐 Deployment

* Hosted on **Render**
* Environment variables configured securely
* Static files served using WhiteNoise

---

## 🔐 Security

* Environment variables for secrets
* No database committed
* Role-based access control
* Django authentication system

---

## 🚀 Future Improvements

* 📊 Graphs & analytics dashboard
* 📄 PDF report generation
* 📤 Export to Excel
* 📱 Fully responsive UI
* 🔔 Notifications

---

## 👨‍💻 Author

**Sairam**
📧 [sreeram0566@gmail.com](mailto:sreeram0566@gmail.com)
🔗 https://linkedin.com/in/sairam0566

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
