#include <arpa/inet.h>
#include <netinet/in.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

#include <cstdio>

int main(int argc, char const *argv[]) {
    int sockfd;
    if ((sockfd = socket(PF_INET, SOCK_STREAM, 0)) == -1) {
        printf("create socket failed.\n");
        return -1;
    }
    struct sockaddr_in addr;
    struct sockaddr_in their_addr;
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8090);
    bzero(&addr.sin_zero, 8);

    if (bind(sockfd, (sockaddr *)&addr, sizeof(struct sockaddr)) == -1) {
        printf("bind failed.\n");
        return -1;
    }
    if (listen(sockfd, 10) == -1) {
        printf("listen failed.\n");
        return -1;
    }

    return 0;
}
