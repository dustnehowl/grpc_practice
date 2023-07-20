from concurrent import futures
import time

import grpc

import unary_practice.hello_pb2 as hello_pb2
import unary_practice.hello_pb2_grpc as hello_pb2_grpc

class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(request.name)
        return hello_pb2.HelloReply(message=f'Hello, {request.name}!, {request.num}!, {request.has_boolean}!')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()