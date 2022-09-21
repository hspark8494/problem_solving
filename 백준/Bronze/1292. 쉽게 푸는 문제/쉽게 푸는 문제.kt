fun main() {
    val l = readLine()!!.split(" ").map { it.toInt() }
    var r = 0
    var index = 1
    var c = 1

    while(true){
        for(i in 1..c){
            if(index>=l[0] && index<=l[1]){
                r+=c
            }
            index++;
        }
        c++;
        if(index>l[1]){
            break
        }
    }
    print(r)
}