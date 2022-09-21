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