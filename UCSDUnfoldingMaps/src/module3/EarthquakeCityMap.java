package module3;

//Java utilities libraries
import java.util.ArrayList;
//import java.util.Collections;
//import java.util.Comparator;
import java.util.List;

//Processing library
import processing.core.PApplet;

//Unfolding libraries
import de.fhpotsdam.unfolding.UnfoldingMap;
import de.fhpotsdam.unfolding.marker.Marker;
import de.fhpotsdam.unfolding.data.MarkerFactory;
import de.fhpotsdam.unfolding.data.PointFeature;
import de.fhpotsdam.unfolding.marker.SimplePointMarker;
import de.fhpotsdam.unfolding.providers.Google;
import de.fhpotsdam.unfolding.providers.MBTilesMapProvider;
import de.fhpotsdam.unfolding.utils.MapUtils;

//Parsing library
import parsing.ParseFeed;

/** EarthquakeCityMap
 * An application with an interactive map displaying earthquake data.
 * Author: UC San Diego Intermediate Software Development MOOC team
 * @author Derek Cartwright Jr.
 * Date: July 17, 2015
 * */
public class EarthquakeCityMap extends PApplet {

	// You can ignore this.  It's to keep eclipse from generating a warning.
	private static final long serialVersionUID = 1L;

	// IF YOU ARE WORKING OFFLINE, change the value of this variable to true
	private static final boolean offline = false;
	
	// Less than this threshold is a light earthquake
	public static final float THRESHOLD_MODERATE = 5;
	// Less than this threshold is a minor earthquake
	public static final float THRESHOLD_LIGHT = 4;

	/** This is where to find the local tiles, for working without an Internet connection */
	public static String mbTilesString = "blankLight-1-3.mbtiles";
	
	// The map
	private UnfoldingMap map;
	
	//feed with magnitude 2.5+ Earthquakes
	// url variable that contains the earthquake data that's going to be used for the map
	private String earthquakesURL = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.atom";

	
	public void setup() {
		size(950, 600, OPENGL);
		
		// Only if I'm working offline
		if (offline) {
		    map = new UnfoldingMap(this, 200, 50, 700, 500, new MBTilesMapProvider(mbTilesString));
		    earthquakesURL = "2.5_week.atom"; 	// Same feed, saved Aug 7, 2015, for working offline
		}
		else {
			map = new UnfoldingMap(this, 200, 50, 700, 500, new Google.GoogleMapProvider());
			// IF YOU WANT TO TEST WITH A LOCAL FILE, uncomment the next line
			//earthquakesURL = "2.5_week.atom";
		}
		
	    map.zoomToLevel(2);
	    MapUtils.createDefaultEventDispatcher(this, map);	
			
	    // The List you will populate with new SimplePointMarkers
	    // This line creates a new arraylist object of "Marker" type
	    // that will be referred to by markers variable
	    List<Marker> markers = new ArrayList<Marker>();

	    // Use provided parser to collect properties for each earthquake
	    // PointFeatures have a getLocation method
	    // This line will create a new list of PointFeature type objects
	    // that will be referred to by earthquakes variable
	    List<PointFeature> earthquakes = ParseFeed.parseEarthquake(this, earthquakesURL);
	    
	    // These print statements show you (1) all of the relevant properties 
	    // in the features, and (2) how to get one property and use it
	    if (earthquakes.size() > 0) {
	    	PointFeature f = earthquakes.get(0);
	    	System.out.println(f.getProperties());
	    	Object magObj = f.getProperty("magnitude");
	    	float mag = Float.parseFloat(magObj.toString());
	    	// PointFeatures also have a getLocation method
	    }
	    	    
	    // for loop will create Markers and add them to the markers list object.
	    for(PointFeature feature : earthquakes){
	    	markers.add(createMarker(feature));
	    }
	    
	    // add marks to the map that show where these earthquakes are located
	    for(Marker mark : markers){
	    	map.addMarker(mark);
	    }
	    
	    
	    
	}
		
	// A suggested helper method that takes in an earthquake feature and 
	// returns a SimplePointMarker for that earthquake
	// TODO: Implement this method and call it from setUp, if it helps
	private SimplePointMarker createMarker(PointFeature feature)
	{
		int yellow = color(255, 255, 0);
	    int blue = color(0, 0, 255);
	    int red = color(255,0,0);
		// finish implementing and use this method, if it helps.
		SimplePointMarker m = new SimplePointMarker(feature.getLocation(), feature.getProperties());
		Object magObj = feature.getProperty("magnitude");
		float mag = Float.parseFloat(magObj.toString());
		if(mag < 4.0){
			m.setRadius(5);
			m.setColor(blue);
		}
		else if(mag > 4.0 && mag <= 4.9){
			m.setRadius(8);
			m.setColor(yellow);
		}
		else{
			m.setRadius(10);
			m.setColor(red);
		}
		return m;
	}
	
	public void draw() {
	    background(10);
	    map.draw();
	    addKey();
	    
	}


	// helper method to draw key in GUI
	// TODO: Implement this method to draw the key
	private void addKey() 
	{	
		// Remember you can use Processing's graphics methods here
		// fill method will fill in all subsequent visual objects with the given color parameter.
		fill(255, 250, 240);
		rect(25, 50, 150, 300);
		
		// Adding text to the key
		// fill method will fill in all subsequent visual objects with the given specific color parameter
		fill(0);
		// textAlign method will place the text according to the parameters that are given. E.g. Left Center
		// will horizontally place the text with respect to the left corner of the text and vertically in the center
		textAlign(LEFT, CENTER);
		textSize(12);
		text("Earthquake Key", 50, 60);
		
		// Create color integers that will be referred to by there color counterparts
		int red = color(255, 0, 0);
		int blue = color(0, 0, 255);
		int yellow = color(255, 255, 0);
		
		// fill method red for the circle
		fill(red);
		ellipse(50, 120, 20, 20);
		// fill method yellow for the circle
		fill(yellow);
		ellipse(50, 170, 16, 16);
		// fill method blue for the circle
		fill(blue);
		ellipse(50, 220, 10, 10);
		
		// fill in the text as black
		fill(0);
		// align the text left center
		textAlign(LEFT, CENTER);
		textSize(10);
		// 
		text("5.0+ Magnitude", 70, 120);
		text("4.0 - 4.9 Magnitude", 70, 170);
		text("Below 4.0", 70, 220);
		
	}
}
