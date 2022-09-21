function solution(n) {
    const num = (n).toString(2).split("").reduce((acc, curr) => acc += (curr=="1"), 0);
    while(true){
        n++;
        if(num == (n).toString(2).split("").reduce((acc, curr) => acc += (curr=="1"), 0)){
            return n;
        }
    }
}