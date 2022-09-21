class Solution {
    fun solution(absolutes: IntArray, signs: BooleanArray): Int {
        var result = 0
        for(i in absolutes.indices){
            result += (absolutes[i] * if(signs[i]) 1 else -1)
        }

        return result
    }
}