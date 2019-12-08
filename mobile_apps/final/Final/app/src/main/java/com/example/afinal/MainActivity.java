package com.example.afinal;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;
import com.google.android.gms.location.FusedLocationProviderClient;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import java.io.IOException;
import java.util.List;
import java.util.Locale;

/*
This application requires Fine GPS Location Tracking to be turned on.
This application should ask the users for access to turn GPS tracking on.
Google Store also needs to be on the most recent update, otherwise, the
application may not work correctly.

If the address keeps returning null or blank, double check the emulator settings
-- check README for more details.
*/
public class MainActivity extends AppCompatActivity {
    // the object that'll allow us to receive coordinates
    private FusedLocationProviderClient fusedLocationProviderClient;

    // the list that we'll use to store and get location
    // information from the Geocoder object
    List<Address> address ;

    // the object that'll allow us to get information
    // based upon the coordinates we put in
    Geocoder geo;
    String addressLine = "";
    String locality = "";
    String state = "";
    String country = "";
    String addy = "";

    // setting the permissions return code
    // see AndroidManifesst.xml to see which
    // permissions are being used
    private final int permCode = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        this.requestPerm();
        geo = new Geocoder(this, Locale.getDefault());

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        fusedLocationProviderClient = LocationServices.getFusedLocationProviderClient(this);
        this.getLoc();
    }

    // requestPerm() to request location permissions
    public void requestPerm() {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION)
                != PackageManager.PERMISSION_GRANTED) {
            // access has been denied
            if (ActivityCompat.shouldShowRequestPermissionRationale(this, Manifest.permission.ACCESS_FINE_LOCATION)) {
                // if access has been denied, show rational
                Toast.makeText(this,
                        "Permission denied for location services. Location services are required to run this app correctly.",
                        Toast.LENGTH_SHORT);
                // request the permission
                ActivityCompat.requestPermissions(this,
                        // permCode == 1
                        new String[] {Manifest.permission.ACCESS_FINE_LOCATION},
                        permCode);
            } else {
                // no rational, request the permission
                ActivityCompat.requestPermissions(this,
                        // permCode == 1
                        new String[] {Manifest.permission.ACCESS_FINE_LOCATION},
                        permCode);
            }
        } else {
            // permission granted
        }
    }

    // onRequestPermissionsResult() should be invoked
    // automatically after running the requestPerm()
    @Override
    public void onRequestPermissionsResult(int requestCode,
                                           String[] permissions,
                                           int[] grantResults) {
        switch(requestCode) {
            case permCode:
                if (grantResults.length > 0 &&
                        grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                    // when access is granted, call getLoc() method
                    this.getLoc();
                } else {
                    // when access is denied, call requestPerm() again
                    // in order to continue to the app
                    Toast.makeText(this, "Location permissions as been denied, please accept turn on permissions to use the app.", Toast.LENGTH_SHORT);
                    this.requestPerm();
                }
        }
    }

    // getLoc() gets the location coordinates
    // then puts in those coordinates into Geocoder
    // to receive detailed information
    public void getLoc() {
        fusedLocationProviderClient.getLastLocation()
                .addOnSuccessListener(this, new OnSuccessListener<Location>() {
                    @Override
                    public void onSuccess(Location location) {
                        if (location != null) {
                            System.out.println("ENTERING TRY");
                            try {
                                double latitude = location.getLatitude();
                                double longitude = location.getLongitude();
                                address = geo.getFromLocation(latitude, longitude, 1);
                                addressLine = address.get(0).getAddressLine(0);
                                locality = address.get(0).getLocality();
                                state = address.get(0).getAdminArea();
                                country = address.get(0).getCountryCode();
                                addy = addressLine;
                                MyList.setCurrentLocation(addy);
                            } catch (IOException e) {
                                MyList.setCurrentLocation(e.toString());
                            }
                        } else if (location == null){
                            // set to "NULL" just for debugging purposes
                            addy = "NULL";
                            MyList.setCurrentLocation(addy);
                        }
                    }
                }).addOnFailureListener(this, new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                    // sets currentLocation in MyList class
                    // to "FAILED" for debugging purposes
                    // see MyList class for more details
                    MyList.setCurrentLocation("FAILED");
                }});
    }

    // moveNext() just moves to next activity
    public void moveNext(View view) {
        Intent intent = new Intent(MainActivity.this, WhereAreYou.class);
        startActivity(intent);
    }
}
