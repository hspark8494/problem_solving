import java.io.*
import java.util.TreeSet

var br = BufferedReader(InputStreamReader(System.`in`))
fun main() {
    val (K,N) = br.readLine().split(" ").map { it.toInt() }
    var setA = TreeSet<Int>()
    var setB = TreeSet<Int>()
    setA.addAll(br.readLine().split(" ").map { it.toInt() })
    setB.addAll(br.readLine().split(" ").map { it.toInt() })
    setA.removeAll(setB)
    println(setA.size)
    for (i in setA){
        print("$i ")
    }
}
