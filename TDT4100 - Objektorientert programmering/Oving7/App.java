package app;

//Import shit
import java.io.IOException;
import app.view.AppController;
import app.view.SubjectEditDialogController;
import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.BorderPane;
import javafx.stage.Modality;
import javafx.stage.Stage;


public class App extends Application{

	// FIELDS
    private Stage primaryStage;
    private BorderPane rootLayout;
    private ObservableList<Subject> subjectData = FXCollections.observableArrayList(); // List to contain subjects

    // Constructor
    public App() {
        // Sample data
        subjectData.add(new Subject("TDT4110", "Informasjonsteknologi grunnkurs", 7.5f, 'A'));
        subjectData.add(new Subject("TMA4100", "Matematikk 1", 7.5f, 'A'));
        subjectData.add(new Subject("TDT4140", "Diskret Matematikk", 7.5f, 'A'));
        subjectData.add(new Subject("EXPH0006", "Examen philosophicum for teknologi og realfag", 7.5f, 'C'));
        subjectData.add(new Subject("MA1201", "Lineær algebra og geometri", 3.7f, 'B'));
        subjectData.add(new Subject("MA1202", "Lineær algebra med anvendelser", 3.8f, 'A'));
    }
  
    // Standard getter
    public ObservableList<Subject> getSubjectData() {
        return subjectData;
    }

    // Start method
    public void start(Stage primaryStage) {
        this.primaryStage = primaryStage;
        this.primaryStage.setTitle("Karakterkalkulator");

        initRootLayout();
        showApp();
    }
    
    // Initialize root layout
    public void initRootLayout() {
        try {
            // Load root layout from fxml file.
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(App.class.getResource("view/RootLayout.fxml"));
            rootLayout = (BorderPane) loader.load();
            
            // Show the scene containing the root layout.
            Scene scene = new Scene(rootLayout);
            primaryStage.setScene(scene);
            primaryStage.show();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Show the App inside of rootLayout
    public void showApp() {
        try {
            // Load  app.
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(App.class.getResource("view/App.fxml"));
            AnchorPane app = (AnchorPane) loader.load();
            
            // Set  app into the center of root layout.
            rootLayout.setCenter(app);

            // Give the controller access to the main app.
            AppController controller = loader.getController();
            controller.setApp(this);
            controller.setData(subjectData);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    public Stage getPrimaryStage() {
        return primaryStage;
    }
    
    /**
     * Opens a dialog to edit details for the specified . If the user
     * clicks OK, the changes are saved into the provided  object and true
     * is returned.
     * 
     * @param subject the  object to be edited
     * @return true if the user clicked OK, false otherwise.
     */
    
    // Opens window to edit subject
    public boolean showSubjectEditDialog(Subject subject) {
        try {
            // Load the fxml file, create a new stage for the new window
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(App.class.getResource("view/SubjectEditDialog.fxml"));
            AnchorPane page = (AnchorPane) loader.load();

            // Create the new Stage.
            Stage dialogStage = new Stage();
            dialogStage.setTitle("Rediger emne");
            dialogStage.initModality(Modality.WINDOW_MODAL);
            dialogStage.initOwner(primaryStage);
            Scene scene = new Scene(page);
            dialogStage.setScene(scene);

            // Set the subject into the controller.
            SubjectEditDialogController controller = loader.getController();
            controller.setDialogStage(dialogStage);
            controller.setSubject(subject);

            // Show the dialog and wait until the user closes it
            dialogStage.showAndWait();
            
            	
            return controller.isOkClicked();
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    }
    
    public boolean refresh(ObservableList<Subject> subjectData) {
    	try {
            // Load  overview.
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(App.class.getResource("view/App.fxml"));
            AnchorPane app = (AnchorPane) loader.load();
            
            // Set  overview into the center of root layout.
            rootLayout.setCenter(app);

            // Give the controller access to the main app.
            AppController controller = loader.getController();
            controller.setApp(this);
            
            
            // Show the averages
            controller.setData(subjectData);

        } catch (IOException e) {
            e.printStackTrace();
        }
		return true;
    }    
    
    // Main methods
    public static void main(String[] args) {
        launch(args);
    }
}