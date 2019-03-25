package patterns.observable;

import java.util.ArrayList;

public class HighscoreList {
	// FIELDS
	private ArrayList<Integer> highscores = new ArrayList<Integer>();
	private ArrayList<HighscoreListListener> listeners = new ArrayList<HighscoreListListener>();
	private int maxSize;
	
	
	
	// CONSTRUCTOR
	public HighscoreList(int maxSize) {
		this.maxSize = maxSize;
	}
	
	// METHODS
	
	public int addResult(int result) { // Basic Bubblesort
		int position = -1;
		for (int i = 0; i < highscores.size(); i++) {
			if (highscores.get(i) >= result) {
				highscores.add(i, result);
				position = i;
				break;
			}
		}
		if(position == -1) {
			highscores.add(result);
			position = highscores.size()-1;
		}
		if (highscores.size() > maxSize) {
			highscores.remove(highscores.size()-1);
		}
		updateListeners(position);
		return position;
	}
	
	public int size() {
		return highscores.size();
	}
	
	public int getElement(int index) {
		if (highscores.size() > index && index >= 0) {
			return highscores.get(0);
		}
		return -1;
	}
	
	
	public String toString() {
		if (highscores.isEmpty()) {
			return "No highscores!";
		}
		else {
			String temp = "";
			for (int highscore : highscores) {
				temp += highscore;
				temp += ", ";
			}
			return temp;
		}
	}
	
	public void addHighscoreListListener(HighscoreListListener listener){
		if (!listeners.contains(listener)) {
			listeners.add(listener);
		}
	}
	
	public void removeHighscoreListListener(HighscoreListListener listener) {
		if (listeners.contains(listener)) {
			listeners.remove(listener);
		}
	}
	
	public void updateListeners(int index) {
		for (HighscoreListListener listener : listeners) {
			listener.listChanged(this,index);
		}
	}
	
	public static void main(String[] args) {
		HighscoreList h1 = new HighscoreList(10);
		h1.addResult(5);
		h1.addResult(6);
		h1.addResult(2);
		System.out.println(h1);
	}
	
}
