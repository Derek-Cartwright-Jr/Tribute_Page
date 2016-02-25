package module4;

import de.fhpotsdam.unfolding.data.Feature;
import de.fhpotsdam.unfolding.data.PointFeature;
import de.fhpotsdam.unfolding.geo.Location;
import de.fhpotsdam.unfolding.marker.SimplePointMarker;
import processing.core.PGraphics;

/** Implements a visual marker for cities on an earthquake map
 * 
 * @author UC San Diego Intermediate Software Development MOOC team
 * @author Derek Cartwright Jr.
 *
 */

// Class CityMarker inherits all the methods from the SimplePointMarker that I created in an earlier module
public class CityMarker extends SimplePointMarker {
	
	// The size of the triangle marker
	// It's a good idea to use this variable in your draw method
	public static final int TRI_SIZE = 5;  
	
	// CityMarker constructor will make a call to the parent class(SimplePointMarker) constructor
	// and give it the "Location" parameter location
	public CityMarker(Location location) {
		super(location);
	}
	
	// Overloaded CityMarker constructor method that accepts a "Feature" parameter city and makes 
	// a call to the parent class constructor(SimplePointMaker) giving it the city location and 
	// property parameters
	public CityMarker(Feature city) {
		super(((PointFeature)city).getLocation(), city.getProperties());
	}
	
	
	// HINT: pg is the graphics object on which you call the graphics
	// methods.  e.g. pg.fill(255, 0, 0) will set the color to red
	// x and y are the center of the object to draw. 
	// They will be used to calculate the coordinates to pass
	// into any shape drawing methods.  
	// e.g. pg.rect(x, y, 10, 10) will draw a 10x10 square
	// whose upper left corner is at position x, y
	/**
	 * Implementation of method to draw marker on the map.
	 */
	public void draw(PGraphics pg, float x, float y) {
		// Save previous drawing style
		pg.pushStyle();
		int tri = pg.color(255, 100, 100);
		// TODO: Add code to draw a triangle to represent the CityMarker
		pg.fill(tri);
		pg.triangle(x-7, y+7, x+7, y+7, x, y-7);
		// Restore previous drawing style
		pg.popStyle();
	}
	
	/* Local getters for some city properties.  You might not need these 
	 * in module 4. 	 */
	
	// getCity: returns the name of the city
	public String getCity()
	{
		return getStringProperty("name");
	}
	
	// getCountry: returns the country the city is in
	public String getCountry()
	{
		return getStringProperty("country");
	}
	
	// getPopulation: returns the population of the city
	public float getPopulation()
	{
		return Float.parseFloat(getStringProperty("population"));
	}
	
}
