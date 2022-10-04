from flask import Flask, jsonify,request
app = Flask(__name__) 
temprecord=[
    {
    "temp_id":"1",
    "date": "oct4",
    "temperature": "100Kelvin"
    }
]
@app.route('/temprecord', methods=['GET'])
def displayTempRecord():
    return jsonify(temprecord)

if __name__ == '__main__':
    app.run()
