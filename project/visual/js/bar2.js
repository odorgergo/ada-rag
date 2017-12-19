v = tweet_per_lang[YEAR][MONTH]
sum = Object.values(v).reduce((a, b) => a + b, 0);
// DATA=Object.values(v)
langs = ["fr", "en", "de", "it"];
data = langs.map(l => ({id: l, label: l, value: v[l]*100/sum}))
var margin = {top:10, right:10, bottom:90, left:10};

var width = 960 - margin.left - margin.right;

var height = 500 - margin.top - margin.bottom;

var xScale = d3.scaleOrdinal().rangeRoundBands([0, width], .03)

var yScale = d3.scale.linear()
      .range([height, 0]);


var xAxis = d3.svg.axis()
		.scale(xScale)
		.orient("bottom");


var yAxis = d3.svg.axis()
		.scale(yScale)
		.orient("left");

var svgContainer = d3.select("#bar").append("svg")
		.attr("width", width+margin.left + margin.right)
		.attr("height",height+margin.top + margin.bottom)
		.append("g").attr("class", "container")
		.attr("transform", "translate("+ margin.left +","+ margin.top +")");

xScale.domain(data.map(function(d) { return d.food; }));
yScale.domain([0, d3.max(data, function(d) { return d.quantity; })]);


//xAxis. To put on the top, swap "(height)" with "-5" in the translate() statement. Then you'll have to change the margins above and the x,y attributes in the svgContainer.select('.x.axis') statement inside resize() below.
var xAxis_g = svgContainer.append("g")
		.attr("class", "x axis")
		.attr("transform", "translate(0," + (height) + ")")
		.call(xAxis)
		.selectAll("text");

// Uncomment this block if you want the y axis
var yAxis_g = svgContainer.append("g")
		.attr("class", "y axis")
		.call(yAxis)
		.append("text")
		.attr("transform", "rotate(-90)")
		.attr("y", 6).attr("dy", ".71em")
		//.style("text-anchor", "end").text("Number of Applicatons");



	svgContainer.selectAll(".bar")
  		.data(data)
  		.enter()
  		.append("rect")
  		.attr("class", "bar")
  		.attr("x", function(d) { return xScale(d.id); })
  		.attr("width", xScale.rangeBand())
  		.attr("y", function(d) { return yScale(d.value); })
  		.attr("height", function(d) { return height - yScale(d.value); });
