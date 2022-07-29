
public class Operation {
	
	
	public double OperandOne;
	public double OperandTwo;
	public String Operation;
	public double result;
	
	public double performOperation() {
		if(Operation.equals("+")) {
			result = OperandOne + OperandTwo;
		}else if (Operation.equals("-")) {
			result = OperandOne - OperandTwo;
		}else if(Operation.equals("*")) {
			result = OperandOne * OperandTwo;	
		}else if (Operation.equals("/")) {
			result = OperandOne / OperandTwo;
		}
		return result;
	}
	
	public double getResults() {
		
		double getResult = result;
		return getResult;
	}

	public double getOperandOne() {
		return OperandOne;
	}

	public void setOperandOne(double d) {
		OperandOne = d;
	}

	public double getOperandTwo() {
		return OperandTwo;
	}

	public void setOperandTwo(double operandTwo) {
		OperandTwo = operandTwo;
	}

	public String getOperation() {
		return Operation;
	}

	public void setOperation(String operation) {
		Operation = operation;
	}
	
	
}
