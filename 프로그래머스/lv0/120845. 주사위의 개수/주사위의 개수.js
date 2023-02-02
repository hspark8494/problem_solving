function solution(box, n) {
    return box.reduce((acc, curr) => acc * parseInt(curr / n), 1);
}