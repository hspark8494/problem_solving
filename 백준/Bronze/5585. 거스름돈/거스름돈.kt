fun main(){
    var n = 1000 - readLine()!!.toInt()
    var r = 0
    while(n>0){
        n -= if(n>=500){
            500
        }else if(n>=100){
            100
        }else if(n>=50){
            50
        }else if(n>=10){
            10
        }else if(n>=5){
            5
        }else{
            1
        }
        r++
    }
    print(r)
}