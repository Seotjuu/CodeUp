// CodeUp :: 1086

#include<stdio.h>
int main(){
    long long int W, H, B;
    float a;
    scanf("%d %d %d",&W, &H, &B);
    a = (W * H * B)/8;
    a = a / (1024 * 1024);
    printf("%.2f MB", a);
}
