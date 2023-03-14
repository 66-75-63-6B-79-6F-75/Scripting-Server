if not __name__ == '__main__':
    # Don't run if imported
    print('Server.py is not meant to be imported')
    exit()

Settings = {} # Settings dictionary
Settings['Port'] = 4123 # Port to listen on (default 4123)
# Settings['PortForward'] = False # Port forward to 4123 (default False)

from flask import Flask, render_template, send_from_directory
from os import listdir

app = Flask(__name__, static_url_path='', static_folder='HTML', template_folder='HTML')

@app.route('/')
def index():
    # Redirect to HTML/index.html
    return app.send_static_file('index.html') # BUGGED | 400 Bad Request | https://stackoverflow.com/questions/75738752/flask-returns-corrupted-unicode-characters-with-a-bad-request

@app.route('/scripts.html')
def scripts():
    # Get all files in Scripts folder
    Scripts = listdir('Scripts')
    # Render HTML/scripts.html
    return render_template('scripts.html', Scripts=Scripts)

@app.route('/scripts/<path:filename>')
def script(filename):
    # Open raw file from Scripts folder
    with open('Scripts/' + filename, 'r') as f:
        rawdata = f.read()
    # Replace newlines with <br> tags
    rawdata_html = rawdata.replace('\n', '<br>')
    # Return raw file with css
    return render_template('RawScript.html', rawdata=rawdata_html)

app.run(host='127.0.0.1', port=Settings['Port'], debug=True)