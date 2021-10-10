// CodeUp :: 1161

#include<stdio.h>
int main(){
    int a,b;
    scanf("%d %d",&a,&b);
    
    //짝+짝=짝 홀홀 짝 짝홀 홀 홀짝 홀//
    if(a%2==0){
        if(b%2==0){
            printf("짝수+짝수=짝수");
        }
        else{
            printf("짝수+홀수=홀수");
        }
    }
    else if(a%2==1){
        if(b%2==0){
            printf("홀수+짝수=홀수");
        }
        else{
            printf("홀수+홀수=짝수");
        }
    }
}
