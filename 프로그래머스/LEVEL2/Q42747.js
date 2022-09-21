//Q42747 H-Index
//https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=javascript
function solution(citations) {
    citations.sort((a,b) => b-a);
    for(let i=0; i<citations.length; i++){
        if(i+1>=citations[i]) return i;
    }
    return citations.length;
}

console.log(solution([4,4,4]))