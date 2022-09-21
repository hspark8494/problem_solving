//Q12939 최댓값과 최솟값
//https://school.programmers.co.kr/learn/courses/30/lessons/12939
function solution(s) {
    let arr = s.split(" ").map(e=>parseInt(e));
    return `${Math.min(...arr)} ${Math.max(...arr)}`;
}