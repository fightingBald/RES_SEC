# _*_ coding : utf-8 _ * _
# @Time : 30/09/2022 15:26
# @Author : Huayi TANG
# File : server
# @Project : RES_SEC

import socket
import threading
from datetime import time

LOCAL_HOST = "127.0.0.1"
PORT_LISTEN = 6666


#回调函数
def tcplink(socket_communication, addr):
    print('Accept new connection from %s:%s...' % addr)
    socket_communication.send(b'Welcome!')
    while True:
        data = socket_communication.recv(1024)
        print(data.decode('utf-8'))       #TODO 因为收到的data是b'hello' ，所以要解码

        if not data or data.decode('utf-8') == 'exit':
            break
        socket_communication.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    socket_communication.close()
    print('Connection from %s:%s closed.' % addr)

if __name__ == '__main__':
    socket_listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 监听端口:
    socket_listen.bind((LOCAL_HOST, PORT_LISTEN))
    #TODO socket_listen设置成 关闭socket端口立即释放
    #socket_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_listen.listen(5)
    print('Waiting for connection...')
    while True:
        # 接受一个新连接: 返回两个值 其中addr是返回的客户端的链接
        socket_communication, addr = socket_listen.accept()
        # 创建新线程来处理TCP连接:单线程在处理连接的过程中，无法接受其他客户端的连接：
        #同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。
        t = threading.Thread(target=tcplink, args=(socket_communication, addr))#回调函数=tcplink
        t.start()

