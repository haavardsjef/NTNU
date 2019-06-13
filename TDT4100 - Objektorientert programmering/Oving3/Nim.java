package encapsulation;
// Skrevet av Håvard Hjelmeseth 28.01.2019

public class Nim {
    // FIELDS
    int[] piles = new int[3];
    
    // CONSTRUCTORS
    public Nim(int pileSize) {
	for (int i = 0; i < piles.length; i++) {
	    piles[i] = pileSize;
	}
    }
    
    public Nim() {
	for (int i = 0; i < piles.length; i++) {
	    piles[i] = 10;
	}
    }
    
    
    // METHODS
    
    public void removePieces(int number, int targetPile) {
	if (isGameOver()) {
	    throw new IllegalStateException("Spillet er over!");
	}
	if (targetPile < 0 || targetPile > piles.length-1) {
	    throw new IllegalArgumentException("Velg mellom haug 0, 1 eller 2!");
	}
	if (!isValidMove(number, targetPile)) {
	    throw new IllegalArgumentException("Ulovlig trekk!");
	}
	piles[targetPile] -= number;
	
    }
    
    
    public boolean isValidMove(int number, int targetPile) {
	if (number >= 1 && number <= piles[targetPile] && !isGameOver()) {
	    return true;
	}
	return false;
    }
    
    public boolean isGameOver() {
	for (int pile : piles) {
	    if (pile == 0) {
		return true;
	    }
	}
	return false;
    }
    
    public int getPile(int targetPile) {
	return piles[targetPile];
    }
    
    public String toString() {
	String temp = "";
	for (int i = 0; i < piles.length; i++) {
	    temp += ("Haug " + i + ": " + getPile(i) + "\n");
	}
	return temp;
    }
}
