// CodeUp :: 1096

#include<stdio.h>
int main(){
    int i,j,A[20][20]={},n, X, Y;
    scanf("%d", &n);
    for(i=1;i<=n;i++){
        scanf("%d %d", &X, &Y);
        A[X][Y]=1;
    }
    for(i=1;i<=19;i++){
        for(j=1;j<=19;j++){
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }
    
}
