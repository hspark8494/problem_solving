import java.io.*
import kotlin.math.absoluteValue

var br = BufferedReader(InputStreamReader(System.`in`))
fun main() {
    val (N, M) = br.readLine().split(" ").map { it.toInt() }
    val nums = br.readLine().split(" ").map { it.toInt() }.toList()
    val prefixSum = mutableListOf<Int>()
    prefixSum.add(0)
    var sum = 0
    for (i in 1 until N) {
        sum += (nums[i-1]-nums[i]).absoluteValue
        prefixSum.add(sum)
    }
    for(i in 0 until M) {
        val (a, b) = br.readLine().split(" ").map { it.toInt() }
        println(prefixSum[b-1] - prefixSum[a-1])
    }
}
