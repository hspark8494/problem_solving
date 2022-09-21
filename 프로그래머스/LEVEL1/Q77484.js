//Q77484 로또의 최고 순위와 최저 순위
//https://school.programmers.co.kr/learn/courses/30/lessons/77484
function solution(lottos, win_nums) {
    let rank = [6,6,5,4,3,2,1];
    let set = new Set(win_nums);
    let result = lottos.filter(e=>set.has(e)).length;
    let zero = lottos.reduce((acc,e)=> acc+(e==0),0);
    return [rank[result+zero], rank[result]];
}