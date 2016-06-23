#!/usr/bin/env python3
import bottle
from plugins.generator import generateDot

app = application = bottle.Bottle()

@app.route('/')
def show_index():
    return bottle.template('index', dot=generateDot("Nexus", 4, 10, 0.03, 0.01))

class StripPathMiddleware(object):
    def __init__(self, a):
        self.a = a
    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e, h)

if __name__ == '__main__':
    bottle.run(app=StripPathMiddleware(app),
               server='auto',
               host='0.0.0.0',
               port=8080)
