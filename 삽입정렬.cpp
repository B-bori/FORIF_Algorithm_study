#include <stdio.h>
int main(){
    int n,i,j,k,d[101], tmp;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d",&d[i]);
    }
    for(i=1;i<n;i++){
        for(j=i;j>0;j--){
            if(d[j]<d[j-1]){
                tmp = d[j];
                d[j] = d[j-1];
                d[j-1] = tmp;
            }
            else{
                break;
            }

        }
    }

    for(i=0;i<n;i++){
        printf("%d ", d[i]);
    }


}
