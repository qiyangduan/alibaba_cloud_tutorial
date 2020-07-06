
from flask import Flask
from flask import jsonify
from flask import request

result = {
  'UK': "Please go to bank --> transfer and fill in your sort code and account number.",
  'spain': "Please go to bank --> transfer and fill in your IBAN number.",
}

app = Flask(__name__, static_url_path='')
@app.route("/")
def hello():
    return "Hello World!"


@app.route("/genie",methods=['GET','POST'])
def genie():
    content = request.json
    # print( content['slotEntities'] )
    for slot in content['slotEntities'] :
        print(slot['intentParameterName'], ' is : ',slot['standardValue'])
    # print( content['intentName'] )
    print( (content))
    replyMessage = 'genie from sun!' + content['utterance']

    result = 0.0
    resultStr = ''
    resultFlag = False
    message = {
        'returnCode': '0',
        'returnErrorSolution': '',
        'returnMessage': 'Sucess',
        'returnValue': {
            'reply': replyMessage,
            'resultType': 'RESULT',
            'properties': {},
        },
    }
    resp = jsonify(message)
    resp.status_code = 200
    print(resp)
    return resp

@app.route('/transfer/<empId>',methods=['GET'])
def getEmp(empId):
    print("country=", empId)  
    if empId in result :
        return result[empId]
    else:
        return "Unknown request: " + empId


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
