function solution(n) {
    arr = Array(n+1).fill(true);
    arr[0]=false, arr[1]=false;

    for(let i=2; i<arr.length; i++){
        if(arr[i]){
            let r = i*2;
            while(r<arr.length){
                arr[r] = false;
                r=r+i;
            }
        }
    }
    return arr.reduce((acc, e) => acc + e);
}