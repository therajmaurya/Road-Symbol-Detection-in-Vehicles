package com.logicturtle.geo_location;

import android.location.Location;

public class LocationModel {

    public String geoKey;

    public double latitude;

    public double longitude;

    public String symbolType;


    public LocationModel() {
    }

    public LocationModel(String geoKey, double latitude, double longitude, String symbolType) {
        this.geoKey = geoKey;
        this.latitude = latitude;
        this.longitude = longitude;
        this.symbolType = symbolType;
    }


    public String getGeoKey() {
        return geoKey;
    }

    public double getLatitude() {
        return latitude;
    }

    public double getLongitude() {
        return longitude;
    }

    public String getSymbolType() {
        return symbolType;
    }
}
