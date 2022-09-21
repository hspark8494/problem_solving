//Q12940 최대공약수와 최소공배수
//https://programmers.co.kr/learn/courses/30/lessons/12940
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