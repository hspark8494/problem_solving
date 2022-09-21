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