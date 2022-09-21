function solution(s) {
    let result = [0,0];
    while(s.length > 1){
        let t = s.split("").reduce((acc, e) => acc + parseInt(e), 0)
        result[0]++;
        result[1] += (s.length - t);
        s = t.toString(2)
    }
    return result;
}