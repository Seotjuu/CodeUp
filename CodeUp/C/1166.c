// CodeUp :: 1166

#include<stdio.h>
int main(){
    int year,a;
    scanf("%d",&year);
    
    if((year%4==0 && year%100!=0) || year%400==0){
        printf("yes");
    }
    else{
        printf("no");
    }
}
