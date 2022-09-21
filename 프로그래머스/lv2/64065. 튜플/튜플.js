function solution(s) {
    let result = {}
    s = s.replace(/{/g, "[").replace(/}/g, "]")
    JSON.parse(s).flat().forEach(e => result[e] = !result[e] ? 1 : result[e]+1)
    return Object.entries(result).sort((a,b) => b[1]-a[1]).map(e => parseInt(e[0]));
}