from SimpleXMLRPCServer import SimpleXMLRPCServer
def add(a , b):
    return a+b
server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(add)
server.serve_forever()
