import java.util.Collections.max

fun main() {
    val li = readLine()!!.split(" ").map(String::toInt).toList()
    val mx = max(li)
    var result = 0
    for (i in li) {
        result += (mx!! - i)
    }
    println(result)
}