import requests, json
PARAMETERS = {
    "amount": 10,
    "type": "boolean"
}
# quiz_questions_response = requests.get(url="https://opentdb.com/api.php?amount=10&category=20&type=boolean")
quiz_questions_response = requests.get(url="https://opentdb.com/api.php", params = PARAMETERS)
quiz_questions_response.raise_for_status()
quiz_questions_response = quiz_questions_response.json()




question_data = quiz_questions_response["results"]


