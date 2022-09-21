// Q12969 직사각형 별찍기
// https://programmers.co.kr/learn/courses/30/lessons/12969
fun main(args: Array<String>) {
    val (a, b) = readLine()!!.split(' ').map(String::toInt)
    println(("*".repeat(a)+"\n").repeat(b))
}