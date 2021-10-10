// CodeUp :: 1170

#include<stdio.h>
int main(){
    int A,B,C;
    scanf("%d %d %2d",&A,&B,&C);
    
    if(C<10){
        printf("%d%d%02d",A,B,C);
    }
    else{
        printf("%d%d%d",A,B,C);
    }
}
