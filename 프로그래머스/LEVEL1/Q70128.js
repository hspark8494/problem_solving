//Q70128 내적
//https://programmers.co.kr/learn/courses/30/lessons/70128
let solution = (a, b) => a.reduce((acc,curr,idx) => acc+curr*b[idx],0)