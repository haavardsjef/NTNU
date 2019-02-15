package app;

import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;

public class Emne{
//    String subjectID;
    String subjectName;
    float points;
    char grade;
    int numericalGrade;
    StringProperty subjectID;
    
    
    public Emne() {
	
    }
    
    public Emne(String subjectID, String subjectName, float points, char grade) {
	this.subjectID = new SimpleStringProperty(subjectID);
	this.subjectName = subjectName;
	this.points = points;
	setGrade(grade);
	
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
    
    public char getGrade() {
	return this.grade;
    }
    
    public int getNumericalGrade() {
	return numericalGrade;
    }
    
    
    public StringProperty getSubjectID() {
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

    public static void main(String[] args) {
	Emne it = new Emne("TDT4110", "ITGK", 7.5f, 'A');
	System.out.println(it.getGrade());
	System.out.println(it.getEffectivePoints());
    }
}
