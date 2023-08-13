# -*- code:utf-8 -*-
# +-------------------------------------------------------------------
# | Author: wzz <1021266737@qq.com> Time: 2023/03/05 上午 01:54
# +-------------------------------------------------------------------

# --------------------------------
# 
# --------------------------------

# from __future__ import print_function
#
# import gevent
# import random
#
# from geventwebsocket import WebSocketServer, WebSocketApplication, Resource
# from geventwebsocket._compat import range_type
#
#
# class PlotApplication(WebSocketApplication):
#     def on_open(self):
#         for i in range_type(10000):
#             self.ws.send("0 %s %s\n" % (i, random.random()))
#             gevent.sleep(0.1)
#
#     def on_close(self, reason):
#         print("Connection Closed!!!", reason)
#
#
# def static_wsgi_app(environ, start_response):
#     start_response("200 OK", [("Content-Type", "text/html")])
#     return [bytes(line, "utf-8") for line in open("index.html").readlines()]
#
#
# resource = Resource([
#     ('/', static_wsgi_app),
#     ('/data', PlotApplication)
# ])
#
# if __name__ == "__main__":
#     server = WebSocketServer(('0.0.0.0', 5000), resource, debug=True)
#     server.serve_forever()


from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello world"


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
