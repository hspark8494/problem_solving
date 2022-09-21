//Q12948 핸드폰 번호
//https://programmers.co.kr/learn/courses/30/lessons/12948?language=javascript
function solution(e) { 
   return "*".repeat(e.length-4) + e.slice(-4);
}