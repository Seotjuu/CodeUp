// CodeUp :: 1078

#include<stdio.h>
int main(){
    int a,sum=0;
    scanf("%d",&a);
    for(int i=1;i<=a;i++){
        if(i%2==0){
            sum=sum+i;
        }
    }
    printf("%d",sum);
        
}

