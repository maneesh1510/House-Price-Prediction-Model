import pandas as pd
from flask import Flask, render_template,request
import pickle 

app= Flask(__name__)
data= pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open("RidgeModel1.pkl",'rb')) 

@app.route('/')

def index():
    locations= sorted(data['Area'].unique())
    return render_template('index.html',locations=locations)


@app.route('/predict',methods=['POST'])
def predict():
    
    location = request.form.get('Area')
    bhk= int(request.form.get('BHK'))
    floor= int(request.form.get('Floor'))
    sqft= int(request.form.get('Size'))
   
    print("ahzam")
    print(location,bhk,floor,sqft)

    input = pd.DataFrame([[location,bhk,floor,sqft]],columns=['Area','BHK','Floor','Size(in sq.ft)'])
    prediction = pipe.predict(input)[0]
    
    return str(prediction)

 
if __name__=="__main__":
   app.run(debug=True,port=5001)
