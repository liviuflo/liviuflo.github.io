from livereload import Server, shell

# Initialize the server
server = Server()

# Watch the current directory for changes
server.watch(".", shell("python -m http.server"))

# Start the server at the default port 8000
server.serve(port=8000, host="127.0.0.1")
