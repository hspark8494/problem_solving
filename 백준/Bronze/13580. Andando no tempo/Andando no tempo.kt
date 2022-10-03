fun main() {
    val (a,b,c) = readLine()!!.split(" ").map { it.toInt() }
    if (a==b+c || b==a+c || c==a+b || a==b || b==c || c==a) println("S")
    else println("N")
}