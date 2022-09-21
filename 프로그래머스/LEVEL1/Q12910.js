//Q12910 나누어 떨어지는 숫자 배열
//https://programmers.co.kr/learn/courses/30/lessons/12910
function solution(arr, divisor) {
    const result = arr.filter(e=> e%divisor==0).sort((a,b)=>a-b);
    return result.length>0 ? result : [-1];
}