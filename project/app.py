from flask import Flask, render_template,jsonify 
import os 
import json 
import subprocess as sp
application=Flask(__name__) 
@application.route("/",methods=['GET']) 
def homepage(): 
	return render_template("index.php") 
#@application.route('/index.php')
#def phpexample():
#    out = sp.run(["template", "index.php"], stdout=sp.PIPE)
#    return out.stdout
