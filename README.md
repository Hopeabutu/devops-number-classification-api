# devops-number-classification-api# Number Classification API

This is a simple API that classifies numbers based on their properties. It accepts a number as a query parameter and returns JSON indicating whether the number is even, odd, prime, or an Armstrong number.

## API URL

The API is deployed and publicly accessible at:

**Base URL:** `https://devops-number-classification-api.onrender.com`

## Endpoints

### 1. Classify a Number

- **Endpoint:** `/api/classify-number`
- **Method:** GET
- **Query Parameter:** `number` (integer)
- **Response Format:** JSON

#### Example Request

```
GET https://devops-number-classification-api.onrender.com/api/classify-number?number=371
```

#### Example Response

```json
{
  "number": 371,
  "is_even": false,
  "is_odd": true,
  "is_prime": false,
  "is_armstrong": true
}
```

## Features

- Accepts GET requests with a number parameter.
- Returns JSON response with number classifications.
- Proper error handling for invalid inputs.
- Provides appropriate HTTP status codes.
- Fast response time (< 500ms).

## Error Handling

- If a non-integer value is provided, the API returns a `400 Bad Request` error:

```json
{
  "error": true,
  "message": "Invalid number format"
}
```

## Running Locally

To run this API locally, follow these steps:

### Prerequisites

- Python 3.11+
- pip
- Virtual environment (optional but recommended)

### Setup Instructions

```sh
git clone https://github.com/Hopeabutu/devops-number-classification-api.git
cd devops-number-classification-api
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
flask run
```

The API will be available at http\://127.0.0.1:5000/api/classify-number?number=371 locally.

## Deployment

This API is deployed using [Render](https://render.com), ensuring public accessibility and stability.

## Contributing

Feel free to fork this repository and submit pull requests.

## License

This project is licensed under the MIT License.




