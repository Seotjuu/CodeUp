// CodeUp :: 1072

#include<stdio.h>
int main(){
    int a,b;
    scanf("%d",&a);
    abc:
        scanf("%d",&b);
        if(a--!=0){
            printf("%d\n",b);
            goto abc;
        }
        
}
