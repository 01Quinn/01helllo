#1

from flask import Flask, jsonify
import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'airports',
    user = 'root',
    password = '453489',
    autocommit = True)
print("connection")

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the airport API."})


@app.route("/airport/<icao_code>", methods=['GET'])
def get_airport_info(icao_code):
    cursor = connection.cursor(dictionary=True)
    query = f"select * from airports where ident = '{icao_code}'"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()

    if result:
        airport_info = {
            "ICAO": result['ident'],
            "Name": result['name'],
            "Location": result['municipality']
        }
        return jsonify(airport_info)
    else:
        return jsonify({"Error": "Airport not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)

#2 prime number

from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def prime_number(number):
    if is_prime(number):
        return jsonify({"Number": number, "isPrime": True})
    else:
        return jsonify({"Number": number, "isPrime": False})

if __name__ == '__main__':
    app.run(debug=True)