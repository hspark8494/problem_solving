fun main(){
    val s = readLine()!!
    print(
        buildString {
            for(i in s) {
                when (i.code) {
                    in 'A'.code..'M'.code, in 'a'.code..'m'.code -> append((i.code + 13).toChar())
                    in 'N'.code..'Z'.code, in 'n'.code..'z'.code -> append((i.code - 13).toChar())
                    else -> append(i)
                }
            }
        }
    )
}