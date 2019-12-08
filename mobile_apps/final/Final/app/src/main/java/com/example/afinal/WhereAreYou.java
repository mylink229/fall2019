package com.example.afinal;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class WhereAreYou extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_where_are_you);
    }

    // serCurrentPlace() sets the MyList.currentPlace
    // the value gathered from the locationText(ID) text field
    public void setCurrentPlace() {
        EditText field = findViewById(R.id.locationText);
        String content = field.getText().toString();

        if (content.isEmpty() == true || content == null) {
            content = "NO PLACE NAMED";
        } else {
            // do nothing
        }

        MyList.setCurrentPlace(content);
    }

    // just moves to the next activity
    public void moveNext(View view) {
        this.setCurrentPlace();
        Intent i = new Intent(WhereAreYou.this, GetLocation.class);
        startActivity(i);
    }
}
