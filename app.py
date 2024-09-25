from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

with open ('dt_house.pkl','rb') as f:
    model=pickle.load(f)

#by default method get
@app.route('/')   #it is use to routing path for url
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result',methods=['POST','GET'])
def result():
    income=float(request.form.get('area'))
    Hage=float(request.form.get('age'))
    rooms=float(request.form.get('room'))
    Brooms=int( request.form.get('bedrooms'))
    population=float(request.form.get('Populations'))

    input=[[income,Hage,rooms,Brooms,population]]

    predict=model.predict(input)[0]
    print(predict)

    result=f"Predicted Profit: {predict:.2f}"

    return render_template('result.html', res=result)


if __name__=='__main__':
    app.run(debug=True)