fun main() {
    val r = (readLine()!!.toInt() + readLine()!!.toInt()) % 12
    if (r!=0){
        print(r)
    }else{
        print(12)
    }
}