// CodeUp :: 1358

#include<stdio.h>
int main(){
    int n,i,j,k;
    scanf("%d",&n);
    
    for(i=0;i<n/2+1;i++){
    	for(j=0;j<n/2-i;j++){
    		printf(" ");
		}
		for(k=0;k<i*2+1;k++){
			printf("*");
		}
		printf("\n");
    	
	}
}
