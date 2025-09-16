
import sys
from wsgiref.simple_server import make_server

import mapscript


class PubMapWEB:
    """
    Create wsgi socket for object PubMap
    Tiny map server
    """

    def __init__(self, mapfile, port=3007, host='0.0.0.0'):
        self.wsgi_host = host
        self.wsgi_port = port
        with open(mapfile) as f:
            mapstyle = f.read()
        self.mapscript_obj = mapscript.fromstring(mapstyle)
    
    def application(self, env, start_response):
        # mapserver magic
        request = mapscript.OWSRequest()
        mapscript.msIO_installStdoutToBuffer()
        request.loadParamsFromURL(env['QUERY_STRING'])
        status_id = self.mapscript_obj.OWSDispatch(request)
        content_type = mapscript.msIO_stripStdoutBufferContentType()
        result = mapscript.msIO_getStdoutBufferBytes()
        mapscript.msIO_resetHandlers()

        # get response status
        if status_id == mapscript.MS_SUCCESS:
            status = '200 OK'
        elif status_id == mapscript.MS_FAILURE:
            status = '400 Bad request'

        # create wsgiref response
        headers = [
            ('Content-type', str(content_type)),
        ]
        start_response(status, headers)
        return [result]
    
    def wsgi(self):
        httpd = make_server(
            self.wsgi_host,
            self.wsgi_port,
            self.application
        )
        print('Serving on port %d...' % self.wsgi_port)
        httpd.serve_forever()
        
    def __call__(self):
        self.wsgi()
        

if __name__ == "__main__":
    map_web = PubMapWEB(sys.argv[1])
    map_web.wsgi()
