// CodeUp :: 1169

#include<stdio.h>
int main(){
    int old,YY=112,SS;
    scanf("%d",&old);
    
    for(int i=1;i<old;i++){
        YY--;
    }
    if(YY<100){
        printf("%d 1",YY);
    }
    else if(YY>=100){
        YY-=100;
        printf("%d 3",YY);
    }
    
}
