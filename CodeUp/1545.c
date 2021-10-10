// CodeUp :: 1545

#include <stdio.h>

int n;



#include<stdbool.h>
bool zero(int a){
    if(a==0){
        return true;
    }
    else{
        return false;
    }
}
int main()
{
  scanf("%d", &n);
  if(zero(n)) printf("zero");
  else printf("non zero");
  return 0;
}
