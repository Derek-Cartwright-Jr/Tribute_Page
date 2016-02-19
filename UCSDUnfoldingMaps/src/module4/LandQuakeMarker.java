package module4;

import de.fhpotsdam.unfolding.data.PointFeature;
import processing.core.PGraphics;

/** Implements a visual marker for land earthquakes on an earthquake map
 * 
 * @author UC San Diego Intermediate Software Development MOOC team
 * @author Derek Cartwright Jr.
 *
 */
public class LandQuakeMarker extends EarthquakeMarker {
	
	// LandQuakeMarker constructor that accepts the "PointFeature" object quake
	// that makes a call to the EarthQuakeMarker super class and sets isOnLand
	// variable equal to true.
	public LandQuakeMarker(PointFeature quake) {
		
		// calling EarthquakeMarker constructor
		super(quake);
		
		// setting field in earthquake marker
		isOnLand = true;
	}


	@Override
	// Override the drawEarthquake method from the EarthQuakeMarker class
	public void drawEarthquake(PGraphics pg, float x, float y) {
		// Draw a centered circle for land quakes
		// DO NOT set the fill color here.  That will be set in the EarthquakeMarker
		// class to indicate the depth of the earthquake.
		// Simply draw a centered circle.
		
		// HINT: Notice the radius variable in the EarthquakeMarker class
		// and how it is set in the EarthquakeMarker constructor
		
		// TODO: Implement this method
		pg.ellipse(x, y, radius*2, radius*2);
		
	}
	

	// Get the country the earthquake is in
	public String getCountry() {
		return (String) getProperty("country");
	}



		
}