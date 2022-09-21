fun main() {
    val l = readLine()!!.split(" ").map { it.toInt() }
    var arr = Array<Int>(l[1]) { 0 }
    var numbersPool = Array<Int>(l[0] + 1) { 0 }

    fun dfs(idx:Int){
        if(idx == l[1]){
            println(arr.joinToString(separator = " "))
            return
        }
        for(i in 1..l[0]) {
            if (numbersPool[i] == 0) {
                numbersPool[i] = 1
                arr[idx] = i
                dfs(idx + 1)
                numbersPool[i] = 0
            }
        }
    }
    dfs(0)
}
