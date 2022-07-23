package zooKeeper;

public class GorillaTest {
//	 Create a GorillaTest class to instantiate a gorilla and have it throw three things, eat bananas twice, and climb once.  
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Mammal mammal = new Mammal();
		Gorilla gorilla = new Gorilla();
		
		mammal.displayEnergy();
		gorilla.throwSomething();
		gorilla.throwSomething();
		gorilla.throwSomething();
		mammal.displayEnergy();
		gorilla.eatBananas();
		gorilla.eatBananas();
		mammal.displayEnergy();
		gorilla.climb();
		mammal.displayEnergy();
		
	}

}
