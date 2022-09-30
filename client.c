#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include<netinet/in.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <string.h>
#include <arpa/inet.h>

typedef struct sockaddr_in Socket_addr;

#define SERVER_IP "127.0.0.1"
#define SERVER_PORT 6666

int main(int argc, char *argv[]){
    
    int client_sock = socket(AF_INET, SOCK_STREAM, 0);
    //向服务器（特定的IP和端口）发起请求
    Socket_addr serv_addr;
    memset(&serv_addr, 0, sizeof(serv_addr));  //每个字节都用0填充
    serv_addr.sin_family = AF_INET;  //使用IPv4地址
    serv_addr.sin_addr.s_addr = inet_addr(SERVER_IP);  //具体的IP地址
    serv_addr.sin_port = htons(SERVER_PORT);  //端口
    connect(client_sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr));
   
    //读取服务器传回的数据
    char buffer[40];
    read(client_sock, buffer, sizeof(buffer)-1);
   
    printf("Message form server: %s\n", buffer);
   
    //关闭套接字
    close(client_sock);
    return 0;
    

    
    

}
