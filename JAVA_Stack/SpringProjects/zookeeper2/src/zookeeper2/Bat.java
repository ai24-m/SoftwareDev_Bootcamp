package zookeeper2;

public class Bat extends Mammal {
	
	
	public Bat(){
        this.setEnergyLevel(300);
    } 
	 
	public void fly() {
		System.out.println(" The Bat taking off ");
		int energy = this.getEnergyLevel()-50;
		this.setEnergyLevel(energy);
		
	}

	public void eatHumans() {
		System.out.println(" The Bat just Eat Human :) ");
		int energy = this.getEnergyLevel()+25;
		this.setEnergyLevel(energy);

	}

	public void attackTown() {
		System.out.println(" The Bat just attack the town ");
		int energy = this.getEnergyLevel()-100;
		this.setEnergyLevel(energy);
	}
}