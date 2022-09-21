function solution(n, arr1, arr2) {
    var answer = [];
    for(let i=0; i<arr1.length; i++){
        let tmp = (arr1[i] | arr2[i]).toString(2);
        let t = ""
        for(let c of tmp){
            t += (c=="1" ? "#" : " ")
        }
        answer.push(t.padStart(n," "));
    }
    return answer;
}