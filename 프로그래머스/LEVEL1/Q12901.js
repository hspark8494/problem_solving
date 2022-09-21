//Q12901 2016년
//https://programmers.co.kr/learn/courses/30/lessons/12901
function solution(a, b) {
    const days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'];
    let months = 0; 
    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].slice(0,a-1).forEach(e => months+=e);
    return days[(months+b)%7];
}