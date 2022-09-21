function solution(price, money, count) {
    return Math.max(-(money-count*(2*price+(count-1)*price)/2),0)
}