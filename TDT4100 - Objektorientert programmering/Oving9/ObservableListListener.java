package patterns.observable;

public interface ObservableListListener {
	public void listChanged(ObservableList highscores, int position);
}