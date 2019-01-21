package encapsulation;
import java.util.Date;

public class Person {
    // Private fields
    private String name;
    private String email;
    private Date birthday;
    private char gender;
    
    
    // Public methods
    public Person() {
	
    }
    
    
    public String getName() {
        return name;
    }
    public void setName(String name) {	
	// Sjekk at navnet inneholder nøyaktig ett mellomrom
	if (name.length()-name.replaceAll(" ", "").length() != 1) {
	    throw new IllegalArgumentException("Navnet må inneholde både fornavn og etternavn, og kan ikke inneholde mellomnavn");
	}
	
	// Sjekk at begge navnene har minst 2 i lengde.
	if (name.substring(0, name.indexOf(" ")).length() < 2 || name.substring(name.indexOf(" ")+1).length() < 2) {
	    throw new IllegalArgumentException("Begge navnene må være minst 2 bokstaver!");
	}
	
	
	// Sjekk at navnet ikke inneholder noen ulovlige tegn.
	for (char c: name.replaceAll(" ", "").toCharArray()) {
	    if (!Character.isLetter(c)) {
		throw new IllegalArgumentException("Navnet kan bare inneholde bokstaver!");
	    }
	}
	
	this.name = name;
    }
    
    
    //Epost
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
	// Sjekk om eposten  inneholder nøyaktig en @
	if (email.length()-email.replaceAll("@", "").length() != 1){
	    throw new IllegalArgumentException("Eposten må inneholde nøyaktig en alfakrøll, eposten skal være på formen fornavn.etternavn@domene.landskode");
	}
	
	//Sjekk at fornavn.etternavn kommer før @
	if (email.substring(0, email.indexOf("@")).replaceAll(".", " ") != name) {
	    throw new IllegalArgumentException("Eposten må være på formen fornavn.etternavn@domene.landskode");
	}
	
	//Sjekk at domene.landskode kommer etter @
	if (email.substring(email.indexOf("@")).split(".") )
        this.email = email;
    }
    
    
    //Birthday
    public Date getBirthday() {
        return birthday;
    }
    public void setBirthday(Date birthday) {
        this.birthday = birthday;
    }
    
    
    // Gender
    public char getGender() {
        return gender;
    }
    public void setGender(char gender) {
	if (!(gender == 'M' || gender == 'F' || gender == '\0')) {
	    throw new IllegalArgumentException("Kjønn må være 'M', 'F' eller ingenting.");
	}
        this.gender = gender;
    }
    
    
public static void main(String[] args) {
    Person per1 = new Person();
    per1.setName("Ola Nordmann");
    System.out.println(per1.getName());
    
}
    
    
    

}
