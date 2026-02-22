# 💰 Expense Tracking System

A full-stack personal expense tracking application built using **Streamlit (Frontend)**, **FastAPI (Backend)**, and **MySQL (Database)**.

The system allows users to add, view, delete, and analyze expenses through an interactive dashboard with dynamic charts and analytics.

---

## 🚀 Features

- Add multiple expenses per day with category and notes
- View and manage expenses by date
- Delete expenses (individual or bulk)
- Interactive dashboard with:
- 📊 Pie chart (Category-wise breakdown)
- 📈 Bar chart (Monthly spending trend)
- Daily percentage change analysis
- Clean and user-friendly UI
- Auto-refresh and reset functionality

---

## 🛠️ Tech Stack

| Layer        | Technology |
|--------------|------------|
| Frontend     | Streamlit  |
| Backend      | FastAPI    |
| Database     | MySQL      |
| Visualization| pandas, matplotlib |

---

## 📂 Project Structure

```

project-expense-tracking/
│
├── backend/
│   ├── server.py
│   ├── db_helper.py
│   └── server.log
│
├── frontend/
│   ├── app.py
│   ├── insert.py
│   ├── view_manage.py
│   ├── dashboard.py
│   └── analytics.py
│
├── images/
├── requirements.txt
├── test/
└── README.md

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shouviksarkar123/project-expense-tracking.git
cd project-expense-tracking
````

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup MySQL Database

Create a database (e.g., `expense_db`) and run:

```sql
CREATE TABLE expenses (
  id INT AUTO_INCREMENT PRIMARY KEY,
  expense_date DATE,
  amount DECIMAL(10,2),
  category VARCHAR(50),
  notes TEXT
);
```

Update MySQL credentials inside `db_helper.py`.

---

## ▶️ Running the Project

### 🔹 Start FastAPI Backend

```bash
cd backend
uvicorn server:app --reload
```

### 🔹 Start Streamlit Frontend

```bash
cd frontend
streamlit run app.py
```

---

## 📊 Dashboard Preview

### 🥧 Analytics Dashboard - Demo 1
![Analytics Demo 1](project-expense-tracking/images/analytics_ui_demo1.png)

### 📈 Analytics Dashboard - Demo 2
![Analytics Demo 2](project-expense-tracking/images/analytics_ui_demo2.png)

### 🖥️ Frontend UI
![Frontend UI](project-expense-tracking/images/app_frontend_ui.png)

## 🔮 Future Improvements

* User Authentication
* Export data as CSV / Excel
* Monthly budget alerts
* Deployment on cloud (AWS / Render)

---

## 👨‍💻 Author

**Shouvik Sarkar**

🔗 GitHub: https://github.com/shouviksarkar123  
🔗 LinkedIn: https://www.linkedin.com/in/shouvik-sarkar-619782279

---

#
