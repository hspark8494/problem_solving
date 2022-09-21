// Q17686 파일명 정렬
// https://school.programmers.co.kr/learn/courses/30/lessons/17686?language=javascript
function solution(files) {
    re = /[0-9]+|([a-zA-Z]|[-.\s])+/g
    return files.sort((a,b)=>{
        let aa = a.match(re);
        let bb = b.match(re);
        aa[0] = aa[0].toLocaleLowerCase();
        bb[0] = bb[0].toLocaleLowerCase();
        if(aa[0] === bb[0]){
            return aa[1] - bb[1];
        }else{
            return aa[0].localeCompare(bb[0]);
        }
    })
}