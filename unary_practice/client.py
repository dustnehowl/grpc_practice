from __future__ import print_function
import os
from dotenv import load_dotenv
import grpc
import hello_pb2 as hello_pb2
import hello_pb2_grpc as hello_pb2_grpc

dotenv_path = '../.env'
load_dotenv(dotenv_path)
cvlab_host = os.getenv("CVLAB_HOST")

def run():
    channel = grpc.insecure_channel(cvlab_host)
    stub = hello_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(hello_pb2.HelloRequest(name='yeonsu', num=1, has_boolean=True))
    response2 = stub.Diffusion(hello_pb2.Request(prompt='hi', image=b'sibal'))
    print("Greeter client received: " + response.message)
    print("Diffusion client received: " + response2.image)

def run2():
    # gRPC 서버에 연결합니다. 서버의 주소와 포트를 지정해주세요.
    channel = grpc.insecure_channel(cvlab_host)
    # Greeter 서비스 스텁을 생성합니다.
    stub = hello_pb2_grpc.GreeterStub(channel)
    try:
        print("보내볼게!!!")
        # 이미지 파일을 바이트 배열로 읽어옵니다. 이 예제에서는 'image.jpg'라는 파일을 사용합니다.
        with open('./images/image.jpg', 'rb') as f:
            image_data = f.read()
        # Request 메시지를 생성합니다.
        request = hello_pb2.Request(
            prompt="Image send from macbook!",  # 원하는 프롬프트를 입력합니다.
            image=image_data        # 이미지 데이터를 bytes 필드에 할당합니다.
        )
        # Greeter 서비스의 Diffusion 메서드에 단일 요청으로 Request 메시지를 보내고, 응답을 받습니다.
        response = stub.Diffusion(request)
        # 서버로부터 받은 응답으로 이미지를 저장합니다. 이 예제에서는 'response_image.jpg'라는 파일에 저장합니다.
        with open('./images/response_image.jpg', 'wb') as f:
            f.write(response.image)
        print("서버 응답 이미지를 'response_image.jpg'로 저장하였습니다.")
    except grpc.RpcError as e:
        print(f"오류 발생: {e}")


if __name__ == '__main__':
    run2()