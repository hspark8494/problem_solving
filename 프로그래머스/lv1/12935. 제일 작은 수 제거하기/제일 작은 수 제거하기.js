function solution(arr) {
    if(arr.length <= 1){
        return [-1];
    }
    let idx=0;
    let min=arr[0];
    for(let i=0; i<arr.length; i++){
        if(min>arr[i]){
            idx = i;
            min = arr[i];
        }
    }
    arr.splice(idx, 1)
    return arr;
}