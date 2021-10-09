// CodeUp :: 1024

#include<stdio.h>
int main(){
    char A[20]={};
    scanf("%s", A);
    for(int i=0;A[i]!='\0';i++){
        printf("\'%c\'\n",A[i]);
    }
}
