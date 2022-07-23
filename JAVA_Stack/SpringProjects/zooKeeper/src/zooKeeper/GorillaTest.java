package zooKeeper;

public class GorillaTest {
//	 Create a GorillaTest class to instantiate a gorilla and have it throw three things, eat bananas twice, and climb once.  
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Gorilla gorilla = new Gorilla();
		
		gorilla.displayEnergy();
		gorilla.throwSomething();
		gorilla.throwSomething();
		gorilla.throwSomething();
		gorilla.displayEnergy();
		gorilla.eatBananas();
		gorilla.eatBananas();
		gorilla.displayEnergy();
		gorilla.climb();
		gorilla.displayEnergy();
		
	}

}
