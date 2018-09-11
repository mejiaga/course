# Turbo CARTO CSS

In this activity we will utilize Turbo CARTO, CARTO's CSS preprocessor in order to style certain markers according to values they represent.

## Instructions

1. Using the McDonald's map created in the previous activity, style the markers in the following ways using CSS:

   1. Hide any markers for McDonald's without a drive-thru.

   2. Apply the following colors to the specified states:

      1. PA: `#388e3c`
      2. FL: `#18ffff`
      3. AZ: `#ff6e40`
      4. LA: `#ef6c00`
      5. CA: `#7e57c2`
      6. CO: `#ffc107`
      7. TX: `#00897b`
      8. All Other States: `#90a4ae`

2. Add a `#e82a37` border to markers representing any McDonald's locations without WiFi.

3. Lastly, make it so that none of the markers overlap with each other.

## Bonus

1. For coloring the states, use a [ramp function](https://github.com/CartoDB/turbo-carto#turbo-carto-ramps).

2. For markers representing a McDonald's with a play place, double the size of the marker, and change the marker's border color to `#3c74f7`.

## Hints

* In order to color the markers in relation to the data they represent, you will need to explore the [Turbo CARTO CSS Docs](https://github.com/CartoDB/turbo-carto).

* Make sure to go back and forth between the map view and the data view to make sure you're styling the correct column names.

* If you forget what any of the marker CSS properties do, visit [CARTO's marker documentation](https://carto.com/docs/carto-engine/cartocss/properties#markers).
