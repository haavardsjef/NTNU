package app.view;

//Import shit
import app.App;
import app.Subject;
import app.SubjectList;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Label;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;

public class AppController {
	// FIELDS
    @FXML
    private TableView<Subject> subjectTable;
    @FXML
    private TableColumn<Subject, String> subjectIDColumn;
    @FXML
    private TableColumn<Subject, String> subjectNameColumn;
    @FXML
    private TableColumn<Subject, String> subjectGradeColumn;

    @FXML
    private Label subjectIDLabel;
    @FXML
    private Label subjectNameLabel;
    @FXML
    private Label subjectPointsLabel;
    @FXML
    private Label subjectGradeLabel;
    @FXML
    private Label gradeAverageLabel;
    @FXML
    private Label gradeAverageNumericalLabel;
    @FXML
    private Label totalPointsLabel;
    @FXML
    private ObservableList<Subject> subjectList;
    @FXML
    private TextField saveID;

    // Reference to the main application.
    private App app;

    /**
     * The constructor.
     * The constructor is called before the initialize() method.
     */
    
    // Konstruktør
    public AppController() {
    }

    /**
     * Initializes the controller class. This method is automatically called
     * after the fxml file has been loaded.
     */
    @FXML
    private void initialize() {
        // Initialize the subject table with the two columns.
        subjectIDColumn.setCellValueFactory(
                cellData -> cellData.getValue().subjectIDProperty());
        subjectNameColumn.setCellValueFactory(
                cellData -> cellData.getValue().subjectNameProperty());
        subjectGradeColumn.setCellValueFactory(
                cellData -> cellData.getValue().subjectGradeProperty());

        // Clear subject details.
        showSubjectDetails(null);
        

        // Listen for selection changes and show the subject details when changed.
        subjectTable.getSelectionModel().selectedItemProperty().addListener(
                (observable, oldValue, newValue) -> showSubjectDetails(newValue));
    }

    /**
     * Is called by the main application to give a reference back to itself.
     * 
     * @param mainApp
     */
    public void setApp(App app) {
        this.app = app;

        // Add observable list data to the table
        subjectTable.setItems(app.getSubjectData());
    }
    
    /**
     * Fills all text fields to show details about the subject.
     * If the specified subject is null, all text fields are cleared.
     * 
     * @param subject the subject or null
     */
    private void showSubjectDetails(Subject subject) {
        if (subject != null) {
            // Fill the labels with info from the subject object.
            subjectIDLabel.setText(subject.getSubjectID());
            subjectNameLabel.setText(subject.getSubjectName());
            subjectPointsLabel.setText(String.valueOf(subject.getPoints()));
            subjectGradeLabel.setText(String.valueOf(subject.getGrade()));
        } else {
            // Subject is null, remove all the text.
        	subjectIDLabel.setText("");
            subjectNameLabel.setText("");
            subjectPointsLabel.setText("");
            subjectGradeLabel.setText("");
        }
    }
    
    
    // REFRESH TOTALS
    public void setData(ObservableList<Subject> subjects) {
    	this.subjectList = subjects;
    	if (subjectList.isEmpty()) {
    		System.out.println("Empty");
    		gradeAverageLabel.setText("");
    		gradeAverageNumericalLabel.setText("");
    		totalPointsLabel.setText("");
    	}
    	else {
    		gradeAverageLabel .setText(String.valueOf(getCharAverage()));
    		gradeAverageNumericalLabel.setText(String.valueOf(getAverage()));
    		totalPointsLabel.setText(String.valueOf(getTotalPoints()));
    	}
    }
   
    

    
    /**
     * Called when the user clicks on the delete button.
     */
    @FXML
    private void handleDeleteSubject() {
        int selectedIndex = subjectTable.getSelectionModel().getSelectedIndex();
        if (selectedIndex >= 0) {
            subjectTable.getItems().remove(selectedIndex);
        } else {
            // Nothing selected.
            Alert alert = new Alert(AlertType.WARNING);
            alert.initOwner(app.getPrimaryStage());
            alert.setTitle("No Selection");
            alert.setHeaderText("Ingen emner valgt");
            alert.setContentText("Velg ett emne i tabellen.");

            alert.showAndWait();
        }
        app.refresh(subjectList);
    }
    
    /**
     * Called when the user clicks the new button. Opens a dialog to edit
     * details for a new subject.
     */
    
    @FXML
    private void handleNewSubject() {
        Subject tempSubject = new Subject();
        boolean okClicked = app.showSubjectEditDialog(tempSubject);
        if (okClicked) {
            app.getSubjectData().add(tempSubject);
        }
        app.refresh(subjectList);
    }

    /**
     * Called when the user clicks the edit button. Opens a dialog to edit
     * details for the selected subject.
     */
    @FXML
    private void handleEditSubject() {
        Subject selectedSubject = subjectTable.getSelectionModel().getSelectedItem();
        if (selectedSubject != null) {
            boolean okClicked = app.showSubjectEditDialog(selectedSubject);
            if (okClicked) {
                showSubjectDetails(selectedSubject);
            }

        } else {
            // Nothing selected.
            Alert alert = new Alert(AlertType.WARNING);
            alert.initOwner(app.getPrimaryStage());
            alert.setTitle("No Selection");
            alert.setHeaderText("Ingen emner valgt");
            alert.setContentText("Velg ett emne i tabellen.");

            alert.showAndWait();
        }
        app.refresh(subjectList);
    }
    
    public float getAverage() {
    	float effectivePoints = 0;
    	float totalPoints = 0;
    	for (Subject subject : subjectList) {
    	    if (subject.getEffectivePoints() != 0) {
    		effectivePoints += subject.getEffectivePoints();
    		totalPoints += subject.getPoints();
    	    }    
    	}
    	return effectivePoints / totalPoints;
        }
    
    public char getCharAverage() {
    	if (getAverage() >= 4.5f) {
    	    return 'A';
    	}
    	if (getAverage() >= 3.5f) {
    	    return 'B';
    	}
    	if (getAverage() >= 2.5f) {
    	    return 'C';
    	}
    	if (getAverage() >= 1.5f) {
    	    return 'D';
    	}
    	return 'E';
    }
    
    public float getTotalPoints() {
    	float totalPoints = 0;
    	for (Subject subject : subjectList) {
    	    totalPoints += subject.getPoints();
    	}
    	return totalPoints;
    }
    
    @FXML
    private void handleSave() {
    	if (saveID.getText() != null && saveID.getText() != " ") {
    		System.out.println("y");
    		System.out.println(saveID.getText());
    		SubjectList savestate = new SubjectList();
        	savestate.saveState(saveID.getText(), subjectList);
    	}
    	else {
    		System.out.println("n");
    	}

    }
    
    @FXML
    private void handleLoad() {
    	if (isValidSaveID()) {
    		SubjectList savestate = new SubjectList();
        	subjectList = savestate.loadState(saveID.getText(), subjectList);
        	app.refresh(subjectList);
    	}
    }
}