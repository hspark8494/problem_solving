import java.io.*

var br = BufferedReader(InputStreamReader(System.`in`))
var bw = BufferedWriter(OutputStreamWriter(System.out))
fun main() {
    val (N, M) = br.readLine().split(" ").map { it.toInt() }
    val ps = Array<MutableList<Int>>(3) { mutableListOf(0) }
    for (i in 0 until N){
        val n = br.readLine().toInt() -1
        for (list in ps){
            list.add(list.last())
        }
        ps[n][ps[n].size-1] = ps[n].last() + 1
    }
    for (i in 0 until M){
        val (s, l) = br.readLine().split(" ").map { it.toInt() }
        for (list in ps){
            bw.write("${list[l] - list[s - 1]} ")
        }
        bw.newLine()
    }
    bw.flush()
    bw.close()
}
