fun main(){
    var w:List<Int> = List<Int>(10) { readLine()!!.toInt() }.sorted()
    var v:List<Int> = List<Int>(10) { readLine()!!.toInt() }.sorted()

    print("${w[9]+w[8]+w[7]} ${v[9]+v[8]+v[7]}")
}