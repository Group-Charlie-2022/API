import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Base {

    public static void main(String[] args) {
        String data = "";
        try {
            File myObj = new File("data.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                data = myReader.nextLine();
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        try {
            FileWriter myWriter = new FileWriter("questions3.csv");
            myWriter.write("text,label\n");

            for(int i = 12; i <= data.length(); i++){
                String window = data.substring(i-12, i);
                if(window.equals("\"question\": ")) {
                    int end = data.substring(i).indexOf("\", \"id\":");
                    String question = data.substring(i, i+end+1);
                    i = i+end+5;
                    System.out.println(question);
                    myWriter.write(question+",conversational\n");
                }

            }

            myWriter.close();
        } catch (IOException e) {
            System.out.println("An error occurred writing the file.");
            e.printStackTrace();
        }


        System.out.println("Successfully wrote to the file.");



    }

}
