package myPackage;

import java.text.DecimalFormat;

import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;
import javafx.scene.control.TextField;

public class Controller {
    @FXML
    private Label taxPercentageLabel;

    @FXML
    private Label taxLabel;
    
    @FXML
    private Label tipPercentageLabel;

    @FXML
    private TextField amountTextField;

    @FXML
    private TextField tipTextField;
    
    @FXML
    private TextField totalTextField;
    
    @FXML
    private TextField taxTextField;
   
    @FXML
    private Slider tipPercentageSlider;
    
    @FXML
    private Slider taxSlider;

    @FXML
    private Label baseAmountLabel;

    @FXML
    private TextField baseAmountValue;
     
    @FXML
    void calculateButtonPressed(ActionEvent event) {
    	this.calculate();
    	
    }
    
    private static DecimalFormat df2 = new DecimalFormat("#.##");
    
    private double amount;
    private double total;
    private double taxValue;    
    private double tipValue;
    private double taxPercent; 
    private double tipPercent; 
    
    
    private void calculateBeforeTip() {
    	int base = Integer.parseInt(baseAmountValue.getText());    	
    	this.taxValue = (this.amount * taxSlider.getValue()) / 100;
    	this.taxTextField.setText(df2.format(taxValue));
    	
    	this.amount = base + (base * taxValue);    	
    	this.amountTextField.setText(df2.format(this.amount));     	
    }
    
    private void calculate() {
    	this.calculateBeforeTip();    	
    	this.tipValue = (this.amount * tipPercentageSlider.getValue()) / 100;
    	this.tipTextField.setText(df2.format(tipValue));
    	
    	this.total = this.amount + tipValue;
    	this.totalTextField.setText(df2.format(this.total)); 
    	System.out.println(this.total);
    	System.out.println(this.amount);
    } 
    
    // called by FXMLLoader to initialize the controller
    public void initialize() {
       taxSlider.valueProperty().addListener(
          new ChangeListener<Number>() {
             @Override
             public void changed(ObservableValue<? extends Number> ov, 
                Number oldValue, Number newValue) {
            	 taxPercent = (float) taxSlider.getValue();
            	 taxPercentageLabel.setText(df2.format(taxPercent));
             }
          }
       );
       
       tipPercentageSlider.valueProperty().addListener(
          new ChangeListener<Number>() {
             @Override
             public void changed(ObservableValue<? extends Number> ov, 
                Number oldValue, Number newValue) {
            	 tipPercent = (float) tipPercentageSlider.getValue();
            	 tipPercentageLabel.setText(df2.format(tipPercent));
             }
          }
       );
    } 
}
