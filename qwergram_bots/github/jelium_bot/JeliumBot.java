/**
 * This as a hello world app learned from https://docs.oracle.com/javase/tutorial/getStarted/cupojava/unix.html
 * with help from http://interactivepython.org/courselib/static/java4python/Java4Python.html
 * and http://stackoverflow.com/questions/1359689/how-to-send-http-request-in-java
**/

import java.net.*;
import java.io.*;
import java.util.Scanner;

public class JeliumBot {

  private static String api_endpoint = "https://api.github.com";
  private static String issues_endpoint = api_endpoint + "/repos/qwergram/automatic-happiness/issues/events";

  // This is how optional arguments happen in Java...
  public static String get_issues() { return JeliumBot.get_issues(-1); }
  public static String get_issues(int event_number) {
    String endpoint_target = JeliumBot.issues_endpoint;
    System.out.println(JeliumBot.issues_endpoint);
    if (event_number > 0) {
      endpoint_target = JeliumBot.issues_endpoint + '/' + String.valueOf(event_number);
    }
    String json_blob = JeliumBot.jelium_helper(endpoint_target);
    return json_blob;
  }

  public static String get_index() {
    return JeliumBot.jelium_helper(JeliumBot.api_endpoint);
  }

  private static String jelium_helper(String url) {
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
    // String json_blob = JeliumBot.get_index();
    String json_blob = JeliumBot.get_issues();
    // String json_blob = JeliumBot.get_issues(674983368);
    System.out.println(json_blob);
  }
}
