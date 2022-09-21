// Q42888 오픈채팅방
// https://school.programmers.co.kr/learn/courses/30/lessons/42888
function solution(record) {
    const dict = {}
    let answer = []
    for(let s of record){
        let token = s.split(" ");
        if(token[2]) dict[token[1]] = token[2];
        if(token[0] !== "Change") answer.push({act : token[0], id : token[1]})
    }

    return answer.map(e => dict[e.id] + '님이 ' + ((e.act==="Enter") ? '들어왔습니다.' : "나갔습니다."));
}