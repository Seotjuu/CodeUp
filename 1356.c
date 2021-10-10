// CodeUp :: 1356

#include<stdio.h>
int main(){
    int n,i,j,k;
    scanf("%d",&n);
    
    for(i=1;i<=n;i++){
        if(i==1 || i==n){
            for(j=1;j<=n;j++){
                printf("*");
            }
        }
        else if(i!=1 || i!=n){
            for(k=1;k<=n;k++){
                if(k==1 || k==n){
                    printf("*");
                }
                else{
                    printf(" ");
                }
            }
        }
        printf("\n");
    }
}
