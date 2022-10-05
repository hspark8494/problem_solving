import kotlin.math.absoluteValue

fun main() {
    val words = """aespa
baekjoon
cau
debug
edge
firefox
golang
haegang
iu
java
kotlin
lol
mips
null
os
python
query
roka
solvedac
tod
unix
virus
whale
xcode
yahoo
zebra""".split("\n")
    val txt = readLine()!!
    val sb = StringBuilder()
    var i = 0
    var tmp =  ""
    var state = true
    for (t in txt){
        if (i >= tmp.length){
            sb.append(t)
            tmp = words[t.code-97]
            i = 0
        }
        if(t != tmp[i]){
            state = false
            break
        }
        i++
    }
    if (state && i == tmp.length) {
        println("It's HG!")
        println(sb.toString())
    }
    else {
        println("ERROR!")
    }
}