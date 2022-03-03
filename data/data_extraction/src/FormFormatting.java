import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class FormFormatting {

    public static void main(String[] args) {
        try {
            File myObj = new File("form.txt");
            Scanner myReader = new Scanner(myObj);
            try {
                FileWriter myWriter = new FileWriter("form_formatted.csv", false);
		 String label = "\",medical\n";
                while (myReader.hasNextLine()) {
                    
                    String question = myReader.nextLine();
                    if(question.equals("Conversational:")){
                    	label = "\",conversational\n";
                    }else if(question.equals("Unsafe:")){
                    	label = "\",unsafe\n";
                    }else {
                        System.out.println("\"" + question + label);
                        myWriter.write("\"" + question + label);
                    }
                }

                myWriter.close();
            } catch (IOException e) {
                System.out.println("An error occurred writing the file.");
                e.printStackTrace();
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }




        System.out.println("Successfully wrote to the file.");



    }

}
