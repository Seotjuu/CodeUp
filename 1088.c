// CodeUp :: 1088

#include<stdio.h>
int main(){
    int i,A;
    scanf("%d",&A);
    for(i=1;i<=A;i++){
        if(i%3==0){
            continue;
        }
        printf("%d ",i);
    }
}
