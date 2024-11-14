# Function to create a connection
import psycopg2
def create_connection():
    return psycopg2.connect(
        host="localhost",
        database="MoviesDB",
        user="postgres",
        password="postgres"
    )

# Function to execute queries
def run_query(query, params=None):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    try:
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    except:
        conn.commit()
        # cur.close()
        conn.close()
        return "Done"