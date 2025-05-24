# Workforce Manager

**Workforce Manager** is a professional-grade Python project to manage skilled and unskilled workers, using object-oriented programming (OOP) and a MySQL database. It includes secure password encryption, modular code, logging, and configuration management. Perfect for showcasing real-world backend development skills.

---

## 🚀 Features

- Add and manage worker records (Skilled and Unskilled)
- Generate company emails automatically
- Fixed wages by worker type
- Store data in a MySQL database
- Prevent duplicate entries using email
- AES encryption for database password
- Logging of operations and errors
- Modular project structure with full OOP concepts

---

## 🧱 Project Structure

```
worker_project/
├── config/
│   └── db_config.ini           # Encrypted DB config
├── db/
│   └── db_handler.py           # DB connection & insert logic
├── encryption/
│   └── aes_encryption.py       # AES encryption utility
├── logs/
│   └── app.log                 # Log file
├── models/
│   ├── base_worker.py          # Abstract base class
│   ├── skilled_worker.py       # Skilled worker logic
│   └── unskilled_worker.py     # Unskilled worker logic
├── utils/
│   └── logger.py               # Central logging setup
├── main.py                     # Entry point to run the app
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🧪 Technologies Used

- Python 3.x
- MySQL
- `mysql-connector-python`
- `pycryptodome` for AES encryption
- OOP principles (Abstraction, Inheritance, Encapsulation, Polymorphism)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/workforce-manager.git
cd workforce-manager
```

### 2. Set Up Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Up MySQL

Create the database and table:

```sql
CREATE DATABASE IF NOT EXISTS workforce;

USE workforce;

CREATE TABLE IF NOT EXISTS workers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    location VARCHAR(100),
    skill VARCHAR(50),
    wages FLOAT
);
```

---

### 5. Encrypt Your MySQL Password

```python
from encryption.aes_encryption import AESCipher
aes = AESCipher("my-secret-key")
print(aes.encrypt("your_mysql_password"))
```

Copy the encrypted string and paste it into:

```ini
# config/db_config.ini
[mysql]
host = localhost
user = root
password = YOUR_ENCRYPTED_PASSWORD
database = workforce
```

---

### 6. Run the Application

```bash
python main.py
```

You should see logs and MySQL entries created for each worker.

---

## 🔄 Sample Execution

```python
from db.db_handler import DBHandler
from models.skilled_worker import SkilledWorker

db = DBHandler()
worker = SkilledWorker("john", "doe", "bangalore")
db.insert_worker(worker)
```

---

## 📧 Email Format Logic

Automatically generated as:
```
firstname.lastname@company.com
```

Example: `John Doe` → `john.doe@company.com`

---

## 🔐 OOP Concepts Used

| OOP Concept    | Where It's Used                                     |
|----------------|------------------------------------------------------|
| Abstraction    | `BaseWorker` defines abstract method `get_details()` |
| Inheritance    | `SkilledWorker` and `UnskilledWorker` from `BaseWorker` |
| Encapsulation  | All worker attributes wrapped inside classes         |
| Polymorphism   | `get_details()` behaves differently per class        |

---

## 📄 Example Log Output

```log
INFO - Worker john.doe@company.com inserted successfully.
WARNING - Duplicate entry skipped for john.doe@company.com
```

---

## 📌 GitHub Workflow

1. Clone → Branch → Add changes → Commit → Push
2. Create Pull Request → Review → Merge into `main`

---

## 📜 License

