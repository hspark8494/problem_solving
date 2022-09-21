const fs = require('fs');
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let n = parseInt(input[0]);
let result = [0, 0];

const arr = []
for(let i=1; i<=n; i++){
    arr.push(input[i].trim().split(" ").map(e=>parseInt(e)))
}


function quad(startX, startY, size) {
    let pre = arr[startX][startY];
    loop:
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            if (pre != arr[startX + i][startY + j]) {
                pre = -1;
                break loop;
            }
        }
    }
    if (pre === -1) {
        let divide = parseInt(size / 2);
        quad(startX, startY, divide);
        quad(startX + divide, startY, divide);
        quad(startX, startY + divide, divide);
        quad(startX + divide, startY + divide, divide);
    }else{
        result[pre]++;
    }
}

quad(0, 0, arr.length)

console.log(result[0])
console.log(result[1])