#include <arpa/inet.h>
#include <netinet/in.h>
#include <string.h>
#include <sys/socket.h>

#include <cstdio>

int main(int argc, char const *argv[]) {
    /* code */
    int sockfd;
    if ((sockfd = socket(PF_INET, SOCK_STREAM, 0)) == -1) {
        printf("create socket failed.\n");
        return -1;
    }
    struct sockaddr_in addr;
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8090);
    bzero(&addr.sin_zero, 8);
    if (connect(sockfd, (sockaddr *)&addr, sizeof(struct sockaddr)) == -1) {
        printf("connect failed.\n");
        return -1;
    } else {
        printf("connect successful.\n");
    }
    while (true) {
        char send_buf[1024] = "hello, server";
        if (send(sockfd, send_buf, 1024, 0) == -1) {
            printf("send failed;\n");
            return -1;
        }

        char buffer[1024];
        if (recv(sockfd, buffer, 1024, 0) == -1) {
            printf("recv failed;\n");
            return -1;
        }
        printf("Receive server response: %s\n", buffer);
    }
    shutdown(sockfd, 2);

    return 0;
}
