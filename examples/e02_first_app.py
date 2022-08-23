import pocketFileExplorer
# create an web app explorer in ".." path
app=pocketFileExplorer.app("..")


import webbrowser
url="http://127.0.0.1:8000/"
webbrowser.open(url)
app.run(debug=True, port=8000) 
#app.kill()

