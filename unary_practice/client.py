from __future__ import print_function

import grpc

import unary_practice.hello_pb2 as hello_pb2
import unary_practice.hello_pb2_grpc as hello_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = hello_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(hello_pb2.HelloRequest(name='yeonsu', num=1, has_boolean=True))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()