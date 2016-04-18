'''
    we will be learning how to create a webpage with simple 'hello world'
    we will be creating different webpages
    using variables (strings, integers)

'''

from flask import Flask, request, render_template
import Image
app = Flask(__name__)



@app.route('/')             # specifies route to the root directory '/' means 'root'
def hello_world():
    return 'Hello World!'


@app.route('/name')             # specifies route to the name directory
def name():
    return '<h1> Jayesh Kurambhatti</h1>'

@app.route('/contact_no')  # specifies route to the contact directory
def contact():
    return '''<h1> 9916567478 8088286577</h1>
              <h2>address : <h3>bangalore</h3></h2>
               <h3> locality</h3> : btm
           '''

# for using a variable you should enter the var name in <> ,eg : <about>, <var2>, <train>, etc
# also the url is always in '' or "", so see the example below

@app.route('/friend/<user>')           # demo of using a string
def call(user):
    return 'hey there %s' % user

@app.route("/post/<int:post_id>")       # demo of int var mention the datatype inside <>
def print_postid(post_id):
    return "the post-id is %s" % post_id

@app.route('/tea')
def print_tea():
    img = Image.open("cup.jpg",'r')
    return img


# whenever you request for a url or webpage or anything, the HTTP GET method is used
# when you are filling a form then we use HTTP POST method to POST info.

@app.route('/method')
def which_m():
    return "the method used is %s " % request.method

# write function for calling html file using render_template library

@app.route('/homepage/<uname>')
def home(uname):
    return render_template("index.html",name = uname)   # copy the uname into variable name of render_templaate()



if __name__ == '__main__':      # its kind of like main() file always run the app from this file
    app.run()                   # starts the server



