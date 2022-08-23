from flask import Flask,request

class app:

    def __init__(self,name,path):
        self.app=Flask(name)
        #---------
        @self.app.route("/")
        def first_page():
            return("hello :D ")


    def run(self,**args):
        self.app.run(**args)


    def kill(self):
        func = request.environ.get('werkzeug.server.shutdown')
        func()
        #exit()





