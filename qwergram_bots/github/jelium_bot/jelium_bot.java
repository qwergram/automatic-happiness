/**
 * This as a hello world app learned from https://docs.oracle.com/javase/tutorial/getStarted/cupojava/unix.html
**/

import java.net.HttpUrlConnection;

public class JeliumBot {

  enum Mode{ WAIT, SCRAPE, REPORT }
  Mode mode;

  public static void main(String[] args) {
    System.out.println("Hello World!"); // Print out a string
  }
}
