function solution(left, right) {
    let result = 0;
    for(;left<=right; left++){
        result += (Number.isInteger(Math.sqrt(left)) ? -1 : 1) * left;
    }
    return result;
}