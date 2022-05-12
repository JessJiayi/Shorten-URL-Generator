
import tornado.web



class ErrorHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("<h1>404：The page is lost!</h1>")
