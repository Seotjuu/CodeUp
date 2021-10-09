// CodeUp :: 1087

#include<stdio.h>
int main(){
    int i,s=0,a;
    scanf("%d",&a);
    for(i=1;i<=a;i++){
        if(a<=s){
            break;
        }
        else{
            s=s+i;
        }
    }
    
    printf("%d",s);
}
