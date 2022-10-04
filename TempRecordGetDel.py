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

@app.route('/temprecord/<int:index>', methods=['DELETE'])
def deleteTempRecord(index): #DAVID AGUINALDO
    temp.pop(index)
    return 'Record was successfully deleted',200
if __name__ == '__main__':
    app.run()
