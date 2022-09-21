//Q12916 문자열 내 p와 y의 개수
//https://programmers.co.kr/learn/courses/30/lessons/12916
function solution(s) {
    let p = 0, y = 0;
    [...s.toLowerCase()].forEach(e => {
        if (e == 'p') {
            p++;
        } else if (e == 'y') {
            y++;
        }
    })
    return (p == y);
}