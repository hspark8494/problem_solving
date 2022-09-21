function solution(x) {
    return x%[...x+''].reduce((acc, e)=> parseInt(acc)+parseInt(e))==0;
}