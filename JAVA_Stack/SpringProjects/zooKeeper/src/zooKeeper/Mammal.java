package zooKeeper;

//Create a Mammal class that has an energyLevel member variable and displayEnergy() method. The displayEnergy() method should show the animal's energy level as well as return it

public class Mammal {
	protected static int energyLevel = 100;

	public static int getEnergyLevel() {
		return energyLevel;
	}
	public void displayEnergy() {
		System.out.println("");
		System.out.println("The energy level of Gorilla is : "+ energyLevel);
		System.out.println("");
	}

}
