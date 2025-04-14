# 🚀 Project Setup & Running Guide

## 📌 Prerequisites
Before running the project, make sure you have:
- ✅ **Python 3.8+** installed
- ✅ **MySQL** database access
- ✅ **Git** installed for version control
- ✅ **A virtual environment** for dependency management
---

## 📂 Project Structure
```
/project_root
│── backend/
│   │── app.py          # Main Flask app
│   │── models.py       # Database models
│   │── routes.py       # API routes (home, delete items, etc.)
│   │── config.py       # Configuration (DB connection, secrets)
│   │── templates/      # Jinja2 templates (frontend files)
│   │── static/         # Static assets (CSS, JS)
│   │── requirements.txt # Backend dependencies
│
│── .env               # Environment variables
│── README.md          # Documentation
```

---

## 💻 1️⃣ Setting Up & Running the Project
### 🔹 Step 1: Clone the Repository
```sh
git clone <REPO_URL>
cd project_root
```

### 🔹 Step 2: Backend Setup
1. Navigate to the backend folder:
    ```sh
    cd backend
    ```
2. Create & activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Set up environment variables:
    Create a **`.env`** file inside `/backend` with your database credentials:
    ```ini
    SECRET_KEY=your_secret_key
    DATABASE_URL=mysql://user:password@your_database_host/dbname
    ```
5. Run Flask App:
    ```sh
    python app.py
    ```
    Now visit **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** to see the UI.
---

## 🛠️ 2️⃣ Git Workflow (For Everyone)
Since we are working in a **team (Frontend & Backend separately)**, we follow this Git branch structure:

### 🔹 Git Branch Workflow
```
main       → (Stable production branch)
│
├── dev    → (Main development branch)
│   ├── frontend → (For frontend changes - Jinja2, HTMX, CSS, JS)
│   ├── backend  → (For backend changes - Flask, database, APIs)
```

### 🔹 Step 1: Pull the Latest Changes
```sh
git checkout dev
git pull origin dev
```

### 🔹 Step 2: Create a New Branch for Your Changes
For frontend changes:
```sh
git checkout -b frontend-feature-branch
```
For backend changes:
```sh
git checkout -b backend-feature-branch
```

### 🔹 Step 3: Make Your Changes
- **Frontend**: Edit Jinja2 templates, modify CSS & JS
- **Backend**: Modify Flask routes, update database models, or change APIs

### 🔹 Step 4: Add, Commit & Push Changes
```sh
git add .
git commit -m "Updated UI for delete item button"
git push origin frontend-feature-branch
```

### 🔹 Step 5: Create a Pull Request
- Go to **GitHub/GitLab**
- Create a **Pull Request (PR)** from `feature-branch → dev`
- **Tag relevant team members for review**

Once merged, your changes will be available for testing in the `dev` branch.

---

## 📌 3️⃣ Development Guidelines
### 🔹 Backend Development
- Follow **Flask MVC** pattern.
- Store database models in `models.py`.
- Define routes properly in `routes.py`.
- Use environment variables for **DB credentials & secrets**.

### 🔹 Frontend Development
- Modify **`/backend/templates/*.html`** files for UI.
- Use **HTMX** for dynamic updates without JavaScript.
- Refresh the **browser** after changes.

Example **HTMX button for deleting an item**:
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
✔ **Clone the repo & install dependencies**  
✔ **Run Flask backend** to test UI changes  
✔ **Run frontend separately if applicable**  
✔ **Follow Git workflow for changes**  
✔ **Push changes & create a PR for review**  

Once approved, your changes will be **merged into `dev`** and tested. 🚀

