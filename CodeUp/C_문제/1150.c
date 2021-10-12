// CodeUp :: 1150

#include<stdio.h>
int main(){
    int a,b,c,min=0;
    scanf("%d %d %d",&a,&b,&c);
    
    min = a<=b ? (a<=c ? a : c) : (b<=c ? b : c);
    printf("%d",min);
}