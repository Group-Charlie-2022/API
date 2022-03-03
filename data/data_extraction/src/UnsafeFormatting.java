import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class UnsafeFormatting {

    public static void main(String[] args) {
        try {
            File myObj = new File("unsafe_questions.txt");
            Scanner myReader = new Scanner(myObj);
            try {
                FileWriter myWriter = new FileWriter("unsafe_questions.csv", true);

                while (myReader.hasNextLine()) {
                    String question = myReader.nextLine();
                    System.out.println(question);
                    myWriter.write("\"" + question + "\",unsafe\n");
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
