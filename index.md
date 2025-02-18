# Building and Deploying a Number Classification API with Flask

## Introduction
In my journey of learning DevOps and cloud technologies, I recently built and deployed a simple API that classifies numbers based on their properties and provides fun facts about the number. This project helped me improve my understanding of API development, deployment, and cloud hosting using **Render**.

## What the API Does
The **Number Classification API** takes an integer as input and returns a JSON response indicating:
- ✅ Whether the number is Even or Odd
- ✅ Whether the number is Prime
- ✅ Whether the number is an Armstrong number
- ✅ Fun facts about the number

This API provides a simple yet practical example of working with Flask, handling HTTP requests, and deploying applications to a cloud service.

## Tech Stack Used
- **Python**: Flask for API development
- **Render**: Cloud deployment platform
- **Git & GitHub**: Version control system

## API Endpoint and Example
📌 **Base URL**: `https://devops-number-classification-api.onrender.com`

To classify a number, make a GET request to the following endpoint:

GET https://devops-number-classification-api.onrender.com/api/classify-number?number=371

bash
Copy
Edit

### Example Response:

```json
{
  "number": 371,
  "is_even": false,
  "is_odd": true,
  "is_prime": false,
  "is_armstrong": true,
  "fun_facts": [
    "371 is a prime number",
    "371 is an Armstrong number"
  ]
}
Challenges Faced
Deploying to Render was a learning experience! I initially faced issues with ensuring the API responded correctly after deployment, but I resolved them by carefully configuring my Flask application and managing dependencies properly.

Lessons Learned
✅ API development with Flask
✅ Handling errors and validation in APIs
✅ Deploying an application to Render
✅ Working with GitHub for version control

Check It Out!
🔗 Live API: Check it out here
🔗 GitHub Repository: View the code

Would love to hear your thoughts! Have you deployed an API before? Let’s connect and learn together! 🚀


