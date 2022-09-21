//Q42576 완주하지 못한 선수
//https://programmers.co.kr/learn/courses/30/lessons/42576?language=javascript
function solution(participant, completion) {
    var dict = {};
    participant.forEach(e => dict[e] ? dict[e]++ : dict[e]=1);
    completion.forEach(e=>{
        if(dict[e]>1){
            dict[e]-=1;
        }else{
            delete dict[e]
        }
    })
    return Object.keys(dict)[0];
}