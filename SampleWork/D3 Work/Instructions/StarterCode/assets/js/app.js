// @TODO: YOUR CODE HERE!

// set up the svg
var svgWidth = 960;
var svgHeight = 500;
var margin = {top: 20, right: 40, bottom: 60, left:100};
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create wrapper
var svg = d3
    .select('#scatter')
    .append('svg')
    .attr('width', svgWidth)
    .attr('height', svgHeight)

var chartGroup = svg.append('g')
    .attr('transform', `translate(${margin.left}, ${margin.top})`)

// import data
d3.csv('./assets/data/data.csv').then(function(healthData) {
    console.log(healthData)

    //cast data as numbers
    healthData.forEach(function(data) {
        data.age = +data.age;
        data.healthcare = +data.healthcare;
        data.income = +data.income;
        data.obesity = +data.obesity;
        data.poverty = +data.poverty;
        data.smokes = +data.smokes;
    })

    // scale functions
    var xLinearScale = d3.scaleLinear()
        .domain(d3.extent(healthData, d => d.poverty))
        .range([0, width])

    var yLinearScale = d3.scaleLinear()
        .domain(d3.extent(healthData, d => d.obesity))
        .range([height, 0]);

// create axes

    var xaxis = d3.axisBottom(xLinearScale);
    var yaxis = d3.axisLeft(yLinearScale);

    chartGroup.append('g')
        .attr('transform', `translate(0, ${height})`)
        .call(xaxis)

    chartGroup.append('g')
        .call(yaxis)

        // create axis labels
    chartGroup.append('text')
        .attr('transform', `translate(${width/3}, ${height +30})`)
        .text("In Poverty (%)")

    chartGroup.append('text')
        .attr('transform', 'rotate(-90)')
        .attr("y", 0 - margin.left*.8)
        .attr("x", 0 - (height / 2))
        .text("Obesity (%)")


        // create scatterplot
        chartGroup.selectAll('circle')
            .data(healthData)
            .enter()
            .append('circle')
            .attr("cx", function(data, index) {
                return xLinearScale(data.poverty)
            })
            .attr("cy", function(data, index) {
                return yLinearScale(data.obesity)
            })
            .attr('r', '10')
            .attr('fill', 'blue');
    
})