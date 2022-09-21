function solution(n, k) {
    return n.toString(k).split("").reduce((acc, curr) => acc+parseInt(curr||curr>1||isPrime(curr)), 0);
}
function isPrime(num){
    for(let i=2; i<=Math.sqrt(num); i++) 
        if(num%i==0) return false;
    return true
}