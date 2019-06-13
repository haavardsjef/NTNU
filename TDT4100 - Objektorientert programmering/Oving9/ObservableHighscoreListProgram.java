package patterns.observable;

import java.util.Scanner;

public class ObservableHighscoreListProgram implements ObservableListListener{
	
	ObservableHighscoreList h1;
	
	// CONSTRUCTOR
	public ObservableHighscoreListProgram() {
	    
	}
	public void listChanged(ObservableList highscores, int position) {
		System.out.println("List changed at position: " + position);
		System.out.println("Current highscores: " + highscores.toString());
		
	    }	
	
	public void init() {
		h1 = new ObservableHighscoreList(7);
		h1.addObservableListListener(this);
	}
	
	public void run() {
		Scanner sc1 = new Scanner(System.in);
		for(int i = 0; i < 100; i++){
			h1.addResult(sc1.nextInt());
		}
		sc1.close();
	}
		
	
	
	public static void main(String[] args) {
		ObservableHighscoreListProgram hlp = new ObservableHighscoreListProgram();
		hlp.init();
		hlp.run();
	}

}