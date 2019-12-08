package com.example.afinal;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MyList {

    // variable that holds the user input for
    // when asked "where are you"
    public static String currentPlace = "";

    // variable that holds address made from Geocoder
    public static String currentLocation = "";

    // these are hardcoded just for examples
    public static List<String> listPlace = new ArrayList<>(Arrays.asList(
            "High School",
            "Mom's house",
            "UWGB"));

    // these are hardcoded just for examples
    public static List<String> listAddy = new ArrayList<>(Arrays.asList(
            "2222 Deckner Ave., Green Bay, WI 54302, USA",
            "1801 Libal Rd., Appleton, WI 55301, USA",
            "2420 Nicolet Dr., Green Bay, WI 54311, USA"));

    // this is the list that's most important
    // listPlace.get(INDEX) + listAddy.get(INDEX) = totalDetails.get(INDEX)
    public static List<String> totalDetails = new ArrayList<>();

    // setters, getters, basic add to list methods
    public static void setCurrentLocation (String loc) {
        currentLocation = loc;
    }

    public static void setCurrentPlace (String place) {
        currentPlace = place;
    }

    public static void addToListPlace() {
        listPlace.add(currentPlace);
    }

    public static void addToListAddy() {
        listAddy.add(currentLocation);
    }

    public static void addToListDetails(String details) {
        totalDetails.add(details);
    }

    public static void removeListDetails(int index) {
        totalDetails.remove(index);
    }
}
