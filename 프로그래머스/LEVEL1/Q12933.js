//Q12933 정수 내림차순으로 배치하기
//https://programmers.co.kr/learn/courses/30/lessons/12933
function solution(n) {
    const arr = new Array(10).fill(0);
    [...n+""].forEach(e=>arr[parseInt(e)]++)
    return parseInt(arr.reverse().reduce((acc,curr,i) => acc+(9-i).toString().repeat(curr),""));
}