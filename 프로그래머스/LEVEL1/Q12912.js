//Q12912 두 정수 사이의 합
//https://programmers.co.kr/learn/courses/30/lessons/12912?language=javascript
function solution(a, b) {
    let n = Math.abs(a-b)+1;
    return n*(a+b) / 2;
}