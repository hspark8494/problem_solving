function solution(N, stages) {
    stages = stages.sort((a,b) => b-a);
    const answer = [];
    for(let i=1; i<=N; i++){
        let clear = 0;
        let total = 0;
        for(let j=0; j<stages.length; j++){
            if(stages[j]>i){
                clear++;
            }
            if(stages[j]>=i){
                total++;
            }else{
                break;
            }
        }
        answer.push([i,clear/total]);
    }
    return answer.sort((a,b) => a[1]-b[1]).map(a=>a[0]);
}