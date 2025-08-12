import sqlite3

def find_user(username):
    conn = sqlite3.connect(":memory:")  # using in-memory DB for demo
    cursor = conn.cursor()

    # Create a sample users table
    cursor.execute("CREATE TABLE users (id Isql_injection_demo.pyNTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'secret')")

    # Insecure SQL query vulnerable to injection (Bandit will flag this)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()
    return result

if __name__ == "__main__":
    # Simulated malicious input
    injected_username = "' OR '1'='1"
    users = find_user(injected_username)
    print("Query result:", users)
