//Q12943 콜라츠 추측
//https://programmers.co.kr/learn/courses/30/lessons/12943
function solution(num) {
    let r = 0;
    while(num>1 && r<500){
        if(num%2==0){
            num = num/2
        }else{
            num = num*3+1
        }
        r++;
    }
    return (r >= 500) ? -1 : r;
}