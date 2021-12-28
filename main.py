# python simple webserver
import http.server
import socketserver
import os

def create_server(port):
    os.chdir('./public')
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", int(port)), Handler)
    print("serving at port", port)
    httpd.serve_forever()

def restart_server(port):
    httpd.shutdown()
    create_server(port)

def handle_command(command):
    if command == "stop":
        httpd.shutdown()
        print("server closed")
    elif command == "start":
        httpd.shutdown()
        port = input("port: ")
        create_server(port)
    elif command == "help":
        print("""
        stop - close server
        restart - restart server
        help - show this message
        """)
    else:
        print("command not found")

def main():
    while True:
        command = get_command()
        handle_command(command)


if __name__ == "__main__":
    main()
