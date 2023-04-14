#include <iostream>
#include <cstdio>
// #include "student.h"
// #include "teacher.h"
#define FILE_PREFIX ""
#define SHM_RO_DIR FILE_PREFIX "/tmp/ro/"
#define SHM_WO_DIR FILE_PREFIX "/tmp/wo/"

#define SHM_RO_PATH(PATH) SHM_RO_DIR PATH
#define SHM_WO_PATH(PATH) SHM_WO_DIR PATH

void test(int a, int b, int c)
{
    char result[5];
    itoa(a + b + c, result, 10);
    printf(result);
}

#define PR(...) test(__VA_ARGS__)

using namespace std;

int main(int argc, char const *argv[])
{
    // std::string s = "zhangsan";
    // Student student(s, 23);
    // Teacher teacher(student);

    // std::cout << student.getName() << std::endl;
    // std::cout << "hello, world" << std::endl;
    cout << SHM_RO_PATH("common_node_attr") << endl;
    cout << SHM_WO_PATH("common_node_attr") << endl;
    PR(1, 2, 3);
    return 0;
}
