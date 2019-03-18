package app;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.Scanner;


import javafx.collections.ObservableList;

public class SubjectList implements FileHandle{
	
	
	public SubjectList() {
		
	}

	@Override
	public void saveState(String filename, ObservableList<Subject> subjectData) {
		
		
		try
        {
            PrintWriter outFile = new PrintWriter(new FileOutputStream(filename+".csv", false));
            for (Subject subject: subjectData) {
            	outFile.print(subject.subjectID+ ',');
            	outFile.print(subject.subjectName+ ',');
            	outFile.print(subject.points + ",");
            	outFile.println(subject.grade);
            }
            outFile.close();
        }
        catch (FileNotFoundException e)
        {
            System.err.println("Error: file " + filename + ".csv could not be opened for writing.");
            System.exit(1);
        }
		
	}

	@Override
	public ObservableList<Subject> loadState(String filename, ObservableList<Subject> subjectData) {
        try
        {
            Scanner in = new Scanner(new FileReader(filename + ".csv"));
            subjectData.clear();
            
            while(in.hasNext()){
                String line = in.nextLine();
                subjectData.add(new Subject(line));
            }
            
             
            in.close();
            return subjectData;
        }
        catch (FileNotFoundException e)
        {
            System.err.println("Error: file " + filename + ".csv could not be opened. Does it exist?");
            System.exit(1);

        }
        return subjectData;
		
	}
	
	

}
