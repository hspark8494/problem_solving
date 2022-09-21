import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static char[] cArr, result, mx;
    static boolean[] visit;
    static BufferedWriter bw;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            cArr = br.readLine().toCharArray();
            int len = cArr.length;
            result = new char[len];
            mx = new char[len];
            visit = new boolean[len];
            Arrays.sort(cArr);
            dfs(len, 0);
        }
        bw.flush();
        bw.close();
        br.close();
    }
    static void dfs(int len, int depth) throws IOException {
        if (depth == len) {
            bw.write(result);
            bw.write("\n");
            return;
        }
        mx[depth] = 0;
        for (int i = 0; i < len; i++) {
            if (visit[i]) continue;
            if (mx[depth] >= cArr[i]) continue;

            mx[depth] = cArr[i];

            visit[i] = true;
            result[depth] = cArr[i];
            dfs(len, depth + 1);
            visit[i] = false;
        }
    }
}