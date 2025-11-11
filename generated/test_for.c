#include <stdio.h> 

void main() {
int i;
int sum;
sum = 0;
for (i = 0; i < 5; i = i + 1) {
sum = sum + i;
}
printf("Total sum: %d", sum);
}
