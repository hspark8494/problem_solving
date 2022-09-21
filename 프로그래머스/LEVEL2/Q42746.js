// Q42746 가장 큰 수
// https://school.programmers.co.kr/learn/courses/30/lessons/42746
function solution(numbers) {
    let ans = numbers.sort((a,b)=>-String(a).repeat(3).localeCompare(String(b).repeat(3))).join("");
    return ans == 0 ? "0" : ans
}