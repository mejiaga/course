# Stock Time Series

In this activity, we use a [Quandl api](https://www.quandl.com/) to fetch stock data and then build a time-series financial plot for the closing stock prices.

## Instructions

* Use the starter code provided and complete the function `buildPlots`

* Use `Plotly.d3.json` to fetch data from the Quandl api. Note that you will need to register for a free api key and then add that key to your url.

```javascript
var api_key = YOUR_API_KEY
var url = `https://www.quandl.com/api/v3/datasets/WIKI/AMZN.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${api_key}`
```

* Use the `unpack` helper function to select the data that you need from the json response object. See the comments for additional documentation.

* Use the code examples from the plotly.js documentation to build your basic time series plot

## Bonus

* Add a [Range Slider](https://plot.ly/python/range-slider/) to the time series plot to dynamically select the view range.

- - -

### Copyright

Copyright Trilogy Education Services © 2017. All Rights Reserved.
