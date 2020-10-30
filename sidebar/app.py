from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/item1')
def item1():
    return render_template('item1.html')

@app.route('/item2')
def item2():
    return render_template('item2.html')
   
@app.route('/item3')
def item3():
    return render_template('item3.html')
    
@app.route('/page1')
def page1():
    return render_template('page1/page1.html')    

@app.route('/page1/item1')
def page1Item1():
    return render_template('page1/item1.html')
        
@app.route('/page1/item2')
def page1Item2():
    return render_template('page1/item2.html')

@app.route('/page1/item3')
def page1Item3():
    return render_template('page1/item3.html')

if __name__=="__main__":
    app.run(host='127.0.0.1',port = 5000,debug=True)
