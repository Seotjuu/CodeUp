// CodeUp :: 1163

#include<stdio.h>
int main(){
    int yy,mm,dd,sum=0;
    scanf("%d %d %d",&yy,&mm,&dd);
    
    sum=(yy+mm+dd)%200;
    if(sum<100){
        printf("대박");
    }
    else{
        printf("그럭저럭");
    }
}
