// Slider START
var num_month = 12;
var month_data = d3.range(0, num_month).map(function (d) { return new Date(2016, 0 + d, 1); });
var slider = d3.sliderHorizontal()
  .min(d3.min(month_data))
  .max(d3.max(month_data))
  .step(1000 * 60 * 60 * 24 * 31)
  .width(1000)
  .tickFormat(d3.timeFormat('%B'))
  .tickValues(month_data)
  .on('onchange', val => {

    MONTH  = d3.timeFormat('%m')(val);
    d3.select("#value").text(d3.timeFormat('%B')(val)+' '+YEAR);
    console.log(MONTH)

    // removeOptions(select)
    // clear_description()
    // removeSuperEdge(E)
    // removeMarkers(E)
    // E = null;
    geojson.setStyle(style);

    // removeNewsLayer()
    // drawNewsDots()

  });



var g = d3.select("div#slider").append("svg")
  .attr("width", 1100)
  .attr("height", 100)
  .append("g")
  .attr("transform", "translate(30,30)");

g.call(slider);
starting_value = new Date(2016, 1, 1);
slider.value(starting_value);
// d3.select("a#setValue2").on("click", () => slider.value(new_value));



// // Slide slider according to clicked object
// function sliderSlider (e) {
//
//   try {
//     year = parseInt(e.originalTarget.attributes.value.value);
//     new_value = new Date(year, 10, 10);
//     slider.value(new_value);
//   } catch (err) {
//   year = parseInt(e.srcElement.getAttribute("value"));
//   new_value = new Date(year, 10, 10);
//   slider.value(new_value);
//
//   };
// }
//
// d3.select("#value").text(d3.timeFormat('%Y')(slider.value()));
// // Slider END
//
// // Ignore this
function popup_function() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
}
