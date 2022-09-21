//Q12980 점프와 순간 이동
//https://school.programmers.co.kr/learn/courses/30/lessons/12980
function solution(n){
    let result = 0;
    while(n>0){
        if(n%2!=0){
            result++;
            n--;
        }else{
            n=parseInt(n/2);
        }
    }

    return result;
}