from flask import Flask , request , render_template
import hashlib
app = Flask(__name__)



@app.route('/')
def uploadPath():
     return render_template('requestUserName.html')


@app.route('/hello' , methods = ['GET' , 'POST'])
def printResult():
    #if request.method == 'POST':
        #userName = request.form['user']
        if request.method == 'POST':
            userName = request.form['user']

            return f"Hello {userName}!"
        
        
@app.route('/sqr' , methods = ['GET','POST'])
def sqr():
     if request.method == 'POST':
          v1 = int(request.form['user1'])
          return str(v1*v1)
     

@app.route('/submit', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        img =   request.form['Path']
        # Convert the Image into md5Hash
        with open(img, "rb") as f:
            im_bytes = f.read()
        im_hash = str(hashlib.md5(im_bytes).hexdigest())
        return f"md5 Hash of the Image is: {im_hash} "
     
     
    
if __name__ == "__main__":
    app.run(debug = True)
 