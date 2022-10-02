fun main() {
    val (n, k) = readLine()!!.split(" ").map { it.toInt() }
    var result = 0
    var h=0
    var m=0
    var s=0
    while (h <= n){
        if (check(h,k) || check(m,k) || check(s,k)){
            result += 1
        }
        s += 1
        if (s>=60){
            m += 1
            s = 0
        }
        if (m>=60){
            h += 1
            m = 0
        }
    }
    println(result)
}

fun check(x:Int, y:Int):Boolean{
    return x.toString().padStart(2, '0').contains(y.toString())
}