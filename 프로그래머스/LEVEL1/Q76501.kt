// Q76501 음양더하기
// https://programmers.co.kr/learn/courses/30/lessons/76501

class Solution {
    fun solution(absolutes: IntArray, signs: BooleanArray): Int {
        var result = 0
        for(i in absolutes.indices){
            result += (absolutes[i] * if(signs[i]) 1 else -1)
        }

        return result
    }
}