function solution(skill, skill_trees) {
    const re = new RegExp(`[${skill}]`, "g");
    let result = 0;
    for(let e of skill_trees){
        let m = e.match(re);
        if(m == null || skill.startsWith(m.join(""))) result++
    }

    return result;
}
