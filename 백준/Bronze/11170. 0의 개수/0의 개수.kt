fun main(){
    for(i in 1..readLine()!!.toInt()){
        var l = readLine()!!.split(" ").map{it.toInt()}
        var zero:Int = 0
        for(i in l[0] .. l[1]){
            var s = i.toString()
            for(i in s){
                if(i=='0')
                    zero++;
            }
        }
        println(zero)
    }
}
