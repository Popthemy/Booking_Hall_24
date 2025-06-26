# 📖 Book Hall

**Solving Scheduling Headaches, Two Classes at a Time**
Book Hall is a Django-based web application built to streamline the scheduling of halls for classes on campus. Our dynamic time-slot feature prevents overlapping classes, maximizes hall utilization, and ensures a seamless booking experience for students and class representatives.

---

## ✨ Features

* ✅ **Dynamic Time Slotting:** Avoid overlapping classes by preventing double-booking and allowing only available slots.
* ✅ **Centralized Hall Management:** View and add halls, see scheduled classes, and manage building-specific schedules.
* ✅ **User Profiles:** Enable class representatives to edit profile details and view all scheduled classes at a glance.
* ✅ **Postgres Backend:** Uses a robust relational database to ensure data integrity and scalability.
* ✅ **User-Friendly:** Intuitive design for straightforward hall and class management.

---

## 🧭 Project Structure

```
bookhall/
│
├── about_us/             # Information about the project, its goals, and the team behind it
├── building/             # Hall management, adding halls, viewing schedules per hall
├── booking/              # Pre-scheduling and main hall booking logic
├── my_user/              # User profile management and scheduled classes view
├── templates/            # HTML templates
├── static/               # Static files (CSS, JS, images)
├── manage.py             # Django's management utility
└── requirements.txt      # Python dependencies
```

---

## 🛠 Tech Stack

* **Backend**: Django (MVT architecture)
* **Database**: PostgreSQL
* **Frontend**: HTML, CSS, JS
* **Version Control**: Git and GitHub
* **Deployment**: Ready for Heroku, Railway, or any cloud provider

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/book-hall.git
cd book-hall
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv env
source env/bin/activate     # On Windows use `env\Scripts\activate`
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Postgres

Create a new database in Postgres and add the credentials to `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<your_database_name>',
        'USER': '<your_database_user>',
        'PASSWORD': '<your_database_password>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Run Development Server

```bash
python manage.py runserver
```

Your app will be available at `http://127.0.0.1:8000/`

---

## 📜 Usage

* Browse to the home page to view all halls.
* Sign up or log in as a class rep.
* Book available halls via the booking section.
* Manage your profile and view scheduled classes.
* Share schedules with classmates once confirmed.

---

## 🤝 Contributing

Contributions are welcome!
Please follow the steps:

1. Fork this repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:

   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## 🧑‍💻 Team

This project is built and maintained by a passionate team of students who aim to improve hall allocation processes across academic institutions.

---

## 🧭 License

This project is licensed under the [MIT License](LICENSE).

---

> **Join us** and help streamline the academic environment!
> ✉️ Feedback and contributions are always welcome.
