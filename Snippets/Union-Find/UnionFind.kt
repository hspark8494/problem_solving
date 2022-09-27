import java.io.*

var parent = IntArray(0)
var values = IntArray(0)
fun find(x: Int): Int {
    var i = x
    while (i != parent[i]) {
        parent[i] = parent[parent[i]]
        i = parent[i]
    }
    return i;
}

fun union(x: Int, y: Int): Boolean {
    val i = find(x)
    val j = find(y)
    if (i == j) return false
    if (values[i] < values[j]) {
        parent[i] = j
        values[j] += values[i]
    } else {
        parent[j] = i
        values[i] += values[j]
    }
    return true
}

var br = BufferedReader(InputStreamReader(System.`in`))
fun main() {

}