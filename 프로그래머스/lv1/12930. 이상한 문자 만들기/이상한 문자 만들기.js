function solution(s) {
    return s.split(" ").map(s => [...s].map( (e,idx) => idx%2 ? e.toLowerCase() : e.toUpperCase()).join("")).join(" ");
}