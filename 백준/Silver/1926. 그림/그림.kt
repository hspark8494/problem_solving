import java.io.*
import kotlin.math.max

var br = BufferedReader(InputStreamReader(System.`in`))
var mx = 0
var cnt = 0
fun main() {
    val (H, W) = br.readLine().split(" ").map { it.toInt() }
    val board = Array(H) { br.readLine().split(" ").map { it == "1" }.toBooleanArray() }
    val visited = Array(H) { BooleanArray(W) }
    var x = 0
    for (i in 0 until H) {
        for (j in 0 until W) {
            if (board[i][j] && !visited[i][j]) {
                dfs(i, j, board, visited)
                cnt = 0
                x++
            }
        }
    }
    println(x)
    print(mx)
}

fun dfs(h: Int, w: Int, board: Array<BooleanArray>, visited: Array<BooleanArray>) {
    if (h < 0 || w < 0 || h >= board.size || w >= board[0].size || visited[h][w]) return
    visited[h][w] = true
    if (board[h][w]) {
        cnt ++
        mx = max(mx, cnt)
        dfs(h - 1, w, board, visited)
        dfs(h + 1, w, board, visited)
        dfs(h, w - 1, board, visited)
        dfs(h, w + 1, board, visited)
    }
}
