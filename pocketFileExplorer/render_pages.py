
class render:

    def __init__(self,path):
        self.__html1=r"""
<!DOCTYPE HTML>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Pocket file explorer</title>
<style>
</style>
  </head>
  <body>
    <h1> <span> <img src="icon.svg"></img></span> Pocket file explorer</h1>
    <div id="container"> """
        self.__html2=r"""
</div>    
    <footer>made whith Pocket file explorer, by: <a href="https://github.com/Saul11235">Edwin Saul</a> </footer>
  </body>
</html>"""
        self.text=":) rendered page "+str(path)

    def get_html(self,url):
        return str(self.__html1+str(self.text)+str(url)+self.__html2)

    def __gen_html(self):
        
        pass



