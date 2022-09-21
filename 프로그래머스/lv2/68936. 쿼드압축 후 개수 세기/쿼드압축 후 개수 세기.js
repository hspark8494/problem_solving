function solution(arr) {
    let result = [0, 0];

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

    return result;
}