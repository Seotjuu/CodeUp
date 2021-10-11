// CodeUp :: 1085

#include<stdio.h>
int main(){
    long long int H, B, C, S;
    float a;
    scanf("%d %d %d %d",&H, &B, &C, &S);
    a = (H * B * C * S)/8;
    a = a / (1024 * 1024);
    printf("%.1f MB", a);
}
