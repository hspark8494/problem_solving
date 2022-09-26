import java.io.BufferedReader
import java.io.InputStreamReader

var br = BufferedReader(InputStreamReader(System.`in`))
fun main() {
    val n = br.readLine()!!.toInt()
    val nums = mutableListOf<Int>()
    for (i in 0 until n) {
        nums.addAll(br.readLine()!!.split(" ").map { it.toInt() })
    }
    nums.sortDescending()
    print(nums[n-1])
}