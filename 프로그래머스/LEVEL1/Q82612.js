//Q82612 부족한 금액 계산하기
//https://programmers.co.kr/learn/courses/30/lessons/82612
function solution(price, money, count) {
    return Math.max(-(money-count*(2*price+(count-1)*price)/2),0)
}
