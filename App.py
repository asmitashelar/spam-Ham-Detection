from flask import Flask, request, render_template # type: ignore
from werkzeug.utils import escape # type: ignore
import pickle

vector=pickle.load(open("vector.pkl",'rb'))
Model=pickle.load(open("spam1.pkl",'rb'))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prediction", methods=['GET','POST'])

def prediction():
    if request.method=="POST":
        email=str(request.form['email'])
        print(email)
        txt = [email]
        
        predict=Model.predict(vector.transform(txt))
        print(predict[0])
        if predict[0] == 1:
            return render_template("index.html",prediction_text="The Email is ham")
        elif predict[0] == 0:
            return render_template("index.html",prediction_text="The Email is spam")
        else:
            return render_template ("index.html",prediction_text="The Email is not recognised")
        
    else:
        return render_template("index.html")

if __name__=='__main__':
    app.run()