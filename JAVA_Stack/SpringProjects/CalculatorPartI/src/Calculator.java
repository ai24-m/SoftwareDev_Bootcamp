
public class Calculator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Operation A = new Operation();
		Operation B = new Operation();
		
		A.setOperandOne(10.5);
		A.setOperation("/");
		A.setOperandTwo(5.2);
		
		A.performOperation();
		
		B.setOperandOne(2.5);
		B.setOperation("*");
		B.setOperandTwo(1.2);

		B.performOperation();
		
		System.out.println(A.getResults());
		System.out.println(B.getResults());
	}

}
