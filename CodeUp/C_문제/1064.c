// CodeUp :: 1064

#include<stdio.h>
int main(){
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);//5 -1 3
    printf("%d",(a<b?a:b)<c?(a<b?a:b):c);
}
