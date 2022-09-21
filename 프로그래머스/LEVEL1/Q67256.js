//Q67256 키패드 누르기
//https://school.programmers.co.kr/learn/courses/30/lessons/67256
function solution(numbers, hand) {
    var answer = '';
    const dist = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    let right = [3, 2];
    let left = [3, 0];
    const getDist = (a, b) => Math.abs(a[0]-b[0]) + Math.abs(a[1]-b[1]);

    for (let h of numbers) {
        if ([1, 4, 7].indexOf(h) > -1) {
            answer += "L";
            left = dist[h];
            continue;
        } else if ([3, 6, 9].indexOf(h) > -1) {
            answer += "R";
            right = dist[h];
            continue;
        }
        const rightDist = getDist(right,dist[h]);
        const leftDist = getDist(left,dist[h]);

        if(rightDist<leftDist){
            right = dist[h];
            answer += "R";
        }else if(leftDist<rightDist){
            left = dist[h];
            answer += "L";
        }else{
            if(hand == "right"){
                answer += "R";
                right = dist[h];
            }else{
                answer += "L";
                left = dist[h];
            }
        }
    }

    return answer;
}