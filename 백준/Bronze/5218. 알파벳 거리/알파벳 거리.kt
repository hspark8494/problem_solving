fun main(){
    for(x in 1 .. readLine()!!.toInt()) {
        val s = readLine()!!.split(" ")
        print("Distances:")
        for(i in 0 until s[0].length){
            val r = s[0][i].code - s[1][i].code
            print(" ${if(r<=0) r*-1 else 26-r}")
        }
        println()
    }
}