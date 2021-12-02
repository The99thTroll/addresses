from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "Contact": "7776665555",
        "Name": "Bob",
        "Done": False,
        "id": 1
    },
    {
        "Contact": "1112223333",
        "Name": "Ross",
        "Done": False,
        "id": 2
    }
]

@app.route("/add-data", methods = ["POST"])

def addContact():
    if not request.json:
        return jsonify({
            'status': "ERROR",
            'message': "Please provide data"
        }, 400)
    contact = {
        "id": contacts[-1]["id"] + 1,
        "Contact": request.json("contact"),
        'Name': request.json.get('name', ""),
        "Done": False
    }
    
    contacts.append(task)
    
    return jsonify({
        'status': "SUCCESS",
        'message': 'Task successfully posted'
    })

@app.route("/get-data")

def getContacts():
    return jsonify({
        "data": contacts
    })

if (__name__ == "__main__"): 
    app.run(debug=True)