from flask import Flask
import pymysql
import os

app = Flask(__name__)

@app.route("/")
def index():
    try:
        db = pymysql.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            database=os.environ['DB_NAME']
        )
        with db.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS visits (count INT)")
            cur.execute("SELECT count(*) FROM visits")
            result = cur.fetchone()
            if result[0] == 0:
                cur.execute("INSERT INTO visits (count) VALUES (1)")
            else:
                cur.execute("UPDATE visits SET count = count + 1")
            db.commit()
            cur.execute("SELECT count FROM visits")
            visit_count = cur.fetchone()[0]
        db.close()
        return f"Flask App has been visited {visit_count} times 14:01!"
    except Exception as e:
        return f"Error: {str(e)}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)