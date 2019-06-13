package objectstructures;

public class Partner {
    // FIELDS
    private String name;
    private Partner partner;
    
    // CONSTRUCTOR
    public Partner(String name) {
	this.name = name;
    }
    
    public String getName() {
	return name;
    }
    
    public Partner getPartner() {
	return partner;
    }
    
    public void setPartner(Partner partner) {
	if (this.partner == null) {
    		this.partner = partner;
	}
	if (this.partner != null) {
	    partner.setPartner(this);
	}
    }
    
}
