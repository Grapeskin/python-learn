#include <cstdio>

#include "version.h"
#ifdef USE_SUPER_PRINT
#define T 123
#include "super_print.h"
#endif

// void super_print();
int main(int argc, char const *argv[]) {
    printf("version: %s\n", version);
#ifdef USE_SUPER_PRINT
    printf("%d", T);
    printf("111\n");
    super_print();
#endif
    return 0;
}
