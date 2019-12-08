package com.example.afinal;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class DeleteLocations extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_delete_locations);
        this.showList();
    }

    // showList() appends savedLocationsText2 (ID) text view
    public void showList() {
        TextView savedLoc = findViewById(R.id.savedLocationsText2);

        for (int i = 0; i < MyList.totalDetails.size(); i++) {
            savedLoc.append(i + " : " + MyList.totalDetails.get(i));
            savedLoc.append(System.getProperty("line.separator"));
            savedLoc.append(System.getProperty("line.separator"));
        }

    }

    // deleteItem() deletes an item in the MyList.totalDetails list
    public void deleteItem(View view) {
        try {
            EditText enteredInt = findViewById(R.id.editText);
            String content = enteredInt.getText().toString();
            int index = Integer.parseInt(enteredInt.getText().toString());

            if (content.isEmpty() == true || content.length() <= 0)  {
                this.moveNext();
            } else {
                MyList.removeListDetails(index);
                this.moveNext();
            }
        } catch (Exception e) {
            Toast.makeText(
                    this,
                    "Please type in the correct item index (1 character allowed) that you'd like to delete.",
                    Toast.LENGTH_SHORT);
            this.moveNext();
        }
    }

    // just refreshes this activity to view
    // the new list after deletion
    public void moveNext() {
        finish();
        startActivity(getIntent());
    }
}
