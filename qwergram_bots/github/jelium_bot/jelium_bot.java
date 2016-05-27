/**
 * This as a hello world app learned from https://docs.oracle.com/javase/tutorial/getStarted/cupojava/unix.html
**/

class JeliumBot {

  enum Mode{ WAIT, SCRAPE, REPORT }
  Mode mode;

  public static void main(String[] args) {
    System.out.println("Hello World!"); // Print out a string
  }
}


public class FreshJuiceTest {
  public static void main(String[] args) {
    JeliumBot jbot = new JeliumBot();
    jbot.mode = JeliumBot.Mode.WAIT;
    System.out.println("Mode: " + jbot.mode);
  }
}
