/**
 * This as a hello world app learned from https://docs.oracle.com/javase/tutorial/getStarted/cupojava/unix.html
 * with help from http://interactivepython.org/courselib/static/java4python/Java4Python.html
 * and http://stackoverflow.com/questions/1359689/how-to-send-http-request-in-java
**/

import java.net.*;
import java.io.*;
import java.util.Scanner;

public class JeliumBot {

  public static String jelium_helper(String url) {
    String to_return = "";
    try {

      Process p = Runtime.getRuntime().exec("python3 jelium_bot_helper.py " + url);

      BufferedReader stdInput = new BufferedReader(
        new InputStreamReader(p.getInputStream())
      );

      BufferedReader stdError = new BufferedReader(
        new InputStreamReader(p.getErrorStream())
      );

      String feed = stdInput.readLine();
      while (feed != null) {
        to_return = to_return + feed;
        feed = stdInput.readLine();
      }

      if (to_return == "") {
        String error_feed = stdError.readLine();
        while (error_feed != null) {
          System.out.println(error_feed);
          error_feed = stdInput.readLine();
        }
      }

    } catch (IOException e){
      e.printStackTrace();
    }
    return to_return;
  }

  public static void main(String[] args) throws Exception {
    String json_blob = JeliumBot.jelium_helper("https://api.github.com");
    System.out.println(json_blob);
  }
}
