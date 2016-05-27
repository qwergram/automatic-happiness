/**
 * This as a hello world app learned from https://docs.oracle.com/javase/tutorial/getStarted/cupojava/unix.html
 * with help from http://interactivepython.org/courselib/static/java4python/Java4Python.html
 * and http://stackoverflow.com/questions/1359689/how-to-send-http-request-in-java
**/

import java.net.*;
import java.io.*;

public class JeliumBot {
  public static void main(String[] args) throws Exception {
    URL github = new URL("http://www.github.com");
    URLConnection github_connection = github.openConnection();
    BufferedReader github_in = new BuffereredReader(
      new InputStreamReader(
        github_connection.getInputStream()
      )
    );
    String inputLine;
    while ((inputLine = github_in.readLine()) != null)
      System.out.println(inputLine);
    github_in.close();
  }
}

class main {
  public static void main(String[] args) {
    JeliumBot jbot = new JeliumBot();
    JeliumBot.main(new String[]);
  }
}
