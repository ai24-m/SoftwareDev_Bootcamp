package zooKeeper;

public class GorillaTest {
//	 Create a GorillaTest class to instantiate a gorilla and have it throw three things, eat bananas twice, and climb once.  
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Mammal g = new Mammal();
		Gorilla h = new Gorilla();
		
		g.displayEnergy();
		h.throwSomething();
		h.throwSomething();
		h.throwSomething();
		g.displayEnergy();
		h.eatBananas();
		h.eatBananas();
		g.displayEnergy();
		h.climb();
		g.displayEnergy();
		
	}

}
