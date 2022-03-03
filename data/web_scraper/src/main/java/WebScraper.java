import com.gargoylesoftware.htmlunit.*;
import com.gargoylesoftware.htmlunit.html.*;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class WebScraper {

    public static void main(String[] args) {



        HashSet<String> questions = new HashSet<>();

        WebClient client = new WebClient();
        client.getOptions().setCssEnabled(false);
        client.getOptions().setJavaScriptEnabled(false);
        try {
            HtmlPage page = client.getPage("https://www.who.int/news-room/questions-and-answers");

            client.getCurrentWindow().getJobManager().removeAllJobs();
            client.close();





            String data = "";
            try {
                File myObj = new File("websites.txt");
                Scanner myReader = new Scanner(myObj);
                while (myReader.hasNextLine()) {
                    data = myReader.nextLine();
                }
                myReader.close();
            } catch (FileNotFoundException e) {
                System.out.println("An error occurred.");
                e.printStackTrace();
            }

            String url = "https://www.who.int/news-room/questions-and-answers/item/";

            HashMap<String, String> values = new HashMap();
            for(int i = 9; i <= data.length(); i++){
                String window = data.substring(i-9, i);
                if(window.equals("\"value\":\"")) {
                    int end = data.substring(i).indexOf("\"");
                    String value = data.substring(i, i+end);
                    String urlEnd = value.toLowerCase().replace(" ", "-");
                    String thisUrl = url + urlEnd;
                    values.put(value, thisUrl);
                    i = i+end+5;
                    if(value.contains("\\u0027s")){
                        values.remove(value);
                    }

                }
            }

            values.put("Women's health", url + "women's-health");
            values.put("Men's health", url + "men's-health");
            values.put("Children's environmental health", url + "women's-health");

            int i = 0;


            for(String value : values.keySet()){
                System.out.println();
                System.out.println(value+": "+values.get(value));
                WebClient newClient = new WebClient();
                newClient.getOptions().setCssEnabled(false);
                newClient.getOptions().setJavaScriptEnabled(false);
                try {
                    HtmlPage newPage = client.getPage(values.get(value));

                    DomElement div = newPage.getElementById("PageContent_C023_Col00");

                    String s = div.asXml();
                    String link = "https://www.who.int";
                    while(s.contains("href=\"/news-room/questions-and-answers/item/")){
                        s = s.substring(s.indexOf("href=\"/news-room/questions-and-answers/item/") + 6);
                        link = link + s.substring(0, s.indexOf("\""));
                        try{
                            newPage = client.getPage(link);
                        }catch(Exception e2){
                            e2.printStackTrace();
                        }
                    }
                    System.out.println(value+": "+link);

                    String text = newPage.asNormalizedText();
                    //System.out.println(text);

                    StringBuilder sb = new StringBuilder(text);
                    sb.reverse();
                    text = sb.toString();

                    while(text.contains("?")){
                        text = text.substring(text.indexOf("?"));
                        int end = text.length();
                        if (text.contains("\n")) {
                            end = text.indexOf("\n");
                        }
                        String question = text.substring(0, end);
                        StringBuilder sb2 = new StringBuilder(question);
                        sb2.reverse();
                        question = sb2.toString();
                        questions.add(question);
                        text = text.substring(end);
                    }




                    newClient.getCurrentWindow().getJobManager().removeAllJobs();
                    newClient.close();

                }catch(Exception e){
                    //writing problems to file
                    try {
                        FileWriter myWriter = new FileWriter("problems.txt", true);
                        myWriter.write(value+": "+values.get(value)+"\n");
                        myWriter.close();
                    } catch (IOException e1) {
                        System.out.println("An error occurred writing the file.");
                        e1.printStackTrace();
                    }
                    e.printStackTrace();
                }
            }


        }catch(Exception e){
            //exception for WHO webpage
            e.printStackTrace();
        }






        //writing to file
        if(true) {
            try {
                FileWriter myWriter = new FileWriter("questions4.csv", false);

                for (String question : questions) {
                    System.out.println(question);
                    myWriter.write("\"" + question + "\",medical\n");
                }
                myWriter.close();
            } catch (IOException e) {
                System.out.println("An error occurred writing the file.");
                e.printStackTrace();
            }
        }

    }

}
