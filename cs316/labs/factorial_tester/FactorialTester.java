import java.math.BigInteger;

public class FactorialTester {
	/*public static BigInteger fact(BigInteger n) {
	}*/

	private static BigInteger TWO = BigInteger.valueOf(2);

	public static BigInteger fib(BigInteger n) {
		if(n.compareTo(BigInteger.ONE)<=1) {
			return n;
		} else {
			return fib(n.subtract(BigInteger.ONE)).add(n.subtract(TWO));
		}
	}

	public static void toh(int n, int src, int dst, int tmp) {
		if (n==1) {
			System.out.println(src + " ---> " + dst);
		} else {
			toh(n-1, src, tmp, dst);
			System.out.println(src + " ---> " + dst);
			toh(n-1, tmp, dst, src);
		}
	}

	public static void main(String[] args) {
		toh(3, 1, 2, 3);
	}
}
