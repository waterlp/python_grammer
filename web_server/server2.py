# coding=utf-8
from http.server import BaseHTTPRequestHandler,HTTPServer
# from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import urllib
import cgi


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()  # 发送\r\n,意味这下一行为报体
        # send html message,
        file =  open('./html/index.html','rb').read()
        # self.wfile.write('hello,nanxiaoting'.encode())
        self.wfile.write(file)
        return

class PostHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        # Begin the response
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Client: %s\n' % str(self.client_address))
        self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
        self.wfile.write('Path: %s\n' % self.path)
        self.wfile.write('Form data:\n')
        # Echo back information about what was posted in the form
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # The field contains an uploaded file
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                self.wfile.write('\tUploaded %s as "%s" (%d bytes)\n' % \
                        (field, field_item.filename, file_len))
            else:
                # Regular form value
                self.wfile.write('\t%s=%s\n' % (field, form[field].value))
        return



if __name__ == '__main__':  # 注意main后面没有括号
    try:
        server = HTTPServer(('', 8080), GetHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print
        '^c received,shutting down the web server!'

# if __name__ == '__main__':
# #     from BaseHTTPServer import HTTPServer
# #     server = HTTPServer(('localhost', 8080), PostHandler)
# #     print 'Starting server, use <Ctrl-C> to stop'
# #     server.serve_forever()