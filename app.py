from flask import Flask
app = Flask(__name__)

@app.route('/healthz')
def healthz():
    return """
    <html>
      <head>
        <title>CHOCHO</title>
      </head>
      <body>
        Hi Iam CHOCHO 
        <a href="http://www.youtube.com/@Chochothechowchow" target="_blank">
          www.youtube.com/@Chochothechowchow
        </a>
      </body>
    </html>
    """, 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

