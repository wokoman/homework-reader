from flask import Flask, render_template_string
import pymysql
import pandas as pd
import os  # Import the os module

app = Flask(__name__)


@app.route("/")
def home():
    # Database connection parameters
    host = os.getenv('DB_HOST')  # Read from environment variable
    user = os.getenv('DB_USER')  # Read from environment variable
    password = os.getenv('DB_PASSWORD')  # Read from environment variable
    database = os.getenv('DB_NAME')  # Read from environment variable

    # Create a connection to the database
    connection = pymysql.connect(
        host=host, user=user, password=password, database=database
    )

    # Create a cursor
    cursor = connection.cursor()

    # Execute a query to fetch the data from the "keboola" table
    cursor.execute("SELECT * FROM keboola")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Convert the rows to a pandas DataFrame
    df = pd.DataFrame(rows, columns=[column[0] for column in cursor.description])

    # Close the cursor and the connection
    cursor.close()
    connection.close()

    # Convert the DataFrame to HTML and return it
    return render_template_string(
        "<html><body>{{ table }}</body></html>", table=df.to_html()
    )


if __name__ == "__main__":
    app.run(debug=True)
