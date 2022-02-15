#include<stdio.h>

int main(){

    int num_1, num_2, num_3, sum;

    printf("Enter the first number :");
    scanf("%d", &num_1);

    printf("Enter the second number :");
    scanf("%d", &num_2);

    printf("Enter the third number :");
    scanf("%d", &num_3);

    sum = num_1 + num_2 + num_3;
    printf("the sum : %d", sum);
}