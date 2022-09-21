function solution(id_list, report, k) {
    const dict = {};
    const result = Array(id_list.length).fill(0);

    id_list.forEach((e) => dict[e] = new Set());
    
    for(s of report){
        let token = s.split(" ");
        dict[token[1]].add(id_list.indexOf(token[0]));
    }
    for(user in dict){
        if(dict[user].size >= k){
            [...dict[user]].forEach(e => result[e]++);
        }
    }

    return result;
}