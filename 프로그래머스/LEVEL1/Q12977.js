//Q12977 소수 만들기
//https://school.programmers.co.kr/learn/courses/30/lessons/12977
function solution(nums) {
    arr = Array(3000).fill(true);
    arr[0]=false, arr[1]=false;
    result = 0;
    for(let i=2; i<arr.length; i++){
        if(arr[i]){
            let r = i*2;
            while(r<arr.length){
                arr[r] = false;
                r=r+i;
            }
        }
    }

    for(let i=0; i<nums.length-2; i++){
        for(let j=i+1; j<nums.length-1; j++){
           for(let k=j+1; k<nums.length; k++){
                if(arr[nums[i]+nums[j]+nums[k]]){
                    result++;
                }
           }
        }
    }

    return result;
}