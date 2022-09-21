function solution(numbers) {
    let ans = numbers.sort((a,b)=>-String(a).repeat(3).localeCompare(String(b).repeat(3))).join("");
    return ans == 0 ? "0" : ans
}