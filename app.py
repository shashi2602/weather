from flask import Flask,render_template,redirect,session,request,url_for
from flask_bootstrap import Bootstrap
import json
import urllib.request


app=Flask(__name__)
Bootstrap(app)

@app.route("/",methods=['GET','POST'])
def main():
    if request.method == 'POST': 
        city = request.form['city'] 
        return redirect('/weather/'+city+'') 
    return render_template('home.html') 


@app.route("/weather/<string:city>")
def weather(city):
    try:
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=1236e58671e4ceb2270dd39abdbff723').read() 
        list_of_data = json.loads(source) 
        return render_template('weather.html', data = list_of_data) 
    except:
        return render_template("error.html")
    
if __name__=="__main__":
    app.run(debug=True,port=5004)
