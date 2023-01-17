port = 4235



from flask import Flask, Response, url_for
import logging
from os import system, listdir, path
from html import escape
import subprocess
from urllib.request import urlretrieve
import zipfile
from time import sleep

app = Flask(__name__, static_folder='static')
system("title https://github.com/66-75-63-6B-79-6F-75")
system("cls")

print("Welcome to Scripting-Server. Would you like to port forward your server with Ngrok?")
Forward = input("Port Forward? (y / n): ")

if not Forward == "y" or not Forward == "n":
       print("Please enter a value of 'y' or 'n' - Exiting in 3 seconds.")
       sleep(3)
       exit(1)

if Forward.lower() == "n":
    Log = input("Make logs? (y / n): ")
    if not Log == "y" or not Log == "n":
       print("Please enter a value of 'y' or 'n' - Exiting in 3 seconds.")
       sleep(3)
       exit(1)
    print(f"\nThis Program will Port towards: 127.0.0.1:{port}\nUsing spaces in files are not fully supported.\nTo make files with spaces compatible, please use %20 where the spaces are in the file.\nSettings:\ndoLog = {Log}\nPort: {port}\n")
elif Forward.lower() == "y":
    UserAuth = input("Auth token: ")

    print("Downloading Ngrok...")
    if path.exists("ngrok.exe"):
        print("Ngrok already is downloaded.")
    else:
        urlretrieve("https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip", "ngrok.zip")
        print("Unzipping...")
        with zipfile.ZipFile("ngrok.zip", 'r') as zip_ref:
            zip_ref.extractall()
        subprocess.run("del ngrok.zip")
    print("Setting up server...")
    subprocess.run(f"ngrok.exe authtoken {UserAuth}")
    subprocess.Popen("ngrok.exe http 4235")


if Log == False:
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

def main():
    @app.route("/")
    def index():
        html = '''
            <html>
            <head>
                <link rel="stylesheet" href="{}">
            </head>
            <body>
                <h1>Please use /files/</h1>
                <p>To see the files stored in the files folder.</p>
                <a href="/files/">Click here for the link!</a>
                <br></br>
                <a href="https://github.com/66-75-63-6B-79-6F-75"> Made by 66-75-63-6B-79-6F-75 </a>
        '''.format(url_for('static', filename='css/style.css'))

        return Response(html, content_type='text/html')

    @app.route('/files/<filename>')
    def serve_file(filename):
        return Response(open('files/' + filename, 'r').read(), content_type='text/plain')

    @app.route('/files/')
    def list_files():
        files = listdir('files')
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