from flask import Flask, render_template, request, Markup
import markdown

app = Flask(__name__)

@app.route('/')
def index():
    content = mkdocsMd('static/doc/index.md')
    return render_template('index.html',**locals())

@app.route('/home/<page>')
def homeMd(page):
    content = mkdocsMd('static/doc' + request.path + '.md')
    return render_template('home/markdown.html',**locals())
    
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

# markdown转html
def mkdocsMd(filename):
	exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']
	mdcontent = ""
	with open(filename,'r',encoding='utf-8') as f:
		mdcontent = f.read()
	html = markdown.markdown(mdcontent,extensions=exts)
	content = Markup(html)
	return content

if __name__=="__main__":
    app.run(host='127.0.0.1',port = 5000,debug=True)
