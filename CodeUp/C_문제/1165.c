// CodeUp :: 1165

#include<stdio.h>
int main(){
    int score, time, i;
    scanf("%d %d",&time,&score);
    
    for(i=time;i<90;i+=5){
        score++;
    }
    printf("%d",score);
}
