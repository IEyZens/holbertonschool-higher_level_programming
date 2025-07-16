import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO Products (id, name, price, category)
        VALUES
        (1, 'Laptop', 799.99, 'Electronics'),
        (2, 'Coffee Mug', 15.99, 'Home Goods')
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
