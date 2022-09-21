//Q12911 다음 큰 숫자
//https://school.programmers.co.kr/learn/courses/30/lessons/12911
function solution(n) {
    const num = (n).toString(2).split("").reduce((acc, curr) => acc += (curr=="1"), 0);
    while(true){
        n++;
        if(num == (n).toString(2).split("").reduce((acc, curr) => acc += (curr=="1"), 0)){
            return n;
        }
    }
}