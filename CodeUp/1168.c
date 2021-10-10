// CodeUp :: 1168

#include<stdio.h>
int main(){
    int A,B,AA=1;
    scanf("%d %d",&A,&B);
    
    A/=10000;
    
    if(B==1 || B==2){
        while(1){
            AA++;
            A++;
            if(A==112){
                break;
            }
        }
    printf("%d", AA);
    }
    
    else if(B==3 || B==4){
        while(1){
            AA++;
            A++;
            if(A==12){
                break;
            }
        }
    printf("%d", AA);
    }
    
    
}
