import java.io.*;
import java.util.*;

/**
 * Created by krasko on 6/8/15.
 *
 * Launch with -Xss515m.
 */
public class Main {
    Scanner in;
    PrintWriter out;

    void run() throws IOException {
        in = new Scanner(new FileReader("i2.in"));
        out = new PrintWriter(new FileWriter("i1.out"));

        int t = nextInt();

        for (int i = 0; i < t; ++i) {
            int tree_size = nextInt();
            int[] tree = new int[tree_size];
            tree[0] = -1;
            for (int j = 1; j < tree_size; ++j) {
                tree[j] = nextInt() - 1;
            }
            solve(tree);
        }

        out.close();
    }

    private void solve(int[] tree) {
        Node root = buildTree(tree);
        setSizes(root);
        calcWeights(root);
        print(sumWeights(root));
    }

    private void print(int i) {
        out.println(i);
    }

    private int sumWeights(Node root) {
        int weight = root.weight;
        for (Node child : root.children) {
            weight += sumWeights(child);
        }
        return weight;
    }

    class HamHode implements Comparable<HamHode> {
        HamHode l = null;
        HamHode r = null;
        int size;

        HamHode(HamHode l, HamHode r) {
            this.l = l;
            this.r = r;
            this.size = l.size + r.size;
        }

        HamHode(Node node) {
            this.size = node.size;
        }

        @Override
        public int compareTo(HamHode rhs) {
            return this.size - rhs.size;
        }
    }

    private int hamWeight(HamHode root, int depth) {
        if (root.l == null || root.r == null) {
            return root.size * depth;
        } else {
            return hamWeight(root.l, depth + 1) + hamWeight(root.r, depth + 1);
        }
    }

    private void calcWeights(Node root) {
        PriorityQueue<HamHode> q = new PriorityQueue<>();
        for (Node child : root.children) {
            calcWeights(child);
            q.add(new HamHode(child));
        }
        while (q.size() > 1) {
            HamHode h1 = q.poll();
            HamHode h2 = q.poll();
            q.add(new HamHode(h1, h2));
        }
        if (q.size() == 1) {
            root.weight = hamWeight(q.poll(), 0);
        } else {
            root.weight = 0;
        }
    }

    private void setSizes(Node root) {
        root.size = 1;
        for (Node child : root.children) {
            setSizes(child);
            root.size += child.size;
        }
    }

    class Node {
        ArrayList<Node> children = new ArrayList<>();
        int size = 1;
        int weight = 0;
    }

    private Node buildTree(int[] parents) {
        Node[] nodes = new Node[parents.length];
        for (int i = 0; i < parents.length; ++i) {
            nodes[i] = new Node();
        }
        for (int i = 1; i < parents.length; ++i) {
            nodes[parents[i]].children.add(nodes[i]);
        }
        return nodes[0];
    }

    StringTokenizer st = new StringTokenizer("");


    int nextInt() {
        while (!st.hasMoreTokens()) {
            st = new StringTokenizer(in.nextLine());
        }
        return Integer.parseInt(st.nextToken());
    }


    public static void main(String[] args) throws IOException {
        new Main().run();
    }
}
