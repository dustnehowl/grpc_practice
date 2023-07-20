from concurrent import futures
import time

import grpc

import hello_pb2 as hello_pb2
import hello_pb2_grpc as hello_pb2_grpc
import numpy as np

class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(request.name)
        return hello_pb2.HelloReply(message=f'Hello, {request.name}!, {request.num}!, {request.has_boolean}!')
    
    def Diffusion(self, request, context):
        print(request.prompt)
        image_np = np.frombuffer(request.image, dtype=np.uint8)
        # 이미지 데이터의 shape 출력
        print("Image shape:", image_np.shape)
        with open('request_image.jpg', 'wb') as f:
            f.write(request.image)
        print("서버 응답 이미지를 'response_image.jpg'로 저장하였습니다.")
        return hello_pb2.Response(image=request.image)


def serve():
    print("start server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()