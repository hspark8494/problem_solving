//Q81301 숫자 문자열과 영단어
//https://programmers.co.kr/learn/courses/30/lessons/81301
class Solution {
    fun solution(s: String): Int {
        val numbers = arrayOf("zero", "one","two","three","four","five","six","seven","eight","nine")
        var answer = s
        for(i in 0 .. 9) {
            answer = answer.replace(numbers[i], i.toString())
        }
        return answer.toInt()
    }
}