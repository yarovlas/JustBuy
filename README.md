# 🛒 JustBuy

JustBuy is a lightweight web application built with Flask, Jinja2, and MySQL. It allows users to interact with a simple interface to manage items (e.g., add/delete) using a clean MVC structure and modern web techniques like HTMX for dynamic UI updates.

---

## 🚀 Project Setup & Running Guide

### 📌 Prerequisites

Make sure you have the following installed before starting:

* ✅ Python 3.8+
* ✅ MySQL database
* ✅ Git
* ✅ (Recommended) Virtual environment for Python dependencies

---

### 📂 Project Structure

```
project_root/
│
├── backend/
│   ├── app.py           # Main Flask app
│   ├── models.py        # SQLAlchemy models
│   ├── routes.py        # API routes
│   ├── config.py        # Configuration (DB, secrets)
│   ├── templates/       # Jinja2 templates (UI)
│   ├── static/          # CSS, JavaScript
│   └── requirements.txt # Backend dependencies
│
├── .env                 # Environment variables
└── README.md            # Project documentation
```

---

## 💻 1️⃣ Setting Up & Running the Project

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/yarovlas/JustBuy.git
cd JustBuy
```

### 🔹 Step 2: Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 🔹 Step 3: Configure Environment

Create a `.env` file in `/backend/`:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=mysql://user:password@host/database
```

### 🔹 Step 4: Run the Flask App

```bash
python app.py
```

Visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🛠️ 2️⃣ Git Workflow (Team)

We use a simple and clean Git workflow for team collaboration.

### 🔹 Branching Model

```
main       → Stable production
dev        → Main development
├── frontend → Frontend features (HTML, HTMX, CSS, JS)
└── backend  → Backend logic (Flask, DB, APIs)
```

### 🔹 Workflow Steps

1. **Update local repo:**

   ```bash
   git checkout dev
   git pull origin dev
   ```

2. **Create a feature branch:**

   ```bash
   # For frontend
   git checkout -b frontend-new-ui

   # For backend
   git checkout -b backend-add-api
   ```

3. **Work on your feature.**

4. **Commit and push:**

   ```bash
   git add .
   git commit -m "Add delete item button UI"
   git push origin <branch-name>
   ```

5. **Open a Pull Request (PR) → `dev`**

   * Review with team
   * Merge after approval

---

## 📌 3️⃣ Development Guidelines

### 🔹 Backend

* Use Flask MVC pattern
* Database logic → `models.py`
* Routes → `routes.py`
* Secrets and DB config → `.env`

### 🔹 Frontend

* Edit templates in `/templates/`
* Use [HTMX](https://htmx.org) for live updates without full reloads

Example delete button with HTMX:

```html
<button
    hx-delete="/delete-item/{{ item.id }}"
    hx-target="#items-table"
    hx-confirm="Are you sure?"
>
    Delete
</button>
```

---

## ✅ 4️⃣ Summary

✔ Clone the repo
✔ Setup backend and virtual environment
✔ Configure `.env` file
✔ Run Flask server
✔ Follow Git flow for development
✔ Submit PRs for team review

---

## 📃 License

[MIT License](LICENSE) – free to use and modify.

---

## 👥 Authors & Contributors

Developed by [@yarovlas](https://github.com/yarovlas) and contributors.
