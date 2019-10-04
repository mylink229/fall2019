package BasicCalculator;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.application.Application;

public class Main extends Application{
	@Override
	public void start(Stage stage) throws Exception {	
		Parent root = 
				FXMLLoader.load(getClass().getResource("lab.fxml"));

		Scene scene = new Scene(root); // attach scene graph to scene
		stage.setTitle("Tip Calculator"); // displayed in window's title bar
		stage.setScene(scene); // attach scene to stage
		stage.show(); // display the stage
	}
	
	public static void main(String[] args) { 
      launch(args); 
	}
}
