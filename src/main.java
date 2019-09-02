import com.github.sarxos.webcam.Webcam;

public class main {
    public static void main(String[] args) {
        System.out.println(Webcam.getWebcams());

        GUI gui = new GUI();
        gui.show();
//        try {
//            gui.runDemo();
//        } catch (InterruptedException e) {
//            e.printStackTrace();
//        }
        //gui.runDemo();
        //System.out.println(gui.run());
    }
}
