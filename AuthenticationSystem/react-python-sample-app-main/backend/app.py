from flask import Flask, jsonify, request, make_response 
from flask_cors import CORS
from descope import REFRESH_SESSION_TOKEN_NAME, SESSION_TOKEN_NAME, DescopeClient

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Hello World, this is TKVs app, it is public information"


@app.route("/protected", methods=["GET"])
def protected_assets():
    session_token = request.headers["Authorization"].split(" ")[1]

    try:
        descope_client = DescopeClient(project_id="P2UUaqVQtiX6Rdh64Gaw2JEVvtRg")
        jwt_response = descope_client.validate_session(session_token=session_token)
        print("Successful Validation")


        response = make_response(
            jsonify(
                {"message": "Secret Code, TKV wuz here", "severity": "high"}
            ),
            200,
        )
        response.headers["Content-Type"] = "application/json"
        return response
    except:
        print("Validation failed")
        response = make_response(
            jsonify(
            {"message": "Now allowed", "severity": "danger"}
            ),
            401,
        )
        response.headers["Content-Type"] = "application/json"
        return response
    
if __name__ == "__main__":
    app.run(port=8080)

