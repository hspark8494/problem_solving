//Q12922 수박수박수박수박수박수?
//https://programmers.co.kr/learn/courses/30/lessons/12922
function solution(n) {
    return "수박".repeat(Math.floor(n/2)) + (n%2 ? "수" : "");
}