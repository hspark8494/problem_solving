// Q87946 피로도
// https://school.programmers.co.kr/learn/courses/30/lessons/87946
function solution(k, dungeons) {
    let length = dungeons.length;
    result = 0;
    const calc = () => {
        let ck = k;
        let tempResult = 0;
        for(let s=0; s<length; s++){
            if(ck>=dungeons[s][0]){
                tempResult++;
                ck-=dungeons[s][1]
            }
        }
        if(tempResult>=result){
            result = tempResult;
        }
    }
    calc()
    let c = new Array(length).fill(0);
    let i = 1, d, p;
    while (i < length) {
        if (c[i] < i) {
            d = i % 2 && c[i];
            p = dungeons[i];
            dungeons[i] = dungeons[d];
            dungeons[d] = p;
            c[i]++;
            i = 1;
            calc()
        } else {
            c[i] = 0;
            i++;
        }
    }
    return result;
}