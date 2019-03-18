package app;

// Import shit
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;

public class Subject{
    String subjectID;
    String subjectName;
    float points;
    char grade;
    int numericalGrade;

    
    
    public Subject() {
    	this.points = 7.5f;
	
    }
    
    public Subject(String subjectID, String subjectName, float points, char grade) {
    	this.subjectID =  subjectID;
    	this.subjectName = subjectName;
		this.points = points;
		setGrade(grade);
	
    }
    
    public Subject(String savedInfo) {
    	String[] infoList = savedInfo.split(",");
    	this.setSubjectID(infoList[0]);
    	this.setSubjectName(infoList[1]);
    	this.setSubjectPoints(infoList[2]);
    	this.setGrade(infoList[3].charAt(0));
    	
    }
    public boolean setGrade(char grade) {
	if (grade == 'A') {
	    numericalGrade = 5;
	    this.grade = grade;
	    return true;
	}
	if (grade == 'B') {
	    numericalGrade = 4;
	    this.grade = grade;
	    return true;
	}
	if (grade == 'C') {
	    numericalGrade = 3;
	    this.grade = grade;
	    return true;
	}
	if (grade == 'D') {
	    numericalGrade = 2;
	    this.grade = grade;
	    return true;
	}
	if (grade == 'E') {
	    numericalGrade = 1;
	    this.grade = grade;
	    return true;
	}
	if (grade == 'G') {
	    numericalGrade = 0;
	    this.grade = grade;
	    return true;
	}
        return false;
    }
    
    public void setSubjectID(String subjectID) {
    	this.subjectID = subjectID;
    }
    public void setSubjectName(String subjectName) {
    	this.subjectName = subjectName;
    }
    public void setSubjectPoints(String points) {
    	this.points = Float.valueOf(points);
    }
    
    public void setSubjectGrade(String grade) {
    	setGrade(grade.charAt(0));
    }
    
    public char getGrade() {
	return this.grade;
    }
    
    public int getNumericalGrade() {
	return numericalGrade;
    }
    
    
    public String getSubjectID() {
        return subjectID;
    }

    public String getSubjectName() {
        return subjectName;
    }

    public float getPoints() {
        return points;
    }
    
    public float getEffectivePoints() {
	return points * numericalGrade;
    }
    
    public StringProperty subjectIDProperty() {
        return (new SimpleStringProperty(subjectID));
    }
    
    public StringProperty subjectNameProperty() {
        return (new SimpleStringProperty(subjectName));
    }
    
    public StringProperty subjectGradeProperty() {
        return (new SimpleStringProperty(String.valueOf(grade))); 	// Converts grade to string then to StringProperty
    }
}
