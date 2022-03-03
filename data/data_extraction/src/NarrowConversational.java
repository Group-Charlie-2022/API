import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashSet;
import java.util.Scanner;

public class NarrowConversational {

    public static void main(String[] args) {
        HashSet<String> old_questions = new HashSet();

        try {
            File myObj = new File("conversational_questions_large.csv");
            Scanner myReader = new Scanner(myObj);
            int i=0;
            while (myReader.hasNextLine()) {
                String question = myReader.nextLine();
                if(i%100==0) {
                    old_questions.add(question);
                }
                i++;
            }
            myReader.close();
        }catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        try {
            FileWriter myWriter = new FileWriter("conversational_questions.csv", false);
            for(String question : old_questions) {
                myWriter.write(question+"\n");
            }
            myWriter.close();
        } catch (IOException e) {
            System.out.println("An error occurred writing the file.");
            e.printStackTrace();
        }





        System.out.println("Successfully wrote to the file.");
    }

}
