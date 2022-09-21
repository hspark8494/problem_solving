function solution(s, n) {
    return [...s].map(e => {
        if (e == " ") {
            return e;
        }
        let c = e.charCodeAt();
        if ((c < "Z".codePointAt() + 1 && c + n > "Z".codePointAt()) || c + n > "z".codePointAt()) {
            return String.fromCharCode(c + n - 26);
        } else {
            return String.fromCharCode(c + n);
        }
    }).join("");
}