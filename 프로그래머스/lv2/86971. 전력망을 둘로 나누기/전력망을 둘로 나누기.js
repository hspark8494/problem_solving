function solution(n, wires) {
    const nodes = Array(n + 1).fill(0).map(e => []);

    for (let wire of wires) {
        nodes[wire[0]].push(wire[1]);
        nodes[wire[1]].push(wire[0]);
    }

    let result = 100;
    for (let wire of wires) {
        const visited = new Array(n).fill(false);
        const net = []
        let val = 0;

        for (let i = 1; i < nodes.length; i++) {
            val = 0;
            if (!visited[i]) {
                val++;
                dfs(i, 0);
                net.push(val);
            }
        }

        function dfs(i, from) {
            if ((i == wire[0] && from == wire[1]) || (from == wire[0] && i == wire[1])) {
                return;
            }
            visited[i] = true;
            val++;
            for (let k of nodes[i]) {
                if (!visited[k]) {
                    dfs(k, i);
                }
            }
        }

        result = Math.min(result, Math.abs(net[0] - net[1]));
    }

    return result;
}