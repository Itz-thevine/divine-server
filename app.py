from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
import os
from groq_functions import groq_reply

app = Flask(__name__)
CORS(app)

@app.route('/schedule', methods=["POST"])
def generate_schedule():
    
    data = request.json
    print(data)
    
    groq_response = groq_reply(data)
    return jsonify({"status":"Request completed succeessfully", "response": groq_response}), 200

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5050)))