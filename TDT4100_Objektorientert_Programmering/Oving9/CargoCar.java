package inheritance;

public class CargoCar extends TrainCar {
	
	// FIELDS
	private int cargoWeight;
	
	
	public CargoCar(int deadWeight, int cargoWeight) {
		super(deadWeight);
		this.cargoWeight = cargoWeight;	
	}
	
	public int getCargoWeight() {
		return cargoWeight;
	}
	
	public void setCargoWeight(int cargoWeight) {
		this.cargoWeight = cargoWeight;
	}
	
	public int getTotalWeight() {
		return getDeadWeight() + getCargoWeight();
	}

	public int getPassengerCount() {
		return 0;
	}
}
