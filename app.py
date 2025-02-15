from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Helper function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Helper function to check if a number is an Armstrong number
def is_armstrong(num):
    digits = list(map(int, str(num)))
    return num == sum(digit ** len(digits) for digit in digits)

# Helper function to check if a number is perfect
def is_perfect(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

# API endpoint to classify the number
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        # Get the number from the query parameter
        number = int(request.args.get('number'))
    except ValueError:
        return jsonify({"error": True, "message": "Invalid number format"}), 400

    # Initialize the response dictionary
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": [],
        "digit_sum": sum(int(digit) for digit in str(number)),
    }

    # Check if the number is Armstrong and odd/even
    if is_armstrong(number):
        response["properties"].append("armstrong")
    if number % 2 == 0:
        response["properties"].append("even")
    else:
        response["properties"].append("odd")

    # Get a fun fact using the Numbers API (math-related fact)
    fun_fact_response = requests.get(f'http://numbersapi.com/{number}/math')
    response["fun_fact"] = fun_fact_response.text

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
