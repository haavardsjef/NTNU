package patterns.observable;

import java.util.ArrayList;

public abstract class ObservableList {

    // FIELDS
    protected ArrayList<Object> list = new ArrayList<Object>();
    private ArrayList<ObservableListListener> listeners = new ArrayList<ObservableListListener>();
    
    // METHODS
    public int size() {
	return list.size();
    }
    
    public Object getElement(int index) {
	if (list.size() > index && index >= 0) {
		return list.get(index);
	}
	return null;
    }
    
    public void addElement(int index, Object element) { // Basic Bubblesort
	if (!acceptsElement(element)) {
	    throw new IllegalArgumentException();
	}
	if (index < 0 || index > list.size()) {
	    throw new IndexOutOfBoundsException();
	}
	list.add(index, element);
	updateListeners(index);
    }
    
    public void addElement(Object element) {
	if (!acceptsElement(element)) {
	    throw new IllegalArgumentException();
	}
	list.add(element);
    }
    
    public void removeElement(int index) {
	if (index < 0 || index > list.size()) {
	    throw new IndexOutOfBoundsException();
	}
	list.remove(index);
    }
    
    public void addObservableListListener(ObservableListListener listener){
	if (!listeners.contains(listener)) {
		listeners.add(listener);
	}
    }
    
    public void removeObservableListListener(ObservableListListener listener) {
	if (listeners.contains(listener)) {
		listeners.remove(listener);
	}
    }
    
    public void updateListeners(int index) {
	for (ObservableListListener listener : listeners) {
		listener.listChanged(this,index);
	}
}
    
    public String toString() {
	if (list.isEmpty()) {
		return "Empty list!";
	}
	else {
		String temp = "";
		for (Object object : list) {
			temp += object;
			temp += ", ";
		}
		return temp;
	}
}
    
    // ABSTRACT METHODS
    public abstract boolean acceptsElement(Object element);
}
