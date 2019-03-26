package patterns.observable;

import java.util.ArrayList;

public class ObservableHighscoreList extends ObservableList{
	// FIELDS
	//private ArrayList<Integer> highscores = new ArrayList<Integer>();
	//private ArrayList<ObservableListListener> listeners = new ArrayList<ObservableListListener>();
	private int maxSize;
	
	
	
	// CONSTRUCTOR
	public ObservableHighscoreList(int maxSize) {
		this.maxSize = maxSize;
		list = new ArrayList<Object>();
	}
	
	// METHODS
	
	public void addResult(int result) { // Basic Bubblesort
		int position = -1;
		boolean removed = false;
		for (int i = 0; i < size(); i++) {
			if ((int) getElement(i) > result) {
				addElement(i, result);
				position = i;
				break;
			}
		}
		if(position == -1) {
			addElement(result);
		}
		if (size() > maxSize) {
			removeElement(size()-1);
			removed = true;
		}
		if (position == -1 && removed == false) {
		    updateListeners(size()-1);
		}	
		if (position != -1) {
		    updateListeners(position);
		}
	}
	
	
	public boolean acceptsElement(Object object) {
	    return object instanceof Integer;
	}
	
	
	
	
	
	
	
	public static void main(String[] args) {
		HighscoreList h1 = new HighscoreList(10);
		h1.addResult(5);
		System.out.println(h1);
		h1.addResult(6);
		System.out.println(h1);
		h1.addResult(2);
		System.out.println(h1);
	}
	
}