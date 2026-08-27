from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from gemini_api import ask_gemini


def read_file(path):
    with open(path, "rb") as file:
        return file.read()


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html;charset=utf-8")
            self.end_headers()
            self.wfile.write(read_file("static/index.html"))

        if self.path == "/script.js":
            self.send_response(200)
            self.send_header("Content-type", "application/javascript")
            self.end_headers()
            self.wfile.write(read_file("static/script.js"))

    def do_POST(self):
        if self.path == "/chat":
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            data = json.loads(body)
            user_message = data["message"]
            ai_reply = ask_gemini(user_message)

            response = {"reply": ai_reply}

            json_data = json.dumps(response)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(json_data.encode())


server = HTTPServer(("localhost", 8000), MyServer)
print("chatbot is ready!")
server.serve_forever()
