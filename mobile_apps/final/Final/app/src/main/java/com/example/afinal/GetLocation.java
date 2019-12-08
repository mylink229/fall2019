package com.example.afinal;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class GetLocation extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_get_location);
        this.setDisplayLocationText(MyList.currentLocation);
    }

    // setDisplayLocationText() sets displayLocationText(ID) text view
    public void setDisplayLocationText(String location) {
        TextView field = findViewById(R.id.displayLocationText);
        field.setText(location);
    }

    // built in methods from the MyList class
    // that  adds items to the separate lists
    // stored in MyList
    // see MyList class for more details
    public void addToMyLists() {
        MyList.addToListPlace();
        MyList.addToListAddy();
    }

    // just moves to the next activity
    public void moveNext(View view) {
        this.addToMyLists();
        Intent intent = new Intent(this, SavedLocations.class);
        startActivity(intent);
    }
}
