function solution(n) {
    let a = 1;
    let b = 2;
    let r = 2
    while(n>r){
        tmp = (a+b)%1000000007;
        a = b;
        b = tmp;
        r++;
    }
    return b;
}