function solution(sizes) {
    const wd = [], ht = [];
    sizes.forEach(e=> {
        if(e[0]>e[1]){
            wd.push(e[0]);
            ht.push(e[1]);
        }else{
            wd.push(e[1]);
            ht.push(e[0]);
        }
    })
    return Math.max(...wd) * Math.max(...ht);
}