//Q12919 서울에서 김서방 찾기
//https://programmers.co.kr/learn/courses/30/lessons/12919
class Solution {
    fun solution(seoul: Array<String>): String {
        var answer = 0
        for(s in seoul){
            if(s == "Kim"){
                break;
            }
            answer++;
        }
        return "김서방은 ${answer}에 있다"
    }
}