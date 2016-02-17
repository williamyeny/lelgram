from flask import Flask, render_template, request, redirect,url_for
import random, string
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)

# class Gram(db.Model):
#   id=db.Column(db.String, primary_key=True)
#   text=db.Column(db.String(150))
#   music=db.Column(db.String(20))
#   image=db.Column(db.String(200))
  
#   def __init__(self, text, music, image):
#     self.text = text
#     self.music = music
#     self.image = image

data=[]

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/create')
def create():
  return render_template('create.html')

@app.route('/generate',methods=['POST'])
def generate():
  t = request.form['text']
  i = request.form['image']
  a = request.form['audio']
#   length_code = (len(a)-8-a.find('watch?v'))*-1
#   print a.find('watch?v')
#   a = a[length_code:].replace('s','').replace('t','start') + ""
  a = a[-11:]
  id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
  data.append({
      'id': id,
      'text': t,
      'image': i,
      'audio': a,
    })
  return redirect('/gram/' + id)
  
@app.route('/gram/<gramid>')
def gram(gramid):
  for h in data:
    if h['id'] == gramid:
      return render_template('gram.html', id=h['id'], t=h['text'], i=h['image'],a=h['audio'])
  return redirect('/404')

@app.route('/404')
def fourohfour():
  return render_template('404.html')

app.run(debug=True,port=4567,host="0.0.0.0")