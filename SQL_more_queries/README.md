# SQL - More Queries 📚

## 📌 Description

This project builds on your knowledge of SQL by introducing advanced operations involving user privileges, constraints, relational integrity, and multi-table queries including subqueries, joins, and unions.

You will work with multiple databases and learn how to design and query them in more sophisticated ways.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain (without looking it up):

- How to create a new MySQL user
- How to grant privileges to a user on a database or table
- What a PRIMARY KEY and a FOREIGN KEY are
- How to apply NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables in one query
- How to use subqueries and JOINs
- How to use UNION to merge results

---

## 🛠️ Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- OS: Ubuntu 20.04 LTS
- MySQL version: `8.0.25` or higher
- Each `.sql` file must:
  - Start with a comment describing the task
  - Include a comment before each SQL query
  - Use uppercase for SQL keywords (e.g. `SELECT`, `FROM`)
  - End with a new line
  - Be checked with `wc` for length

- A `README.md` file at the root of the project folder is mandatory.

---

## 💻 Setup Instructions

### Installing MySQL (for local environment)

```bash
sudo apt update
sudo apt install mysql-server
mysql --version
sudo service mysql start
sudo mysql
```

### Accessing MySQL in the sandbox container

- Username: `root`
- Password: `root`

Start the MySQL service:

```bash
service mysql start
```

---

## 🗂️ Project Structure

| File | Description |
|------|-------------|
| `0-privileges.sql` | List all privileges for two users |
| `1-create_user.sql` | Create a user with full privileges |
| `2-create_read_user.sql` | Create a database and a read-only user |
| `3-force_name.sql` | Create a table with NOT NULL constraint |
| `4-never_empty.sql` | Create a table with default value for ID |
| `5-unique_id.sql` | Create a table with a UNIQUE constraint |
| `6-states.sql` | Create `hbtn_0d_usa` and a `states` table |
| `7-cities.sql` | Create `cities` table with a FOREIGN KEY |
| `8-cities_of_california_subquery.sql` | List cities of California using subquery |
| `9-cities_by_state_join.sql` | List cities and corresponding states |
| `10-genre_id_by_show.sql` | List shows with at least one genre |
| `11-genre_id_all_shows.sql` | List all shows and associated genre IDs |
| `12-no_genre.sql` | List shows without a genre |
| `13-count_shows_by_genre.sql` | Count how many shows per genre |
| `14-my_genres.sql` | List genres of the show "Dexter" |
| `15-comedy_only.sql` | List all comedy shows |
| `16-shows_by_genre.sql` | List all shows and their genres |

---

## 📦 Importing Provided Data

To import the dump for TV shows:

```bash
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
curl -s "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" | mysql -uroot -p hbtn_0d_tvshows
```

---

## ✅ Best Practices

- Always comment your queries
- Use consistent formatting
- Use only one `SELECT` statement when specified
- Use `JOIN`, `UNION`, or subqueries as required

---

## 🧑‍💻 Author

Project by **Guillaume** – Holberton School.
Contributions by Thomas Roncin.
