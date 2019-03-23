package inheritance;

public class TrainCar {
		
	
	// FIELDS
	private int deadWeight;
	
	public TrainCar(int deadWeight) {
		this.deadWeight = deadWeight;
	}
	
	public int getTotalWeight() {
		return deadWeight;
	}
	
	public void setDeadWeight(int deadWeight) {
		this.deadWeight = deadWeight;
	}
	
	public int getDeadWeight() {
		return deadWeight;
	}
	
}
