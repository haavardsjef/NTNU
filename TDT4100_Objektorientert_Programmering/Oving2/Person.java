package encapsulation;
import java.util.Date;

public class Person {
    // Private fields
    private String name;
    private String email;
    private Date birthday;
    private char gender;
    final static String[] landskoder = {"ad", "ae", "af", "ag", "ai", "al", "am", "ao", "aq", "ar", "as", "at", "au", "aw", "ax", "az", "ba", "bb", "bd", "be", "bf", "bg", "bh", "bi", "bj", "bl", "bm", "bn", "bo", "bq", "br", "bs", "bt", "bv", "bw", "by", "bz", "ca", "cc", "cd", "cf", "cg", "ch", "ci", "ck", "cl", "cm", "cn", "co", "cr", "cu", "cv", "cw", "cx", "cy", "cz", "de", "dj", "dk", "dm", "do", "dz", "ec", "ee", "eg", "eh", "er", "es", "et", "fi", "fj", "fk", "fm", "fo", "fr", "ga", "gb", "gd", "ge", "gf", "gg", "gh", "gi", "gl", "gm", "gn", "gp", "gq", "gr", "gs", "gt", "gu", "gw", "gy", "hk", "hm", "hn", "hr", "ht", "hu", "id", "ie", "il", "im", "in", "io", "iq", "ir", "is", "it", "je", "jm", "jo", "jp", "ke", "kg", "kh", "ki", "km", "kn", "kp", "kr", "kw", "ky", "kz", "la", "lb", "lc", "li", "lk", "lr", "ls", "lt", "lu", "lv", "ly", "ma", "mc", "md", "me", "mf", "mg", "mh", "mk", "ml", "mm", "mn", "mo", "mp", "mq", "mr", "ms", "mt", "mu", "mv", "mw", "mx", "my", "mz", "na", "nc", "ne", "nf", "ng", "ni", "nl", "no", "np", "nr", "nu", "nz", "om", "pa", "pe", "pf", "pg", "ph", "pk", "pl", "pm", "pn", "pr", "ps", "pt", "pw", "py", "qa", "re", "ro", "rs", "ru", "rw", "sa", "sb", "sc", "sd", "se", "sg", "sh", "si", "sj", "sk", "sl", "sm", "sn", "so", "sr", "ss", "st", "sv", "sx", "sy", "sz", "tc", "td", "tf", "tg", "th", "tj", "tk", "tl", "tm", "tn", "to", "tr", "tt", "tv", "tw", "tz", "ua", "ug", "um", "us", "uy", "uz", "va", "vc", "ve", "vg", "vi", "vn", "vu", "wf", "ws", "ye", "yt", "za", "zm", "zw"};
    
    
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
	if (!email.substring(0, email.indexOf("@")).replace('.', ' ').equals(this.name)) {
	    throw new IllegalArgumentException("Eposten må inneholde fornavn og etternavn");
	}
	
	//Sjekk at domene.landskode kommer etter @
	System.out.println(email.substring(email.indexOf("@")+1));
	//String[] temp = email.substring(email.indexOf("@")+1).split(".");
	String[] temp = "ntnu.no".split(".");
	
	System.out.println(temp.length);
	if (temp.length != 2) {
	    throw new IllegalArgumentException("Eposten må være på formen fornavn.etternavn@domene.landskode");
	}
	if (!lovliglandskode(temp[1])) {
	    throw new IllegalArgumentException("Eposten må inneholde en lovlig landskode!");
	}
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
    
    
    private static boolean lovliglandskode(String kode) {
	for (String landskode : landskoder) {
	    if (kode == landskode) {
		return true;
	    }
	}
	return false;
    }
    
    
    
public static void main(String[] args) {
    Person per1 = new Person();
    per1.setName("ola nordmann");
   // System.out.println(per1.getName());
    per1.setEmail("ola.nordmann@ntnu.no");
    System.out.println(per1.getEmail());
    
}
    
    
    

}
