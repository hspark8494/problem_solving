//Q72410 신규 아이디 추천
//https://school.programmers.co.kr/learn/courses/30/lessons/72410
function solution(new_id) {
    let answer = new_id.toLowerCase();
    answer = answer.replace(/[^\w\.\-]/g, "").replace(/(\.+)/g,".").replace(/(^\.|\.$)/g, "");
    if(answer == ""){
        answer = "a";
    }
    answer = answer.slice(0,15).replace(/(\.$)/g, "");

    while(answer.length <= 2){
        answer=String(answer)+answer[answer.length-1];
    }
    return answer;
}