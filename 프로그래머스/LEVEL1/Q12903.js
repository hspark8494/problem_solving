//Q12903 가운데 글자 가져오기
//https://programmers.co.kr/learn/courses/30/lessons/12903?language=javascript
function solution(s) {
    let r = s.length/2;
    console.log(r)
    if(s.length%2==0){
        return s[r-1] + s[r];
    }else{
        return s[Math.floor(r)];
    }
}