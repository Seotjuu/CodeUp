// CodeUp :: 1083

#include<stdio.h>
int main(){
    int i,s,x;
    scanf("%d",&x);
    for(i=1;i<=x;i++){
        if(i%3==0){
            printf("X ");
        }
        else{
            printf("%d ",i);
        }
    }
}
