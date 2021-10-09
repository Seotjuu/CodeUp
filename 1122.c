// CodeUp :: 1122

#include<stdio.h>
int main(){
    int s,m=0,i;
    scanf("%d",&s);
    
    if(s/60!=0){
        for(i=1;i<=s/60;i++){
            m+=1;
        }
    }
    s=s-(m*60);
    printf("%d %d",m,s);
}
