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

class FreshJuiceTest {

  public static void main(String[] args) {
    JeliumBot jbot = new JeliumBot();
    jbot.mode = JeliumBot.Mode.WAIT;
    jbot.main(new String[0]);
    // Interesting, This is very different than python
    System.out.println("Mode: " + jbot.mode);
  }

}
