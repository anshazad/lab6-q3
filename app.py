import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")        

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    d1=eval(jsonObj['d'])
    l1=eval(jsonObj['l']) 
    
    
    k=d1.values()
    for i in l1:
    	for j in d1:
    		if (i in k):
    			d1.popitem(j)
   
    response="<b> Output: "+str(d1)+".</b><br>"
    return response
if __name__ == "__main__":
	app.run()




