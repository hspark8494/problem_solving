// Q42840 모의고사
// https://school.programmers.co.kr/learn/courses/30/lessons/42840
function solution(answers) {
    const arr = [[1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    const result = [0, 0, 0];
    for (let i = 0; i < answers.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            if (arr[j][i % arr[j].length] == answers[i]) {
                result[j]++;
            }
        }

    }
    let max = Math.max(...result);
    var answer = [];
    for (let i = 0; i < result.length; i++) {
        if (max == result[i]) {
            answer.push(i + 1);
        }
    }

    return answer;
}
