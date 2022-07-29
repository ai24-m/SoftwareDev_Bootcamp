package zooKeeper;

public class Gorilla extends Mammal {


	public void throwSomething() {
		int energy = getEnergyLevel() -5;
		System.out.println(" The Gorilla has thrown somthing ");
		this.setEnergyLevel(energy);
		
	}
	
	public void eatBananas() {
		int energy = getEnergyLevel()+ 10;
		System.out.println(" The Gorilla has ate Banana  ");
		this.setEnergyLevel(energy);
	}
		 
	public void climb() {
		int energy = getEnergyLevel()- 10;
		System.out.println(" The Gorilla has climbed the tree");
		this.setEnergyLevel(energy);

		
	}
	

}