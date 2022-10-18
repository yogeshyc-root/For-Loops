#include<stdio.h>

int n=5 , num=10;

void main(){
    for(int i = 0;i<=n;i++){
        num = 10;
        for(int j = 0;j<i;j++){
            printf("%d ",num);
            num-=2;
        }
        printf("\n");
    }
}