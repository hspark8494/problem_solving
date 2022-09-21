function solution(n, m) {
    let nm = n*m
    if(m>n){
        let temp = n;
        n = m;
        m = temp;
    }
    while(m != 0){
        let r = n%m;
        n = m;
        m = r;
    }

    return [n, nm/n];
}