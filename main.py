#   def application(environ, start_response):
#       status = '200 OK'
#       response_headers = [('Content-Type', 'text/plain')]
#       start_response(status, response_headers)
#       return environ['REMOTE_ADDR']

import webapp2

from view import IP_Address
from view import IP_List
from view import IP_Set
from view import Not_Found

urls = [ (r'/ip/?', IP_Address),
         (r'/iplist/?', IP_List),
         (r'/ipset/.*/?', IP_Set),
         (r'/.*', Not_Found),
]

application = webapp2.WSGIApplication(urls, debug=True)
