import java.util.*

fun main(){
    val sc = Scanner(System.`in`)
    val n = sc.nextInt()
    var money = sc.nextInt()
    val list = List<Int>(n) { sc.nextInt() }.reversed()
    var index = 0
    var coin =0
    while(money>0){
        if(money>=list[index]){
            money-=list[index]
            coin++
        }else{
            index++
        }
    }
    print(coin)
}
