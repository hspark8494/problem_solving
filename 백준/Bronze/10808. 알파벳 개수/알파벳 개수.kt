fun main(){
    val arr:Array<Int> = Array(26) { 0 }
    for(i in readLine()!!){
        arr[i.code-97] ++
    }
    arr.forEach { print("$it ") }
}