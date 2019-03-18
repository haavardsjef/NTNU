package app.view;

//Import shit
import app.Subject;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.TextField;
import javafx.stage.Stage;


// Dialog to edit details of a subject.

public class SubjectEditDialogController {

    @FXML
    private TextField subjectIDField;
    @FXML
    private TextField subjectNameField;
    @FXML
    private TextField subjectPointsField;
    @FXML
    private TextField subjectGradeField;


    private Stage dialogStage;
    private Subject subject;
    private boolean okClicked = false;

    /**
     * Initializes the controller class. This method is automatically called
     * after the fxml file has been loaded.
     */
    @FXML
    private void initialize() {
    }

    /**
     * Sets the stage of this dialog.
     * 
     * @param dialogStage
     */
    public void setDialogStage(Stage dialogStage) {
        this.dialogStage = dialogStage;
    }

    /**
     * Sets the subject to be edited in the dialog.
     * 
     * @param subject
     */
    public void setSubject(Subject subject) {
        this.subject = subject;

        subjectIDField.setText(subject.getSubjectID());
        subjectNameField.setText(subject.getSubjectName());
        subjectPointsField.setText(String.valueOf(subject.getPoints()));
        subjectGradeField.setText(String.valueOf(subject.getGrade()));
    }

    /**
     * Returns true if the user clicked OK, false otherwise.
     * 
     * @return
     */
    public boolean isOkClicked() {
        return okClicked;
    }

    /**
     * Called when the user clicks ok.
     */
    @FXML
    private void handleOk() {
        if (isInputValid()) {
            subject.setSubjectID(subjectIDField.getText());
            subject.setSubjectName(subjectNameField.getText());
            subject.setSubjectPoints(subjectPointsField.getText());
            subject.setSubjectGrade(subjectGradeField.getText());

            okClicked = true;
            dialogStage.close();
        }
    }

    /**
     * Called when the user clicks cancel.
     */
    @FXML
    private void handleCancel() {
        dialogStage.close();
    }

    /**
     * Validates the user input in the text fields.
     * 
     * @return true if the input is valid
     */
    private boolean isInputValid() {
        String errorMessage = "";

        if (subjectIDField.getText() == null || subjectIDField.getText().length() == 0) {
            errorMessage += "No valid subject ID!\n"; 
        }
        if (subjectNameField.getText() == null || subjectNameField.getText().length() == 0) {
            errorMessage += "No valid subject Name!\n"; 
        }
        if (subjectPointsField.getText() == null || subjectPointsField.getText().length() == 0 || subjectPointsField.getText().substring(subjectPointsField.getText().indexOf('.')).length() != 2 ){
            errorMessage += "Vennligst oppgi ett desimaltall med nøyaktig en desimal!\n"; 
        }

        if (subjectGradeField.getText() == null || subjectGradeField.getText().length() == 0) {
            errorMessage += "No valid grade!\n"; 
        } 

        if (errorMessage.length() == 0) {
            return true;
        } else {
            // Show the error message.
            Alert alert = new Alert(AlertType.ERROR);
            alert.initOwner(dialogStage);
            alert.setTitle("Invalid Fields");
            alert.setHeaderText("Please correct invalid fields");
            alert.setContentText(errorMessage);
            
            alert.showAndWait();
            
            return false;
        }
    }
}