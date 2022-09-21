class Solution {
    fun solution(x: Int, n: Int): Array<Long> {
        return (1..n).map { it.toLong() * x.toLong() }.toTypedArray();
    }
}