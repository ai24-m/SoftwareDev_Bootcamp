package projectOnee;

public class HelloWorldTest {

	public static void main(String[] args) {
		HelloWorld h = new HelloWorld();
		h.greet();
		System.out.println("Hiii ");
		HelloWorld m = new HelloWorld();
		m.hi();	
		System.out.println(h.greet());

	}

}
