from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def webout():
	
	return '<h2>This is wonderful Project</h2>'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=7000)
