package module4;

import de.fhpotsdam.unfolding.data.PointFeature;
import processing.core.PGraphics;
import java.lang.Math;

/** Implements a visual marker for ocean earthquakes on an earthquake map
 * 
 * @author UC San Diego Intermediate Software Development MOOC team
 * @author Your name here
 *
 */
public class OceanQuakeMarker extends EarthquakeMarker {
	
	public OceanQuakeMarker(PointFeature quake) {
		super(quake);
		
		// setting field in earthquake marker
		isOnLand = false;
	}
	

	@Override
	public void drawEarthquake(PGraphics pg, float x, float y) {
		// Drawing a centered square for Ocean earthquakes
		// DO NOT set the fill color.  That will be set in the EarthquakeMarker
		// class to indicate the depth of the earthquake.
		// Simply draw a centered square.
		
		// HINT: Notice the radius variable in the EarthquakeMarker class
		// and how it is set in the EarthquakeMarker constructor
		
		// TODO: Implement this method
		float diam = radius*2;
		float side = (float) (diam/(Math.sqrt(2)));
		float x_buff = x/side;
		float y_buff = y/side;
		pg.rect(x-x_buff, y-y_buff, side, side);
	}
	


	

}
