function solution(n) {
    s = new Set();
    for(let i=1; i<=Math.ceil(n/2); i++){
        if(n%i==0){
            s.add(i);
            s.add(n/i);
        }
    }
    let result = 0;
    for(let i of s){
        result += i;
    }
    return result;
}