import os
from webapp2 import RequestHandler, Response

ROOT = '/home/hua/uwsgi/go/iplist'

class IP_List(RequestHandler):
    def get(self):
        items = os.listdir(ROOT)
        text = ''
        for item in items:
            item = os.path.join(ROOT, item)
            if not os.path.isfile(item):
                return Response("Error ... %s is not a file." % item)
            else:
                with open(item) as fd:
                    text = text + os.path.basename(item) + ' @ ' + fd.read() + '\n'
        return Response(text)

class IP_Set(RequestHandler):
    def get(self, ip):
        return Response('Empty ...')

class IP_Address(RequestHandler):
    def get(self):
        return Response(str(self.request.remote_addr))

class Not_Found(RequestHandler):
    def get(self):
        return Response("Not Found")
