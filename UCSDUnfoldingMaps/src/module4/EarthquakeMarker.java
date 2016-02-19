package module4;

import de.fhpotsdam.unfolding.data.PointFeature;
import de.fhpotsdam.unfolding.marker.SimplePointMarker;
import processing.core.PGraphics;

/** Implements a visual marker for earthquakes on an earthquake map
 * 
 * @author UC San Diego Intermediate Software Development MOOC team
 * @author Derek Cartwright Jr.
 *
 */
public abstract class EarthquakeMarker extends SimplePointMarker
{
	
	// Did the earthquake occur on land?  This will be set by the subclasses.
	// isOnLand variable is protected which will allow all files in the module
	// to gain access.
	protected boolean isOnLand;

	// The radius of the Earthquake marker
	// You will want to set this in the constructor, either
	// using the thresholds below, or a continuous function
	// based on magnitude. 
	protected float radius;
	
	
	/** Greater than or equal to this threshold is a moderate earthquake */
	public static final float THRESHOLD_MODERATE = 5;
	/** Greater than or equal to this threshold is a light earthquake */
	public static final float THRESHOLD_LIGHT = 4;

	/** Greater than or equal to this threshold is an intermediate depth */
	public static final float THRESHOLD_INTERMEDIATE = 70;
	/** Greater than or equal to this threshold is a deep depth */
	public static final float THRESHOLD_DEEP = 300;

	// ADD constants for colors

	
	// abstract method implemented in derived classes
	public abstract void drawEarthquake(PGraphics pg, float x, float y);
		
	
	// Constructor that makes a call to the super constructor from the SimplePointMarker 
	// passing it the feature's location.
	public EarthquakeMarker (PointFeature feature) 
	{
		super(feature.getLocation());
		// Add a radius property and then set the properties
		java.util.HashMap<String, Object> properties = feature.getProperties();
		float magnitude = Float.parseFloat(properties.get("magnitude").toString());
		properties.put("radius", 2*magnitude );
		setProperties(properties);
		this.radius = 1.75f*getMagnitude();
	}
	

	// calls abstract method drawEarthquake and then checks age and draws X if needed
	public void draw(PGraphics pg, float x, float y) {
		// save previous styling
		pg.pushStyle();
			
		// determine color of marker from depth
		colorDetermine(pg);
		
		// call abstract method implemented in child class to draw marker shape
		drawEarthquake(pg, x, y);
		
		// OPTIONAL TODO: draw X over marker if within past day		
		
		// reset to previous styling
		pg.popStyle();
		
	}
	
	// determine color of marker from depth
	// We suggest: Deep = red, intermediate = blue, shallow = yellow
	// But this is up to you, of course.
	// You might find the getters below helpful.
	private void colorDetermine(PGraphics pg) {
		//TODO: Implement this method
		
		if(this.getDepth() <= 70){
			pg.fill(255, 255, 0);
		} 
		else if(this.getDepth() <= 300 && this.getDepth() >= 70){
			pg.fill(0, 0, 255);
		} 
		else{
			pg.fill(255, 0, 0);
		}		
	}
	
	
	/*
	 * getters for earthquake properties
	 */
	
	// getMagnitude: returns the magnitude of the earthquake marker
	public float getMagnitude() {
		return Float.parseFloat(getProperty("magnitude").toString());
	}
	
	// getDepth: returns the depth of the earthquake
	public float getDepth() {
		return Float.parseFloat(getProperty("depth").toString());	
	}
	
	// getTitle: returns the title of the earthquake
	public String getTitle() {
		return (String) getProperty("title");	
		
	}
	
	// getRadius: returns the radius of the earthquake
	public float getRadius() {
		return Float.parseFloat(getProperty("radius").toString());
	}
	
	// isOnLand: indicates whether or not the earthquake took place on land or sea
	public boolean isOnLand()
	{
		return isOnLand;
	}
	
	
}
