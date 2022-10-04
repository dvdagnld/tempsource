from flask import Flask, jsonify,request
app = Flask(__name__) 
temprecord=[
    {
    "temp_id":"1",
    "date": "oct4",
    "temperature": "100Kelvin"
    }
]
@app.route('/temprecord', methods=['POST']) #DAVID AGUINALDO
def addTempRecord():
    temp = request.get_json()
    temprecord.append(temp)
    return {'id': len(temprecord)},200

if __name__ == '__main__':
    app.run()
