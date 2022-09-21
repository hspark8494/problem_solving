function solution(numbers) {
    const set = new Set();
    numbers = numbers.split("");
    for(let i=0; i<numbers.length; i++){
        const perArr = [];
        const perCheck = Array(numbers.length).fill(false);
        perm(i);

        function perm(r){
            if(perArr.length == r+1){
                set.add(parseInt(perArr.join("")));
                return;
            }
            for(let j=0; j<numbers.length; j++){
                if(!perCheck[j]){
                    perArr.push(numbers[j]);
                    perCheck[j] = true;
                    perm(r);
                    perCheck[j] = false;
                    perArr.pop();
                }
            }
        }

    }
    return [...set].reduce((acc,curr) => acc+isPrime(curr), 0);
}
function isPrime(n){
    if(n<=1){
        return false;
    }
    for(let i=2; i<=Math.sqrt(n); i++){
        if(n%i==0) {
            return false;
        }
    }
    return true;
}