// CodeUp :: 1460

#include<stdio.h>
int main(){
    int i,j,n,a=0;
    scanf("%d",&n);
    
    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            a=a+1;
            printf("%d ",a);
        }
        printf("\n");
    }
}
