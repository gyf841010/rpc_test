from xmlrpclib import ServerProxy
server = ServerProxy("http://localhost:8000")
try:
    ret = server.add(30,90)
    print 'result:', ret
    print 'result type:', type(ret)
except Exception as ex:
    print "exception", ex
