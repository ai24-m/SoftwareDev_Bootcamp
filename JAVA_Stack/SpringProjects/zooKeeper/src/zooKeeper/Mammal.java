package zooKeeper;

public class Mammal {
	
	

	private int energyLevel ;
	
	public  Mammal() {
		this.energyLevel=100;
	}
	
	public void energyLevel(){
		energyLevel=100;
		
	}

	public  int getEnergyLevel() {
		return energyLevel;
	}

	public void setEnergyLevel(int energyLevel ) {
		this.energyLevel = energyLevel;
	}

	public void displayEnergy() {
		System.out.println(" The energy level is :"+ energyLevel);
		System.out.println("");

	}

}
