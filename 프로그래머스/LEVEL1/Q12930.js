//Q12930 이상한 문자 만들기
//https://programmers.co.kr/learn/courses/30/lessons/12930
function solution(s) {
    return s.split(" ").map(s => [...s].map( (e,idx) => idx%2 ? e.toLowerCase() : e.toUpperCase()).join("")).join(" ");
}