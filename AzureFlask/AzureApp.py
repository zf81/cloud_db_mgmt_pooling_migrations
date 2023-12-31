from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, text

load_dotenv()  

AZUREURL = os.getenv("AZUREURL")

engine = create_engine(AZUREURL,
    connect_args={'ssl': {'ssl-mode':'preferred'}},
)    


app = Flask(__name__)   

@app.route('/')
def mainpage():
    return render_template('azurebase.html')

@app.route('/patients')
def patients():
    # Establish a database connection
    with engine.connect() as connection:
        # Execute an SQL query to fetch data (replace this with your query)
        query1 = text('SELECT * FROM patients')

        result1 = connection.execute(query1)

        # Fetch all rows of data
        patientdata = result1.fetchall()

    return render_template('azurepatients.html', data1=patientdata)


@app.route('/laboratoryorder')
def laboratory_order():
    # Establish a database connection
    with engine.connect() as connection:
        # Execute an SQL query to fetch data (replace this with your query)
        query2 = text('SELECT * FROM laboratory_order')

        result2 = connection.execute(query2)

        # Fetch all rows of data
        labdata = result2.fetchall()

    return render_template('azurelabs.html', data2=labdata)

if __name__ == '__main__':
    app.run(debug=True)