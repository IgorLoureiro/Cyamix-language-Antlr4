#include <stdio.h>

void main() {
    char name[] = "";
    int age;
    float height;
    int active;
    printf("Enter your name: ");
    scanf(" %s", &name);
    printf("Enter your age: ");
    scanf("%d", &age);
    printf("Enter your height: ");
    scanf("%f", &height);
    printf("Are you active? (1 for yes, 0 for no): ");
    scanf("%d", &active);
    printf("\nData Summary:\n");
    printf("Age: %d\n", age);
    printf("Height: %.2f\n", height);
    printf("Name: %s\n", name);
    printf("Active: %d\n", active);
}