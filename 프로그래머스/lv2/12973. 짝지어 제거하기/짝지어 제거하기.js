function solution(s) {
    let left = s.split("");
    let right = [];

    while(left.length > 0){
        if(right.length == 0){
            right.push(left.pop());
            continue;
        }
        if(left[left.length-1] === right[right.length-1]){
            left.pop();
            right.pop();
        }else{
            right.push(left.pop());
        }
    }
    return right.length==0 ? 1 : 0;
}