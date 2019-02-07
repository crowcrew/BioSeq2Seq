function formatOneAlignment(oneAlignment) {
  var sequenceTable = "<table class='oneAlignmentTable'><tr>";
  var sequence0 = "<tr style=''>";
  var sequence1 = "<tr style='display: inline-block;'>";
  var pairColors = ["color: #000000;", "color: #000000;"];

  for (var i = 0; i < oneAlignment.length; i++) {
    if (oneAlignment[i][0] == oneAlignment[i][1]) {
      pairColors[0] = "color: #ff00ff;";
      pairColors[1] = "color: #ff00ff;";
    } else {
      pairColors[0] = "color: #000000;";
      pairColors[1] = "color: #000000;";
    }
    sequence0 +=
      "<td " +
      "class='oneAlignmentTd'>" +
      "<p style='margin-top:10px; margin-bottom:0px; padding:0px; " +
      pairColors[0] +
      "'>" +
      oneAlignment[i][0] +
      "</p>" +
      "<p style='margin:0px; padding:0px; " +
      pairColors[1] +
      "'>" +
      oneAlignment[i][1] +
      "</p>" +
      "</td>";
  }
  sequence0 += "</tr>";
  sequence1 += "</tr>";
  sequenceTable = sequenceTable + sequence0 + sequence1;
  sequenceTable += "</table>";
  return sequenceTable;
}

function render(AllAlignments, sequenceNames, userFile) {
  var width = (99 * window.innerWidth) / 100,
    height = (90 * window.innerHeight) / 100;

  var div = d3
    .select("body")
    .append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

  var svg = d3
    .select("body")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

  var color = d3.scaleOrdinal(d3.schemeCategory20);

  var simulation = d3
    .forceSimulation()
    .force(
      "link",
      d3
        .forceLink()
        .id(function(d) {
          return d.id;
        })
        .distance(width / 6)
        .strength(2)
    )
    .force("charge", d3.forceManyBody(-500))
    .force("center", d3.forceCenter(width / 2, height / 2));

  AllAlignments = JSON.parse(AllAlignments.replace(/&quot;/g, '"'));
  sequenceNames = JSON.parse(sequenceNames.replace(/&quot;/g, '"'));

  var nodes = [];
  var links = [];

  nodes.push({
    id: 0,
    name: "user-sequence",
    data: userFile
  });

  var nodeCounter = 0;

  for (var i = 0; i < AllAlignments.length; i++) {
    for (var j = 0; j < AllAlignments[i].length; j++) {
      nodes.push({
        id: ++nodeCounter,
        name: sequenceNames[i].split("/").pop(),
        data: formatOneAlignment(AllAlignments[i][j])
      });
      links.push({
        source: 0,
        target: nodeCounter
      });
    }
  }

  var localGraph = {
    nodes: nodes,
    links: links
  };

  var link = svg
    .append("g")
    .attr("class", "links")
    .selectAll("line")
    .data(localGraph.links)
    .enter()
    .append("line");

  var node = svg
    .append("g")
    .attr("class", "nodes")
    .selectAll("circle")
    .data(localGraph.nodes)
    .enter()
    .append("circle")
    .attr("r", 10)
    .attr("fill", function(d) {
      if(d.name==="user-sequence")
      return "#ff00ff";
      else 
      return "#fdb81e";
    })
    .call(
      d3
        .drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended)
    )
    .on("mouseover", function(d) {
      div
        .transition()
        .duration(200)
        .style("opacity", 0.9);
      div
        .html(d.name + "<br/>" + d.data)
        .style("left", d3.event.pageX + "px")
        .style("top", d3.event.pageY - 28 + "px")
        .style("height", -d3.event.pageX + "px")
        .style("width", -d3.event.pageY + "px");
    })
    .on("mouseout", function(d) {
      div
        .transition()
        .duration(500)
        .style("opacity", 0);
    });


  simulation.nodes(localGraph.nodes).on("tick", ticked);

  simulation.force("link").links(localGraph.links);

  function ticked() {
    link
      .attr("x1", function(d) {
        return d.source.x;
      })
      .attr("y1", function(d) {
        return d.source.y;
      })
      .attr("x2", function(d) {
        return d.target.x;
      })
      .attr("y2", function(d) {
        return d.target.y;
      });

    node
      .attr("cx", function(d) {
        return d.x;
      })
      .attr("cy", function(d) {
        return d.y;
      });
  }

  function dragstarted(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  }

  function dragged(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
  }

  function dragended(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  }
}
