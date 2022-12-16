port = 4235
doLog = True

from flask import Flask, Response, url_for
import logging
import os
from html import escape

if doLog == False:
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

app = Flask(__name__, static_folder='static')
os.system("title https://github.com/66-75-63-6B-79-6F-75")
os.system("cls")

print(f"\nThis Program will Port towards: 127.0.0.1:{port}\nUsing spaces in files are not fully supported.\nTo make files with spaces compatible, please use %20 where the spaces are in the file.\nSettings:\ndoLog = {doLog}\nPort: {port}\n")
def main():
    # @app.route("/")
    # def index():
    #     return "<h2>Hello. Please use a valid directory!</h2>"

    @app.route('/files/<filename>')
    def serve_file(filename):
        return Response(open('files/' + filename, 'r').read(), content_type='text/plain')

    @app.route('/files/')
    def list_files():
        files = os.listdir('files')
        html = '''
            <html>
            <head>
                <link rel="stylesheet" href="{}">
            </head>
            <body>
                <h1>Files</h1>
                <p>Here are the files available:</p>
        '''.format(url_for('static', filename='css/style.css'))
        for file in files:
            html += '<p><a href="/files/' + escape(file) + '">' + escape(file) + '</a></p>'
        html += '</body></html>'
        return Response(html, content_type='text/html')


    app.run(host='127.0.0.1', port=port)
    
    
if __name__ == "__main__":
    main()