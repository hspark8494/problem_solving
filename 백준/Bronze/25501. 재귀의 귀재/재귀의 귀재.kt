import java.io.BufferedReader
import java.io.InputStreamReader

var x = 0
var br = BufferedReader(InputStreamReader(System.`in`))
fun recursion(s: String, l: Int, r: Int): Int {
    x+=1
    return if (l >= r) 1 else if (s[l] != s[r]) 0 else recursion(s, l + 1, r - 1)
}

fun isPalindrome(s: String): Int {
    return recursion(s, 0, s.length - 1)
}

fun main(args: Array<String>) {
    var n = br.readLine()!!.toInt()
    for (i in 0 until n){
        x = 0
        println("${isPalindrome(br.readLine())} $x")
    }

}