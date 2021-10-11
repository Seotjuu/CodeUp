// CodeUp :: 2001

#include<stdio.h>
int main(){
    int P1,P2,P3,J1,J2,S=0;
    scanf("%d %d %d %d %d",&P1,&P2,&P3,&J1,&J2);
    
    //파스타 최소 가격
    if(P1<=P2){
        if(P1<=P3){
            S+=P1;
        }
        else{
            S+=P3;
        }
    }
    else if(P2<=P1){
        if(P2<=P3){
            S+=P2;
        }
        else{
            S+=P3;
        }
    }
    else if(P3<=P1){
        if(P3<=P2){
            S+=P3;
        }
        else{
            S+=P2;
        }
    }
    
    //생과일 주스 최소 가격
    if(J1<=J2){
        S+=J1;
    }
    else{
        S+=J2;
    }
    
    
    printf("%.1f",S*1.1);
    
    
}
