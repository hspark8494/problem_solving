// Q12982 예산
// https://school.programmers.co.kr/learn/courses/30/lessons/12982
function solution(d, budget) {
    const arr = d.sort((a,b)=>a-b);
    let result = arr.length;
    while(result>0){
        for(let i=0; i+result<=arr.length; i++){
            let acc = arr.slice(i, result+i).reduce((acc, e) => acc+e);
            if(acc<=budget){
                return result;
            }
        }
        result--;
    }

    return result;
}
