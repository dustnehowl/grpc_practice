# Overview
프로토콜 버퍼는 구조화 된 데이터를 직렬화하기 위한 언어 중립적이고 플랫폼에 구애받지 않는 확장 가능한 매커니즘이다.

Json과 비슷하지만 더 작고 빠르다. native language bindings을 생성한다. 데이터를 어떻게 구조화할지 한 번 정의하면, 특수하게 생성된 소스 코드를 사용하여 다양한 데이터 스트림과 다양한 언어를 사용하여 구조화된 데이터를 쉽게 쓰고 읽을 수 있다.

프로토콜 버퍼는 정의 언어(.proto), 프로토 컴파일러가 데이터와 인터페이스 하기 위해 생성하는 코드, 언어별 런타임 라이브러리, 파일에 기록되거나 네트워크 연결을 통해 전송되는 데이터의 직렬화 형식의 조합으로 구성된다.
# What Problems do Protocol Buffers Solve?
프로토콜 버퍼는 최대 수 메가바이트 크기의 정형화된 데이터 패킷을 위한 직렬화 형식을 제공한다. 이 형식은 임시 네트워크 트래픽과 장기 데이터 저장 모두에 적합하다. 프로토콜 버퍼는 기족 데이터를 무효화하거나 코드를 업데이트할 필요 없이 새로운 정보로 확장할 수 있다.

프로토콜 버퍼는 구글에서 가장 일반적으로 사용되는 데이터 형식이다. 서버 간 통신은 물론 디스크에 데이터를 보관할 때에도 광범위하게 사용된다. 프로토콜 버퍼 메시지와 서비스는 엔지니어가 작성한 .proto 파일로 설명된다.


```
message Person {
  optional string name = 1;
  optional int32 id = 2;
  optional string email = 3;
}
```

프로토 컴파일러는 빌드 시 .proto파일에서 호출되어 해당 프로토콜 버퍼를 조작하기 위해 다양한 프로그래밍 언어로 코드를 생성한다. 생성된 각 클래스에서 각 필드에 대한 간단한 접근자와 전체 구조를 원시 바이트열로 직렬화하고 구문 분석하는 메서드가 포함되어 있다.

```
Person john = Person.newBuilder()
    .setId(1234)
    .setName("John Doe")
    .setEmail("jdoe@example.com")
    .build();
output = new FileOutputStream(args[0]);
john.writeTo(output);
```

프로토콜 버퍼는 구글의 모든 서비스에서 광범위하게 사용되며 그 안의 데이터는 한동안 지속될 수 있으므로 이전 버전과의 호환성을 유지하는 것이 매우 중요하다. 프로토콜 버퍼를 사용하면 기존 서비스를 중단하지 않고도 프로토콜 버퍼에 새 필드를 추가하거나 기존 필드를 삭제하는 등의 변경 사항을 원활하게 지원할 수 있다.
# What are the Benefits of Using Protocol Buffers? 
프로토콜 버퍼는 언어에 구애받지 않고 플랫폼에 구애받지 않으며 확장 가능한 방식으로 구조화된 레코드형 데이터를 직렬화해야 하는 모든 상황에 이상적이다. 프로토콜 버퍼는 통신 프로토콜을 정의하는 데 가장 많이 사용되며(gRPC와 함께), 데이터 저장에 사용된다.
### Some of advantages of using protocol buffers include:
1. 컴팩트한 데이터 저장
2. 빠른 파싱
3. 다양한 프로그래밍 언어 사용성
4. 자동 생성 클래스를 통한 기능 최적화
## Cross-language Compatibility
지원되는 모든 프로그래밍 언어로 작성된 코드로 동일한 메시지를 읽을 수 있다. 한 플랫폼의 Java프로그램이 한 소프트웨어 시스템에서 데이터를 캡쳐하고 .proto정의에 따라 직렬화한 다음 다른 플랫폼에서 실행되는 별도의 Python 애플리케이션에서 직렬화된 데이터에서 특정 값을 추출하도록 할 수 있다.
### 지원하는 언어
* C++
* C#
* Java
* Kotlin
* Objective-C
* PHP
* Python
* Ruby
## Cross-project Support
특정 프로젝트의 코드 베이스 외부에 있는 .proto 파일에 메시지 유형을 정의하여 프로젝트 전반에서 프로토콜 버퍼를 사용할 수 있다. 팀 외부에서 널리 사용될 것으로 예상되는 메시지 유형이나 열거 형을 정의하는 경우에는 종속성 없이 자체 파일에 넣을 수 있다.
## Updating Proto Definitions Without Updating Code
소프트웨어 제품이 이전 버전과 호환되는 것은 표준이지만, 실제로 호환되는 경우는 흔치 않다. .proto정의를 업데이트 할 때 몇가지 간단한 관행을 따르는 한, 이전 코드는 새로 추가된 필드를 무시하고 문제 없이 새 메시지를 읽을 수 있다. 이전 코드에서 삭제된 필드는 기본값을 가지며, 삭제된 반복 필드는 비어 있다.
## When are Protocol Buffers not a Good Fit?
* 메모리에 담을 수 있다고 가정하기 때문에 아주 큰 용량은 다른 방법을 고려해야한다.
* 파싱 없이는 두 메시지가 같은 내용을 담고 있는지 비교하기 힘들다.
## Who Uses Protocol Buffers?
* gRPC
* Google CLoud
* Envoy Proxy
## How do Protocol Buffers Work?
