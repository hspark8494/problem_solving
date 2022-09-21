// Q43162 네트워크
// https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=javascript
function solution(n, computers) {
    let result = 0;
    li = [];
    for(let i=0; i<computers.length; i++){
        li.push({ 
            index:i, 
            node:computers[i], 
            visited:false
        })
    }
    for(let l of li){
        if(!l.visited){
            l.visited = true;
            result++;
            bfs(l)
        }
    }
    function bfs(k){
        for(let i=0; i<k.node.length; i++){
            if(k.node[i] == 1 && !li[i].visited){
                li[i].visited = true;
                bfs(li[i])
            }
        }
    }
    return result;
}
