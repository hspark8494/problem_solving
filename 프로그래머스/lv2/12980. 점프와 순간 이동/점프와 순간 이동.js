function solution(n){
    let result = 0;
    while(n>0){
        if(n%2!=0){
            result++;
            n--;
        }else{
            n=parseInt(n/2);
        }
    }

    return result;
}