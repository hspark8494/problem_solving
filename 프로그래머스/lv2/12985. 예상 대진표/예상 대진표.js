function solution(n, a, b) {
    let answer = 1;
    if(a<b){
        let temp = a;
        a = b;
        b = temp;
    }
    while(!(a%2==0 && a-1==b)){
        a = Math.ceil(a/2);
        b = Math.ceil(b/2);
        answer++;
    }
    return answer;
}