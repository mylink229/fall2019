package BasicCalculator;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;

public class Controller {
    @FXML
    private Button addBtn;

    @FXML
    private Button subtractBtn;

    @FXML
    private Button multiplyBtn;

    @FXML
    private Button divideBtn;

    @FXML
    private Label num1;

    @FXML
    private Label num2;

    @FXML
    private TextField num1Text;

    @FXML
    private TextField num2Text;

    @FXML
    private Label result;

    @FXML
    private TextArea resultText;

    @FXML
    void addBtnPress(MouseEvent event) {
    	int x = 0;
    	int y = 0;
    	x = Integer.parseInt(num1Text.getText());
    	y = Integer.parseInt(num2Text.getText());
    	int k = x + y;
    	resultText.setText(Integer.toString(k));
    }

    @FXML
    void divideBtnPress(MouseEvent event) {
    	int x = 0;
    	int y = 0;
    	x = Integer.parseInt(num1Text.getText());
    	y = Integer.parseInt(num2Text.getText());
    	int k = x / y;
    	resultText.setText(Integer.toString(k));
    }

    @FXML
    void multiplyBtnPress(MouseEvent event) {
    	int x = 0;
    	int y = 0;
    	x = Integer.parseInt(num1Text.getText());
    	y = Integer.parseInt(num2Text.getText());
    	int k = x * y;
    	resultText.setText(Integer.toString(k));
    }

    @FXML
    void subtractBtnPress(MouseEvent event) {
    	int x = 0;
    	int y = 0;
    	x = Integer.parseInt(num1Text.getText());
    	y = Integer.parseInt(num2Text.getText());
    	int k = y - x;
    	resultText.setText(Integer.toString(k));
    }

}


