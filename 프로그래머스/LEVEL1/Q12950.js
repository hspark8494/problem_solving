//Q12950 행렬의 덧셈
//https://programmers.co.kr/learn/courses/30/lessons/12950?language=javascript
function solution(arr1, arr2) {
    for(let i=0; i<arr1.length; i++){
        for(let j=0; j<arr1[i].length; j++){
            arr1[i][j]+=arr2[i][j];
        }
    }
    return arr1;
}