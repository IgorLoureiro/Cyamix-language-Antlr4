#include <stdio.h>

void main() {
    int i = 0;
    do {
        printf("i: %d\n", i);
        i = i + 1;
    }
    while (i < 3);
}