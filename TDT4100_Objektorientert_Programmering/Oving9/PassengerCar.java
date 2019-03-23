package inheritance;

public class PassengerCar extends TrainCar{


	// FIELDS
	private int passengerCount;

	
	public PassengerCar(int deadWeight, int passengerCount) {
		super(deadWeight);
		this.passengerCount = passengerCount;
	}
	
	public int getPassengerCount() {
		return passengerCount;
	}
	
	public void setPassengerCount(int passangerCount) {
		this.passengerCount = passangerCount;
	}
	
	public int getTotalWeight() {
		return getDeadWeight() + 80 * getPassengerCount();
	}
}
