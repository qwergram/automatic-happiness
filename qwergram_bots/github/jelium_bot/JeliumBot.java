/**
 * This as a hello world app learned from https://docs.oracle.com/javase/tutorial/getStarted/cupojava/unix.html
 * with help from http://interactivepython.org/courselib/static/java4python/Java4Python.html
 * and http://stackoverflow.com/questions/1359689/how-to-send-http-request-in-java
**/

import java.net.*;
import java.io.*;
import java.util.Scanner;

public class JeliumBot {

  public static String use_helium() {
    try {

      Process p = Runtime.getRuntime().exec("cat compile_and_run.sh");
      BufferedReader stdInput = new BufferedReader(
      new InputStreamReader(p.getInputStream())
      );

      String feed = stdInput.readLine();
      while (feed != null) {
        System.out.println(feed);
        feed = stdInput.readLine();
      }

    } catch (IOException e){
      e.printStackTrace();
      System.exit(-1);
    }
    return "null";
  }

  public static void main(String[] args) throws Exception {
    JeliumBot.use_helium();
  }
}
