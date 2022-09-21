//Q12934 정수 제곱근 판별
//https://programmers.co.kr/learn/courses/30/lessons/12934
function solution(n) {
    let r = Math.sqrt(n)
    if(!Number.isInteger(r)) return -1
    
    return Math.pow((r+1),2);
}