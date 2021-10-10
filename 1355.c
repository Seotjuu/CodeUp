// CodeUp :: 1355

#include<stdio.h>
int main(){
    int n,i,j,k;
    scanf("%d",&n);
    
    for(i=0;i<n;i++){
        for(j=0;j<i;j++){
            printf(" ");
        }
        for(k=n;k>i;k--){
            printf("*");
        }
        printf("\n");
    }
}


