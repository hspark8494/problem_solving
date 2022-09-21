import java.io.*

val br = BufferedReader(InputStreamReader(System.`in`))
fun main(){
    val com = br.readLine()!!.toInt()
    val n = br.readLine()!!.toInt()

    val li:List<ArrayList<Int>> = List(com){ArrayList<Int>()}
    for(i in 0 until n){
        val r = br.readLine().split(" ").map { it.toInt()-1}
        li[r[0]].add(r[1])
        li[r[1]].add(r[0])
    }
    val visited = BooleanArray(com)
    dfs(li, 0, visited)
    var r = 0
    visited.forEach { if(it) r++}
    println(r-1)
}

fun dfs(li:List<ArrayList<Int>>, v:Int, visited:BooleanArray){
    visited[v] = true
    for(i in li[v]){
        if(!visited[i]){
            dfs(li, i, visited)
        }
    }
}