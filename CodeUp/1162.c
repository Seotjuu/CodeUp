// CodeUp :: 1162

#include<stdio.h>
int main(){
    int yy,mm,dd,sum=0;
    scanf("%d %d %d",&yy,&mm,&dd);
    sum=yy-mm+dd;
    if(sum%10==0){
        printf("대박");
    }
    else{
        printf("그럭저럭");
    }
}
