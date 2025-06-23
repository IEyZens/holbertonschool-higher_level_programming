# SQL - Introduction 📊

## 📌 Description

This project introduces the basics of **SQL** and **MySQL** through a series of scripts to manipulate a relational database: creating, deleting, inserting, sorting, updating, and more.

You will become familiar with **DML** (Data Manipulation Language) and **DDL** (Data Definition Language) commands essential for interacting with a relational database system.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain (without Google!):

- What a database is
- What a relational database is
- What SQL stands for
- What MySQL is
- How to create and delete a database or a table
- How to use commands like `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- What subqueries are
- How to use MySQL functions
- How to write clean, robust, and commented SQL queries

---

## 🧠 Key Concepts

- SQL vs MySQL
- DDL vs DML
- Basic database operations
- SQL syntax (uppercase keywords!)
- Record management and advanced queries

---

## 🛠️ Technical Requirements

- Allowed editors: `vi`, `vim`, or `emacs`
- OS: Ubuntu 20.04 LTS
- MySQL version: `8.0.25` minimum
- Each `.sql` file must:
  - Start with a comment describing the task
  - Include a comment before each SQL query
  - End with a new line (`\n`)
  - Be testable using `wc` for file length

---

## 💻 MySQL Installation (Ubuntu 20.04)

```bash
sudo apt update
sudo apt install mysql-server
mysql --version
sudo service mysql start
```

To connect:

```bash
sudo mysql -uroot
```

---

## 🗂️ Project Content

Each file represents a specific SQL task:

| File | Description |
|------|-------------|
| `0-list_databases.sql` | List all databases |
| `1-create_database_if_missing.sql` | Create `hbtn_0c_0` if it doesn't exist |
| `2-remove_database.sql` | Delete `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | List all tables of a given database |
| `4-first_table.sql` | Create a table named `first_table` |
| `5-full_table.sql` | Print the full definition of `first_table` |
| `6-list_values.sql` | List all rows of `first_table` |
| `7-insert_value.sql` | Insert a row into `first_table` |
| `8-count_89.sql` | Count rows with `id = 89` |
| `9-full_creation.sql` | Create and populate `second_table` |
| `10-top_score.sql` | List records ordered by score (descending) |
| `11-best_score.sql` | List records with score >= 10 |
| `12-no_cheating.sql` | Update Bob’s score to 10 using name only |
| `13-change_class.sql` | Delete records with score ≤ 5 |
| `14-average.sql` | Compute the average score |
| `15-groups.sql` | Group records by score count |
| `16-no_link.sql` | List only rows with a non-empty name field |

---

## 🧪 Example Execution

```bash
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

---

## 📚 Useful Resources

- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-mysql)
- [MySQL Cheat Sheet](https://devhints.io/mysql)
- [MySQL 8.0 SQL Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

---

## ✅ Best Practices

- Use **comments** above every query
- Keep a consistent **naming convention**
- Test your scripts regularly using the **sandbox**
- Never use `SELECT` or `SHOW` when disallowed

---

## 🧑‍💻 Author

Project provided by **Guillaume** – Holberton School.
Contributions by [YourName].

