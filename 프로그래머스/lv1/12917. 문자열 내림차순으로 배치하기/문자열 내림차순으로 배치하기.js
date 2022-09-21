function solution(s) {
    const li = [...s];
    for (let i = 0; i < li.length; i++) {
        let max = li[i];
        let idx = i;
        for (let j = i; j < li.length; j++) {
            if(li[j]>=max){
                idx = j;
                max = li[j]
            }
        }
        let temp = li[i];
        li[i] = li[idx];
        li[idx] = temp;
    }
    return li.join("");
}