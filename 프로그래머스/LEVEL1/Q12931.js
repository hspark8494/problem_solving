//Q12931 자릿수 더하기
//https://programmers.co.kr/learn/courses/30/lessons/12931
let solution = (n) => [...n.toString()].reduce((acc, e) => acc + parseInt(e), 0);