//Q12947 하샤드 수
//https://programmers.co.kr/learn/courses/30/lessons/12947
function solution(x) {
    return x%[...x+''].reduce((acc, e)=> parseInt(acc)+parseInt(e))==0;
}
