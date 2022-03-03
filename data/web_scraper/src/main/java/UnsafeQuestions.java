import com.gargoylesoftware.htmlunit.WebClient;
import com.gargoylesoftware.htmlunit.html.DomElement;
import com.gargoylesoftware.htmlunit.html.HtmlPage;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

public class UnsafeQuestions {

    public static void main(String[] args) {



        HashSet<String> questions = new HashSet<>();

        WebClient client = new WebClient();
        client.getOptions().setCssEnabled(false);
        client.getOptions().setJavaScriptEnabled(false);
        try {
            HtmlPage page = client.getPage("https://www.mentalhealthforum.net/forum/forums/depression-forum.366/");

            client.getCurrentWindow().getJobManager().removeAllJobs();
            client.close();


            try {

                for(int i=1; i<50; i++) {
                    String xml = page.asXml();
                    if (xml.contains("<a href=\"/forum/forums/depression-forum")) {
                        String url = "https://www.mentalhealthforum.net/forum/forums/depression-forum.366/page-" + i;
                        try {
                            HtmlPage newPage = client.getPage(url);
                            System.out.println(url);

                            String newXml = newPage.asXml();
                            //System.out.println(newXml);
                            while(newXml.contains("<div class=\"structItem-title\">")){
                                newXml = newXml.substring(newXml.indexOf("<div class=\"structItem-title\">") + 31);
                                String question = newXml.substring(newXml.indexOf("\">") + 42, newXml.indexOf("</a>")-38);
                                System.out.println(question);
                                questions.add(question);
                                newXml = newXml.substring(newXml.indexOf("</a>") + 4);
                            }

                        }catch(Exception e){
                            e.printStackTrace();
                        }
                    }
                }


            }catch(Exception e){

                e.printStackTrace();
            }


        }catch(Exception e){
            //exception for WHO webpage
            e.printStackTrace();
        }






        //writing to file
        if(true) {
            try {
                FileWriter myWriter = new FileWriter("unsafe_questions.csv", false);

                for (String question : questions) {
                    System.out.println(question);
                    myWriter.write("\"" + question + "\",unsafe\n");
                }
                myWriter.close();
            } catch (IOException e) {
                System.out.println("An error occurred writing the file.");
                e.printStackTrace();
            }
        }

    }

}
