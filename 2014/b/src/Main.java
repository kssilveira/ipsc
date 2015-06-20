import java.io.*;
import java.lang.reflect.Array;
import java.math.BigInteger;
import java.util.*;

/**
 * Created by krasko on 6/8/15.
 */
public class Main {

    Scanner in;
    PrintWriter out;

    BigInteger TWO = BigInteger.valueOf(2);

    void run() throws IOException {

        in = new Scanner(new FileReader("b1 (1).in"));
        out = new PrintWriter(new FileWriter("b.out(2)"));

        long t = nextLong();
        for (long j = 0; j < t; ++j) {
            int n = (int) nextLong();
            long[] strip = new long[n];
            long[] seed = new long[43];
            for (int i = 0; i < n; ++i) {
                strip[i] = nextLong();
            }
            for (int i = 0; i < 43; ++i) {
                seed[i] = nextLong();
            }
            nextLong();
            String moves = nextString();
            solve(strip, seed, moves);
        }

        out.close();
    }

    private void reverse(long[] arr) {
        for (int i = 0; i < arr.length / 2; ++i) {
            long tmp = arr[i];
            arr[i] = arr[arr.length - 1 - i];
            arr[arr.length - 1 - i] = tmp;
        }
    }

    private void insert(long[] arr, Rnd rnd) {
        long num_empty = 0;
        for (long l : arr) {
            if (l == 0) num_empty++;
        }
        long new_value = 1;

        long pos = rnd.next() % num_empty;
        if (rnd.next() % 10 == 0) {
            new_value = 2;
        }
        int ptr = 0;
        while (pos >= 0) {
            if (arr[ptr] == 0) {
                --pos;
            }
            if (pos == -1) {
                arr[ptr] = new_value;
            }
            ++ptr;
        }
    }

    private void solve(long[] strip, long[] seed, String moves) {
        Rnd rnd = new Rnd(seed);

        for (int i = 0; i < strip.length; ++i) {
            if (strip[i] > 0) {
                strip[i] = Long.numberOfTrailingZeros(strip[i]);
            }
        }

        for (char c : moves.toCharArray()) {
            if (c == 'r') {
                reverse(strip);
            }

            int write = -1;
            boolean effect = false;

            for (int i = 0; i < strip.length; ++i) {
                if (strip[i] != 0) {
                    if (write >= 0 && strip[write] == strip[i]) {
                        strip[write] = -1 - strip[write];
                        strip[i] = 0;
                        effect = true;
                    }
                    else if (i > write + 1) {
                        strip[++write] = strip[i];
                        strip[i] = 0;
                        effect = true;
                    } else {
                        write = i;
                    }
                }
            }

            if (c == 'r') {
                reverse(strip);
            }

            for (int i = 0; i < strip.length; ++i) {
                strip[i] = Math.abs(strip[i]);
            }

            if (effect) {
                insert(strip, rnd);
            }
        }

        for (int i = 0; i < strip.length; ++i) {
            print((strip[i] == 0 ? BigInteger.ZERO : TWO.pow((int) strip[i])), i == strip.length - 1);
        }

    }

    class Rnd {

        int r = 43, s = 22;
        long m = 1L << 32;
        int ptr = 43;
        Map<Integer, Integer> c_map = new HashMap<>();
        Map<Integer, Long> rand_map = new HashMap<>();

        Rnd(long[] seed) {
            for (int i = 0; i < seed.length; ++i) {
                rand_map.put(i, seed[i]);
            }
        }

        int c(int i) {
            if (!c_map.containsKey(i)) {
                if (i >= 43 && rand(i - s) - rand(i - r) - c(i - 1) < 0) {
                    c_map.put(i, 1);
                } else {
                    c_map.put(i, 0);
                }
            }
            return c_map.get(i);
        }

        long rand(int i) {
            if (!rand_map.containsKey(i)) {
                long val = rand(i - s) - rand(i - r) - c(i - 1);
                rand_map.put(i, (val + m) % m);
            }
            return rand_map.get(i);
        }

        long next() {
            return rand(ptr++);
        }
    }

    void print(BigInteger i, boolean newline) {
        out.print(i);
        if (newline) {
            out.print('\n');
        } else {
            out.print(' ');
        }
    }

    StringTokenizer st = new StringTokenizer("");

    long nextLong() {
        while (!st.hasMoreTokens()) {
            st = new StringTokenizer(in.nextLine());
        }
        return Long.parseLong(st.nextToken());
    }

    String nextString() {
        while (!st.hasMoreTokens()) {
            st = new StringTokenizer(in.nextLine());
        }
        return st.nextToken();
    }

    public static void main(String[] args) throws IOException {
        new Main().run();
    }
}
