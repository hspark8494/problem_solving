//Q12909 올바른 괄호
//https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=javascript
function solution(s) {
    let closeBrace = 0;

    for(let i=s.length-1; i>=0; i--){
        if (s[i] == ")") {
            closeBrace++;
        } else {
            closeBrace--;
        }
        if(closeBrace<0){
            return false;
        }
    }
    return closeBrace==0;
}