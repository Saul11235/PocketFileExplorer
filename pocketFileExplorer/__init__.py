from flask import Flask,request

try:
    from render_pages import render
except:
    from .render_pages import render


class app:

    def __init__(self,path):
        self.__app=Flask(__name__)
        self.__render=render(path)

        @self.__app.route("/")
        def first_page():
            html=self.__render.get_html("")
            return(html)

        @self.__app.route('/<path:url_file>')
        def file_explorer(url_file):
            html=self.__render.get_html(url_file)
            return(html)

    def get_object(self): return self.__app

    def run(self,**args):
        self.__app.run(**args)

    def kill(self):
        func = request.environ.get('werkzeug.server.shutdown')
        func()
        #exit()





