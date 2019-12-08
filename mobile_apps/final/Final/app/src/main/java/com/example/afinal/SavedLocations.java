package com.example.afinal;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class SavedLocations extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_saved_locations);
        this.setSavedLoc();
    }

    // setSavedLoc() appends the savedLocationsText (ID) text view
    // from the MyList.totalDetails list
    public void setSavedLoc() {
        TextView savedLoc = findViewById(R.id.savedLocationsText);

        // loops through two arrays-- for each element in each array,
        // concatenate to its counter part to create 1 new variable
        // then add that variable to MyList.totalDetails, then append
        // that 1 element to savedLocationsText (ID)
        for (int i = 0; i < MyList.listAddy.size(); i++) {
            String item = MyList.listPlace.get(i) + " -- " + MyList.listAddy.get(i);
            MyList.addToListDetails(item);
            savedLoc.append(i + " : " + item);
            savedLoc.append(System.getProperty("line.separator"));
            savedLoc.append(System.getProperty("line.separator"));
        }
    }

    // just moves to the next activity
    public void moveNext(View view) {
        Intent intent = new Intent(SavedLocations.this, DeleteLocations.class);
        startActivity(intent);
    }
}
