// Q70129 이진 변환 반복하기
// https://school.programmers.co.kr/learn/courses/30/lessons/70129
function solution(s) {
    let result = [0, 0];
    while (s.length > 1) {
        let t = s.split("").reduce((acc, e) => acc + parseInt(e), 0)
        result[0]++;
        result[1] += (s.length - t);
        s = t.toString(2)
    }
    return result;
}
