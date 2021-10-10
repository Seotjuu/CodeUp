// CodeUp :: 1158

#include<stdio.h>
int main(){
    float a;
    scanf("%f",&a);
    
    if((a>=30 && a<=40) || (a>=60 && a<=70)){
        printf("win");
    }
    else{
        printf("lose");
    }
}
