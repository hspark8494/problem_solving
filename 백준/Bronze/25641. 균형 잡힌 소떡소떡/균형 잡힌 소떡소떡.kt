fun main() {
    val len = readLine()!!.toInt()
    val str = readLine()!!
    var s = 0
    var t = 0
    for (c in str) {
        if (c == 's') {
            s++
        } else {
            t++
        }
    }
    for (i in 0 until len) {
        if (s == t) {
            print(str.substring(i until len))
            break
        }
        if (str[i] == 's') {
            s--
        } else {
            t--
        }
    }
}