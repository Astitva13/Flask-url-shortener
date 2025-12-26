# 🔗 Flask URL Shortener

A simple and efficient **URL shortening service** built using **Flask** and **SQLAlchemy**.  
This project demonstrates core backend concepts such as routing, database persistence, redirect logic, and edge-case handling, along with a minimal UI for easy demonstration.

---

## 🚀 Features

- Shorten long URLs into unique short links
- Persistent storage using SQLite database
- Redirect short URLs to original URLs
- Handles edge cases:
  - Duplicate long URLs return the same short link
  - Collision-safe short code generation
  - Input validation for empty and invalid URLs
  - Proper 404 handling for invalid short codes
- Simple and user-friendly web interface
- REST API endpoint for programmatic access

---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **Flask-SQLAlchemy**
- **SQLite**
- **HTML & CSS** (minimal UI)

---

## 📂 Project Structure

flask-url-shortener/
│
├── app.py # Main Flask application
├── models.py # Database models
├── requirements.txt # Project dependencies
├── README.md # Project documentation
│
├── templates/
│ └── index.html # Web UI template
│
├── static/
│ └── style.css # Basic styling
│
└── urls.db # SQLite database (generated at runtime)

yaml
Copy code

---

## ⚙️ How It Works

1. User submits a long URL via the web form or API
2. Backend validates the input
3. A unique short code is generated (or reused if URL already exists)
4. URL mapping is stored in the database
5. Visiting the short URL redirects the user to the original URL

---

## 📡 API Endpoints

### ➤ Create Short URL
**POST** `/shorten`

**Request Body (JSON):**

{
  "url": "https://www.example.com"
}

**Response:**

{
  "original_url": "https://www.example.com",
  "short_code": "Ab3Xk9",
  "short_url": "http://127.0.0.1:5000/Ab3Xk9"
}

### ➤ Redirect
GET /<short_code>

Redirects to the original URL if the short code exists, otherwise returns 404.

### ➤ Run Locally

**1️⃣ Clone the repository**

git clone https://github.com/YOUR_USERNAME/flask-url-shortener.git
cd flask-url-shortener

**2️⃣ Create and activate virtual environment**

python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

**3️⃣ Install dependencies**

pip install -r requirements.txt
4️⃣ Run the application

python app.py

**5️⃣ Open in browser**

http://127.0.0.1:5000

## 🎯 Why This Project?

**This project focuses on backend fundamentals rather than feature bloat.
It is designed to clearly demonstrate:**

Request–response flow

Database modeling and persistence

Unique identifier generation

Error handling and validation

Clean, maintainable backend structure

## 📌 Future Enhancements (Optional)
Click counter for short URLs

Custom user-defined short codes

URL expiration

Deployment to cloud platform

🧑‍💻 Author
Astitva Mishra
