//Q77884 약수의 개수와 덧셈
//https://programmers.co.kr/learn/courses/30/lessons/77884
function solution(left, right) {
    let result = 0;
    for(;left<=right; left++){
        result += (Number.isInteger(Math.sqrt(left)) ? -1 : 1) * left;
    }
    return result;
}