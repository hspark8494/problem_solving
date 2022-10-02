fun main() {
    val n = readLine()!!.toInt()
    val sb = StringBuilder()
    for (i in 1..n){
        if (i==1) {
            sb.append("int a;\nint *ptr = &a;\n")

        }else if(i==2){
            sb.append("int **ptr2 = &ptr;\n")
        }else{
            sb.append("int ${"*".repeat(i)}ptr${i} = &ptr${i-1};\n")
        }
    }
    println(sb.toString())
}
