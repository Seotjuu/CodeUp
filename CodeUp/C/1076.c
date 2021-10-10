// CodeUp :: 1076

#include<stdio.h>
int main(){
    char x,a='a';
    scanf("%c",&x);
    do{
        printf("%c ",a);
        a=a+1;
    }while(a!=x+1);
}
