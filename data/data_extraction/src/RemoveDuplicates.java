import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashSet;
import java.util.Scanner;

public class RemoveDuplicates {

    public static void main(String[] args) {

        HashSet<String> old_questions = new HashSet();
        HashSet<String> new_questions = new HashSet();

        try {
            File myObj = new File("medical_questions.csv");
            Scanner myReader = new Scanner(myObj);

            while (myReader.hasNextLine()) {
                old_questions.add(myReader.nextLine());
            }
            myReader.close();
        }catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        try {
            File myObj = new File("final_med_qs.txt");
            Scanner myReader = new Scanner(myObj);
            try {
                FileWriter myWriter = new FileWriter("medical_questions.csv", true);
                while (myReader.hasNextLine()) {
                    String question = "\"" + myReader.nextLine() + "\",medical\n";
                    if(!old_questions.contains(question)){
                        System.out.print(question);
                        myWriter.write(question);
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
