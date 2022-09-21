function solution(numbers, target) {
    let result = 0;
    function solve(acc, sign, dept){
        acc += (numbers[dept] * sign);
        if(dept+1>=numbers.length){
            if(acc === target){
                result++;
            }
            return;
        }else{
            solve(acc, 1, dept+1);
            solve(acc, -1, dept+1);
        }
    }

    solve(0, 1, 0)
    solve(0, -1, 0)
    return result;
}