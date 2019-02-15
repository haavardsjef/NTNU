package app;

import java.util.ArrayList;

public class KarakterKalkulator {
    // Fields
    ArrayList<Emne> subjects = new ArrayList<Emne>();
    
    
    // Constructor
    public KarakterKalkulator() {
    }
    
    public void addEmne(String emneKode, String emneNavn, float Studiepoeng, char Karakter) {
	this.subjects.add(new Emne(emneKode, emneNavn, Studiepoeng, Karakter));
    }
    
    public float getAverage() {
	float effectivePoints = 0;
	float totalPoints = 0;
	for (Emne subject : subjects) {
	    if (subject.getEffectivePoints() != 0) {
		effectivePoints += subject.getEffectivePoints();
		totalPoints += subject.getPoints();
	    }    
	}
	return effectivePoints / totalPoints;
    }
    
    public char getCharAverage() {
	if (getAverage() > 4.5f) {
	    return 'A';
	}
	if (getAverage() > 3.5f) {
	    return 'B';
	}
	if (getAverage() > 2.5f) {
	    return 'C';
	}
	if (getAverage() > 1.5f) {
	    return 'D';
	}
	return 'E';
    }
    
    public float getTotalPoints() {
	float totalPoints = 0;
	for (Emne subject : subjects) {
	    totalPoints += subject.getPoints();
	}
	return totalPoints;
    }
    
    public static void main(String[] args) {
	KarakterKalkulator Bruker1 = new KarakterKalkulator();
	Bruker1.addEmne("TDT4110", "ITGK", 7.5f, 'A'); 
	Bruker1.addEmne("TDT4100", "Objekt", 7.5f, 'B');
	Bruker1.addEmne("MA1201", "LinAlg1", 3.7f, 'B');
	Bruker1.addEmne("ProgLab", "Proglab", 7.5f, 'G');
	System.out.println(Bruker1.getAverage());
	System.out.println("Karaktersnitt: " + Bruker1.getCharAverage());
	
    }
}
