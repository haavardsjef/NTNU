package inheritance;

import java.util.ArrayList;
import inheritance.TrainCar;
import inheritance.CargoCar;
import inheritance.PassengerCar;

public class Train{
	
	// FIELD
	public ArrayList<TrainCar> locomotive = new ArrayList<TrainCar>();
	
	
	public Train() {
	}
	
	public void addTrainCar(TrainCar trainCar) {
		locomotive.add(trainCar);
	}
	
	public boolean contains(TrainCar trainCar) {
		return locomotive.contains(trainCar);
	}
	
	public int getTotalWeight() {
		int totalWeight = 0;
		for (TrainCar trainCar: locomotive) {
			totalWeight += trainCar.getTotalWeight();
		}
		return totalWeight;
	}
	
	public int getPassengerCount() {
		int passengerCount = 0;
		for (TrainCar trainCar: locomotive) {
			if (trainCar instanceof PassengerCar) {
				passengerCount += ((PassengerCar) trainCar).getPassengerCount();
			}
		}
		return passengerCount;
	}
	
	public int getCargoWeight() {
		int cargoWeight = 0;
		for (TrainCar trainCar: locomotive) {
			if (trainCar instanceof CargoCar) {
				cargoWeight += ((CargoCar) trainCar).getCargoWeight();
			}
		}
		return cargoWeight;
	}
	
	public static void main(String[] args) {
		Train t = new Train();
		t.addTrainCar(new CargoCar(100,100));
		t.addTrainCar(new PassengerCar(10, 1));
		System.out.println(t.getPassengerCount());
		//System.out.println(t.getCargoWeight());
	}
}
