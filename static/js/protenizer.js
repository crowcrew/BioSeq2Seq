function formatProteinSequence(protein_sequence) {
  var sequenceTable = "<table class='oneAlignmentTable'><tr>";
  var sequence0 = "<tr style=''>";
  var sequence1 = "<tr style='display: inline-block;'>";
  var pairColors = ["color: #000000;", "color: #000000;"];

  for (var i = 0; i < protein_sequence.length; i++) {
    var color = "color: #ff00ff;";
    sequence0 +=
      "<td " +
      "class='oneAlignmentTd'>" +
      "<p style='margin-top:10px; margin-bottom:0px; padding:0px; " +
      color +
      "'>" +
      protein_sequence[i] +
      "</p>" +
      "</td>";
  }
  sequence0 += "</tr>";
  sequence1 += "</tr>";
  sequenceTable = sequenceTable + sequence0 + sequence1;
  sequenceTable += "</table>";
  return sequenceTable;
}

function render(protein_sequence, userFile) {
  var width = (99 * window.innerWidth) / 100,
      height = (90 * window.innerHeight) / 100;

  var div = d3
    .select("body")
    .append("div")
    .attr("class", "protein")
    .style("opacity", 0.9);

  var color = d3.scaleOrdinal(d3.schemeCategory20);
  console.log(protein_sequence);
  protein_sequence = formatProteinSequence(protein_sequence);


  div
    .html("<label style='text-align:center;'>" + userFile + "</label>" + "<br/>" + protein_sequence);



}
