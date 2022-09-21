//Q12906 같은 숫자는 싫어
//https://programmers.co.kr/learn/courses/30/lessons/12906
function solution(arr)
{
    let answer = [arr[0]];
    for(let i=1; i<arr.length; i++){
        if(answer[answer.length-1]!=arr[i]){
            answer.push(arr[i])
        }
    }
    return answer;
}