//Q12918 문자열 다루기 기본
//https://programmers.co.kr/learn/courses/30/lessons/12918?language=javascript
function solution(s) {
    return (s.length==4 || s.length==6) && [...s].every(e=>parseInt(e)>=0)
}