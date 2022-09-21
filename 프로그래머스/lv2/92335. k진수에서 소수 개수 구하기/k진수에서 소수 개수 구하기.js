function solution(n, k) {
    let s = n.toString(k).split("0");
    const isPrime = num => {
        if(num=="" || num<=1) return false;
        for(let i=2; i<=Math.sqrt(num); i++) 
            if(num%i==0) return false;
        return true
    }
    return s.reduce((acc, curr) => acc+isPrime(curr), 0);
}