import java.util.ArrayList;
import java.util.List;


public class Node {
	private int val;
	private List<Node> branches;
	public int getVal() {
		return val;
	}
	public void setVal(int val) {
		this.val = val;
	}
	public List<Node> getBranches() {
		return branches;
	}
	public void setBranches(List<Node> branches) {
		this.branches = branches;
	}
	public Node getBranch(int index) {
		return branches.get(index);
	}
	public void addBranch(Node n) {
		this.branches.add(n);
	}
	public Node(List<Node> n, int v) {
		branches = n;
		this.val = v;
	}
	
	public static boolean DFS(int search, Node n) {
		if (search==n.val)
			return true;
		for (Node b : n.branches) {
			return DFS(search, b);
		}
		return false;
	}
	public static Node NodesOfDepth(int depth) {
		Node last = null;
		Node root = null;
		for(int i = 1; i <= depth; i++) {
			Node n = new Node(new ArrayList<Node>(), i);
			if(last!=null)
				last.addBranch(n);
			last = n;
			if(root == null)
				root = n;
		}
		return root;
	}
}
