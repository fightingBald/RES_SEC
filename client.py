# _*_ coding : utf-8 _ * _ 
# @Time : 30/09/2022 16:50
# @Author : Huayi TANG
# File : client
# @Project : RES_SEC

import socket
import threading
from datetime import time

LOCAL_HOST = "127.0.0.1"
PORT_TO_CONNECT = 6666


if __name__ == '__main__':
    #创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接。
    socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_client.connect((LOCAL_HOST,PORT_TO_CONNECT))
    #发送数据 TODO b代表 转成byte流的形式发送
    socket_client.send(b'hello')
    #socket_client。recv FROM服务器 消息
    #字节流解码成utf-8
    msg_recv = socket_client.recv(1024).decode('utf-8')
    print(msg_recv)
    socket_client.close()



