import os
from time import strftime
from webapp2 import RequestHandler, Response

ROOT = '/home/hua/uwsgi/go/iplist'
PASSWORD = "ilovexiaoyezi"

class IP_List(RequestHandler):
    def get(self):
        items = os.listdir(ROOT)
        items.sort()
        text = ''
        for item in items:
            if item in ['.gitignore', 'README']:
                continue
            item = os.path.join(ROOT, item)
            if not os.path.isfile(item):
                return Response("Error ... %s is not a file." % item)
            else:
                with open(item) as fd:
                    text = text + os.path.basename(item) + ' @ ' + fd.read() + '\n'
        res = Response(text)
        res.headers = [('Content-Type', 'text/plain; charset=utf8')]
        return res

class IP_Set(RequestHandler):
    def get(self, name, ip, password):
        if name == '' or ip == '' or password == '':
            return Response('Empty ... no information provided.')
        elif password != PASSWORD:
            return Response('Error ... Authentication error.')
        else:
            with open(os.path.join(ROOT, name), 'w') as fd:
                fd.write(ip + ' @ ' + strftime("%Y-%m-%d %H:%M:%S"))
            return Response('Success ... IP address stored: %s' % ip)

class IP_Address(RequestHandler):
    def get(self):
        return Response(str(self.request.remote_addr))

class Not_Found(RequestHandler):
    def get(self):
        return Response("Not Found")
