//Q64061 크레인 인형뽑기 게임
//https://programmers.co.kr/learn/courses/30/lessons/64061
function solution(board, moves) {
    const boardStack = [];
    const resultStack = [];
    let result = 0;
    for (let i = 0; i < board[0].length; i++) {
        let li = [];
        for (let j = board[0].length - 1; j >= 0; j--) {
            if (board[j][i] != 0) {
                li.push(board[j][i])
            }
        }
        boardStack.push(li);
    }
    moves.forEach(e => {
        let r = boardStack[e - 1].pop();
        if (r != undefined) {
            if (resultStack[resultStack.length - 1] === r) {
                resultStack.pop();
                result = result + 2;
            } else {
                resultStack.push(r);
            }
        }
    })
    return result;
}