#
# slash for the path
#

from platform import system

slash="/"

if system()=="windows":
    slash="\\"

def slash_url(url):
    new_url=url.replace("\\",slash)
    new_url=new_url.replace("\\",slash)
    return new_url

