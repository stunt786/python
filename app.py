from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def webout():
	html_content = '''
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Welcome to DevOps</title>
		<style>
			body {
				font-family: Arial, sans-serif;
				background-color: #f4f4f4;
				margin: 0;
				padding: 0;
				display: flex;
				justify-content: center;
				align-items: center;
				height: 100vh;
			}
			.container {
				text-align: center;
				background: white;
				padding: 50px;
				border-radius: 10px;
				box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
			}
			h1 {
				color: #333;
			}
		</style>
	</head>
	<body>
		<div class="container">
			<h1>DevOps is fun and Wonderful!</h1>
		</div>
	</body>
	</html>
	'''
	return render_template_string(html_content)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=7000)
