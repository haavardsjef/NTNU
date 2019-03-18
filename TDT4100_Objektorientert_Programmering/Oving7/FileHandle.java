package app;

import javafx.collections.ObservableList;

public interface FileHandle {
	public void saveState(String filename, ObservableList<Subject> subjectData);
	public ObservableList<Subject> loadState(String filename, ObservableList<Subject> subjectData);
}
