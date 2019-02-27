# print("Hello World")

# lists = [1, 2, 3, 4]

# for list in lists:
#     print(list)
# --- PYTHON WEBAPP USING TORNADO
import tornado.ioloop
import tornado.web
import os
import json
STATIC_DIRNAME = "res"
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), STATIC_DIRNAME),
    "static_url_prefix": "/res/",
    "debug": True,
    "autoreload": True
}
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
        #self.write("Hello, world")
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

class StopHandler(tornado.web.RequestHandler):
    def get(self):
        #stopApp() 
        print("Stopped") 
class APIHandler(tornado.web.RequestHandler):
    def post(self):
        #phone = self.get_body_argument("phone", default=None, strip=False)
        phone = self.get_argument("phone")
        account_no = self.get_argument("account_no")
        print(phone)
        print(account_no)
        if account_no == "0033033067":
            redirect(self)
           
       # print("Phone is "+req.phone)
        print("post received")

class StartHandler(tornado.web.RequestHandler):
    def get(self):
        startApp()
        print("Started")
#################################
def redirect(mself):
        mself.redirect('/login')
        return
def startApp():
    print("started")
def stopApp():
    tornado.ioloop.IOLoop.current().stop()
def restartApp():
    tornado.ioloop.IOLoop.current().restart()  

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler),
        (r"/api", APIHandler),
        (r"/stop", StopHandler),
        (r"/start", StartHandler)
    ],  **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    print("App started")
    tornado.ioloop.IOLoop.current().start()
    