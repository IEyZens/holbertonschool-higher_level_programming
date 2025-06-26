# Python - Object-relational Mapping 🐍🗃️

## 📌 Description

This project bridges the world of **Databases** and **Python** using both raw **MySQLdb** and **SQLAlchemy**, an Object Relational Mapper (ORM).
It is divided into two parts:

- **Part 1:** Use `MySQLdb` to connect and run SQL queries from Python
- **Part 2:** Use `SQLAlchemy` to abstract the database structure using Python objects only

ORMs allow developers to focus on manipulating Python objects without worrying about how the data is stored, providing clean, maintainable, and database-independent code.

---

## 🎯 Learning Objectives

You should be able to explain (without Google):

- How to connect to a MySQL database from Python
- How to SELECT and INSERT rows using Python
- What an ORM is and how it works
- How to map a Python Class to a MySQL table using SQLAlchemy

---

## 🛠️ Requirements

- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- Files must end with a new line
- First line of each file: `#!/usr/bin/python3`
- Use `pycodestyle` (v2.7.*)
- All files must be executable
- Documentation required for:
  - Modules
  - Classes
  - Functions (inside and outside classes)
- Do NOT use `execute()` with SQLAlchemy

---

## 💻 Installation Instructions

### MySQL 8.0

```bash
sudo apt update
sudo apt install mysql-server
mysql --version
sudo mysql
```

### Install MySQLdb (mysqlclient)

```bash
sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
sudo pip3 install mysqlclient
```

### Install SQLAlchemy

```bash
sudo pip3 install SQLAlchemy
```

---

## 🗂️ Project Structure

| File | Description |
|------|-------------|
| `0-select_states.py` | List all states using `MySQLdb` |
| `1-filter_states.py` | List states starting with 'N' |
| `2-my_filter_states.py` | Filter states by name (vulnerable to SQL injection) |
| `3-my_safe_filter_states.py` | Filter states by name (safe from SQL injection) |
| `4-cities_by_state.py` | List all cities with corresponding state name |
| `5-filter_cities.py` | List all cities in a specific state |
| `model_state.py` | SQLAlchemy model for `states` table |
| `6-model_state.py` | Generate states table using SQLAlchemy |
| `7-model_state_fetch_all.py` | List all State objects with SQLAlchemy |
| `8-model_state_fetch_first.py` | Display the first State object |
| `9-model_state_filter_a.py` | List all State objects containing 'a' |
| `10-model_state_my_get.py` | Print the id of a State by name |
| `11-model_state_insert.py` | Insert a new State |
| `12-model_state_update_id_2.py` | Update a State name |
| `13-model_state_delete_a.py` | Delete all States with 'a' in the name |
| `model_city.py` | SQLAlchemy model for `cities` table |
| `14-model_city_fetch_by_state.py` | Print all cities with corresponding state |

---

## 🧪 Example Execution

```bash
./0-select_states.py root root hbtn_0e_0_usa
./5-filter_cities.py root root hbtn_0e_4_usa "Texas"
./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
```

---

## 🧠 Concepts to Understand

- SQL vs ORM
- MySQL queries vs SQLAlchemy object manipulation
- Database schema modeling with classes
- Security risks: SQL injection

---

## ✅ Best Practices

- Use parameterized queries to avoid SQL injection
- Keep code modular and documented
- Validate arguments (optional for this project)
- Avoid raw `execute()` when using SQLAlchemy ORM

---

## 🧑‍💻 Author

Project by **Guillaume** – Holberton School.
Contributions by Thomas Roncin.

