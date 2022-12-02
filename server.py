from flask import Flask
import json
from config import me


app = Flask("server")

@app.get("/")
def home():
    return "Hello from Flask"


@app.get("/test")
def test():
    return "This is another endpoint"

@app.get("/about")
def about():
    return "Frank Sharper"
 
 
 
###################################################################
#################  CATALOG API ##################################
#################################################################
 
@app.get("/api/version")
def version():
    version = {
        "v": "v1.0.4",
        "name": "zombie rabbit"
    }
    
    # parse a dict into json string
    return json.dumps(version)



@app.get("/api/about")
def api_about():
    return json.dumps(me)


# get /api/about
# return me as json













 
 
 
app.run(debug=True)
