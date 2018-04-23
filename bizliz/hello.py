import tornado.ioloop
import tornado.web

from bizliz.web import handler


def make_app():
    return tornado.web.Application([
        (r"/", handler.MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()