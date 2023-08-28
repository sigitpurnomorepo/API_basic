from flask import jsonify, request
from app.user import userbp
import json
import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

user_file = os.path.join(location, "../data/user.json")

def read_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    return data
    
def write_json(file_path, data):
    with open(file_path, "w") as file:
        data = json.dump(data, file, indent=2)

@userbp.route("/users", methods=["GET"])
def get_all_user():
    data = read_json(user_file)
    response = jsonify(
        {
            "success": True,
            "data": data
        }
    )
    return response, 200


@userbp.route("/users", methods=["POST"]) # Get all data
def create_user():
    data = request.get_json()
    # print(data)
    newData = {
        "_id": data["_id"],
        "name": data["name"],
        "email": data["email"],
        "role": data["role"]
    }
    # print(newData)
    temp_data = read_json(user_file) # Add new data
    # print(temp_data)
    temp_data["data"].append(newData)
    # print(temp_data)
    write_json(user_file, temp_data)

    response = jsonify(
        {
            "success": True,
            "message": "New user is created"
        }
    )

    return response, 200


@userbp.route("/users/<int:id>", methods=["GET"])   # Get one user data
def get_one_user(id):
    users = read_json(user_file)
    
    # looping untuk mencari id yang sesuai dengan parameter
    user = [user for user in users["data"] if user["_id"] == id]

    # Jika user tidak ditemukan
    if not user:
        response = jsonify(
            {
                "message": "User Not Found"
            }
        )

        return response

    response = jsonify(
        {
            "success": True,
            "data": user[0]
        }
    )

    return response


@userbp.route("/users/<int:id>", methods=["PUT"]) # Update data user
def update_user(id):
    data = request.get_json()

    users = read_json(user_file)

    # Update user data
    for user in users["data"]:
        if user["_id"] == id:
            user["name"] = data["name"]
            user["email"] = data["email"]
            user["role"] = data["role"]
            break

    write_json(user_file, users)

    response = jsonify(
        {
            "success": True,
            "message": "User data successfully updated!"
        }
    )

    return response


@userbp.route("/users/<int:id>", methods=["DELETE"]) # Delete user
def remove(id):
    users = read_json(user_file)
    # print(users)

    # Filter and remove user data
    for user in users["data"]:
        if user["_id"] == id:
            users["data"].remove(user)
            break

    write_json(user_file, users)

    response = jsonify(
        {
            "success": True,
            "message": "Remove user data successfully!"
        }
    )

    return response

