#include <arpa/inet.h>
#include <fcntl.h>
#include <netinet/in.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

#include <cstdio>
#include <vector>

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
    int flags = fcntl(sockfd, F_GETFL, 0);
    fcntl(sockfd, F_SETFL, flags | O_NONBLOCK);
    std::vector<int> connections;
    while (true) {
        // printf("111\n");
        socklen_t sin_size = (socklen_t)sizeof(struct sockaddr_in);
        int newfd =
            accept(sockfd, (sockaddr *)&their_addr, (socklen_t *)&sin_size);
        // printf("222\n");
        if (newfd != -1) {
            printf("new connection... fd=%d\n", newfd);
            connections.push_back(newfd);
            // printf("accept failed;\n");
            // return -1;
        }
        for (const auto &conn : connections) {
            char *buffer = new char[1024];
            int ret = recv(conn, buffer, 1024, 0);
            if (ret > 0) {
                // printf("recv failed;\n");
                // continue;
                // return -1;
                buffer[ret] = '\0';
                printf("Receive client request from [%d], size: %d: %s\n", conn,
                       ret, buffer);
                char send_buf[1040] = "hello, client: ";
                strncat(send_buf, buffer,
                        sizeof(send_buf) - strlen(send_buf) - 1);
                if (send(conn, send_buf, 1040, 0) == -1) {
                    printf("send failed;\n");
                    // return -1;
                }
            } else if (ret == 0) {
                auto it =
                    std::find(connections.begin(), connections.end(), conn);
                if (it != connections.end()) {
                    printf("Connection disconnect... fd=%d\n", conn);
                    shutdown(conn, 2);
                    connections.erase(it);
                }
            }
            delete[] buffer;
        }
        // printf("end...\n");
        // sleep(1);
    }
    for (const auto &conn : connections) {
        shutdown(conn, 2);
    }

    return 0;
}
