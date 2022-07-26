# 웹과 관련된 컴포넌트들

## 1. [웹소캣](/Web/WebSocket/)

전이중 통신을 지원하는 웹소켓에 대한 예제  
웹소켓과, 이를 쓰기 편하게 만든 라이브러리인 SocketIO에 대해 알아봄.  
웹소켓은 브라우저에서 자체적으로 지원하는 프로토콜임. 하지만 구형 브라우저들은 웹소켓을 지원하지 않을 수 있다.  
SocketIO는 웹소켓과, 웹소켓을 지원하지 않는다면 poll방식으로 웹소켓과 비슷한 경험을 할 수 있게 해주는 라이브러리임.  
이 예제에서는 웹소켓을 그대로 사용하는 방법과, socketIO를 통해 사용하는 방법을 알아봄.  

### 1.1 [웹소캣](/Web/WebSocket/WebSocket/)

#### 1.1.1 [파이썬](/Web/WebSocket/WebSocket/Python/)

웹소켓 서버는 비동기로 동작함. 파이썬의 경우 asyncio나 tornado, celery등을 사용한다.  
이 예시들은 웹소켓을 사용한 에코서버의 예시를 다룬다.  

#### [서버](/Web/WebSocket/WebSocket/Python/server/) 실행

```bash
python3 server.py
```

#### [클라](/Web/WebSocket/WebSocket/Python/client/) 실행

```bash
npm start
```

#### 1.1.2 [노드](/Web/WebSocket/WebSocket/Node/)

#### [서버](/Web/WebSocket/WebSocket/Node/server/) 실행

```bash
node server.js
```

#### [클라](/Web/WebSocket/WebSocket/Node/client/) 실행

```bash
npm start
```

### 1.2 [SocketIO](/WEb/WebSocket/SocketIO/)

SocketIO는 웹소켓을 캡슐화하여 사용하기 편하게 만든 라이브러리로써, 범용성이 높음.  
SocketIO는 emit()을 통해 특정 이벤트를 송수신 하거나, send를 통해 메시지를 송수신할 수 있음  

#### 송신

```javascript
sock.emit("event name", "event content"); // 이벤트 전송
sock.send("message"); // 메시지 전송 (메시지도 결국 message라는 이벤트)
```

#### 수신

```javascript
sock.on('event name', ...)                      // 이벤트 수신
sock.on('message')                              // 메시지 수신 (메시지도 결국 message라는 이벤트)
```

#### 1.2.1 [노드](/Web/WebSocket/SocketIO/Node/)

#### [서버](/Web/WebSocket/SocketIO/Node/server/) 실행

```bash
node server.js
```

#### [클라](/Web/WebSocket/SocketIO/Node/client/) 실행

```bash
npm start
```

#### 1.2.2 [파이썬](/Web/WebSocket/SocketIO/Python/)

#### [서버](/Web/WebSocket/SocketIO/Python/server/) 실행

```bash
python3 server.py
```

#### [클라](/Web/WebSocket/SocketIO/Python/client/) 실행

```bash
npm start
```

### 1.3 [채팅](/Web/Chat)

여러명의 사람이 동시에 참여 가능한 채팅방.  
![image](/Image/Web/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-11-08%2023.11.30.png)

#### [서버](/Web/Chat/server/) 실행

```bash
node server.js
```

#### [클라](/Web/Chat/client/) 실행

```bash
npm start
```

### 1.4 [웹 SSh 콘솔](/Web/WebSSH)

웹상에서 ssh 콘솔을 사용하기 위한 예제.  
![image](/Image/Web/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-11-08%2023.43.06.png)

위 그림과 같이 클라이언트는 웹서버와, 웹서버는 SSH서버와 통신을 하게 되어있다.
또한 실시간 전이중 통신을 위해 웹서버에서는 SSH서버와 통신하기 위한 쓰레드와, 클라이언트와 통신하기 위한 쓰레드를 별도로 분리하여 동작시킨다.

```python
async def recv_msg(ws, ssh:Channel):
    while ssh.closed == False:
        msg = ssh.recv(1000)
        await ws.send(msg.decode())
```
별도의 쓰레드에서 동작하는 코루틴, 이 코루틴의 목적은 ssh서버로부터 변화된 데이터를 받아(recv) 웹소켓으로 데이터를 넘겨주는 역할을 함.  
 
#### [서버](/Web/WebSSH/server/) 실행
```bash
python3 server.py
```

#### [클라](/Web/WebSSH/client/) 실행
```bash
npm start
```

sample  
![image](/Image/Web/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-11-09%2000.59.01.png)
![image](/Image/Web/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202022-11-09%2000.59.04.png)


### 1.5 [웹 동시 편집](/Web/MultiEdit/)
웹상에서 동일한 에디터로 편집하기 위함.  
![image](/Image/Web/%ED%99%94%EB%A9%B4%20%EA%B8%B0%EB%A1%9D%202022-11-09%2013.16.58.gif)

웹소켓을 통해 자신을 제외한 서버에 연결된 모든 웹소켓에 내용을 전달함.
#### [서버](/Web/MultiEdit/server/) 실행
```bash
node server.py
```

#### [서버](/Web/MultiEdit/client/) 실행
```bash
npm start
```