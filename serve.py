# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:56:00 2018

@author: lucas.tostes
"""

from flask import Flask
from flask import render_template
from flask import request
from flask import make_response

from random import sample

app = Flask(__name__)


def generate_code():
	code_base = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	passlen = 6
	
	p =  "".join(sample(code_base,passlen ))
	return "BR" + p

#@app.context_processor
#def utility_processor():
#    def generate_code():
#		code_base = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#		passlen = 6
#		
#		p =  "".join(random.sample(s,passlen ))
#		return "BR" + p
#    return dict(generate_code=generate_code)
	
@app.route('/')
def index():
	if not request.cookies.get('unique_code'):
		code = generate_code()
		res = make_response(render_template('index.html', message = 'Your new code is: {}'.format(code)))
		res.set_cookie('unique_code', code, max_age=60*3)
	else:
		code = request.cookies.get('unique_code')
		res = render_template('index.html', message = 'Your already generated code is: {}'.format(code))
	
	return res
   
if __name__ == "__main__":
    app.run(host= '0.0.0.0',debug=True)