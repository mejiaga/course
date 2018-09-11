# Legend and Popups

In this activity, we will color markers by `storetype` using the GUI instead of CARTO CSS. We will add a legend and popups to our markers to display some information about each location when hovered over.

## Instructions

1. Create a brand new map using the McDonald's data

2. Open the SQL editor for the McDonald's data layer, and select only McDonald's locations whose `storetype` is not `freestanding`. This will select locations inside a Walmart, hospital, airport, in other words, stores which are not stand-alone. This is to reduce the density of our map.

3. Head over to the style tab for this layer, and choose the `fill` option. Select to fill each marker `by value`, and select `storetype`. **Use the GUI, not CARTO CSS, to do this.**

4. If done correctly, your map should have different colored points for each store type and a legend to indicate their meaning.

5. Look into adding a popup that will appear when you hover over a marker. In particular, we want to display the state, address, and phone number for each location.

## Hints

* If you're having trouble figuring out how to add popups, there's an informative GIF and article on the [Carto Blog](https://carto.com/blog/add-pop-ups-to.your-carto-builder-maps).
