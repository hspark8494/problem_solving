import java.io.*

val br = BufferedReader(InputStreamReader(System.`in`))
var mx = 0;
var mxPos:Pair<Int, Int> = Pair(1,1)
val posW = arrayOf(1, -1, 0, 0);
val posH = arrayOf(0, 0, 1, -1);
var wh:Pair<Int, Int> = Pair(1,1)

fun findStart(board:MutableList<String>):Pair<Int, Int> {
    for (i in board.indices){
        for (j in board[i].indices){
            if (board[i][j] == '.'){
                return Pair(j,i)
            }
        }
    }
    return Pair(1,1)
}

private fun dfs(board:MutableList<String>, curr:Pair<Int, Int>, visited:Array<BooleanArray>, dept:Int){
    if (dept>mx){
        mx = dept
        mxPos = curr
    }
    for (i in 0..3){
        val w = curr.first + posW[i]
        val h = curr.second + posH[i]
        if (!visited[h][w] && board[h][w] == '.'){
            visited[h][w] = true
            dfs(board, Pair(w,h), visited, dept+1)
        }
    }
}

fun main() {
    for (t in 0 until br.readLine()!!.toInt()) {
        mx = 0
        val l = br.readLine()!!.split(" ").map { it.toInt() }
        wh = Pair(l[0], l[1])
        val board = mutableListOf<String>();
        for (i in 0 until wh.second) {
            board.add(br.readLine()!!)
        }
        mxPos = findStart(board)
        var visited = Array(wh.second){BooleanArray(wh.first)}
        visited[mxPos.second][mxPos.first] = true
        dfs(board, mxPos, visited, 0)

        visited = Array(wh.second){BooleanArray(wh.first)}
        visited[mxPos.second][mxPos.first] = true
        dfs(board, mxPos, visited, 0)

        println("Maximum rope length is $mx.")
    }
}
