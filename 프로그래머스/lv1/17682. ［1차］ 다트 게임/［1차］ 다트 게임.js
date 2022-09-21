function solution(dartResult) {
    const exp = "SDT";
    const val = ["**1", "**2", "**3"]
    const tokens = dartResult.match(/([0-9]+|S|D|T|\*|#)/g);
    let result = [];
    for (let i = 0; i < tokens.length; i++) {
        let idx = exp.indexOf(tokens[i]);
        if (idx > -1) {
            result.push(eval(tokens[i - 1] + val[idx]));
            continue;
        }
        if (tokens[i] == "#") {
            result[result.length - 1] *= (-1);
        } else if (tokens[i] == "*") {
            result[result.length - 1] *= 2;
            if (result.length - 2 >= 0) {
                result[result.length - 2] *= 2;
            }
        }
    }

    return result.reduce((acc, c) => acc + c);
}