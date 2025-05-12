from http.server import BaseHTTPRequestHandler, HTTPServer

from utils import open_html_file

data = open_html_file('category1.html')

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """Класс отвечает за обработку входящих запросов от клиентов"""

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(data, "utf-8"))

    def do_POST(self):
        """Метод для обработки входящих POST-запросов"""

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body)
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
