// Q12900 2 x n 타일링
// https://school.programmers.co.kr/learn/courses/30/lessons/12900
function solution(n) {
    let a = 1;
    let b = 2;
    let r = 2
    while(n>=r){
        tmp = (a+b)%1000000007;
        a = b;
        b = tmp;
        r++;
    }
    return b;
}


console.log(solution(300))