function solution(s) {
    let arr = s.split(" ").map(e=>parseInt(e));
    return `${Math.min(...arr)} ${Math.max(...arr)}`;
}