

var clustal = {}
clustal["A"] = "color: #80a0f0;"
clustal["R"] = "color: #f01505;"
clustal["N"] = "color: #00ff00;"
clustal["D"] = "color: #c048c0;"
clustal["C"] = "color: #f08080;"
clustal["Q"] = "color: #00ff00;"
clustal["E"] = "color: #c048c0;"
clustal["G"] = "color: #f09048;"
clustal["H"] = "color: #15a4a4;"
clustal["I"] = "color: #80a0f0;"
clustal["L"] = "color: #80a0f0;"
clustal["K"] = "color: #f01505;"
clustal["M"] = "color: #80a0f0;"
clustal["F"] = "color: #80a0f0;"
clustal["P"] = "color: #ffff00;"
clustal["S"] = "color: #00ff00;"
clustal["T"] = "color: #00ff00;"
clustal["W"] = "color: #80a0f0;"
clustal["Y"] = "color: #15a4a4;"
clustal["V"] = "color: #80a0f0;"

function printOneAlignment(oneAlignment, sequenceName, htmlElementID){
	var sequenceTable = "<label class='fileLabel'>"+ sequenceName + "</label><br>";
	var sequenceTable = sequenceTable + "<table class='oneAlignmentTable'><tr>";
	var sequence0 = "<tr style=''>";
	var sequence1 = "<tr style='display: inline-block;'>";	
	for(var i =0; i < oneAlignment.length; i++){
		sequence0+=("<td "+"class='oneAlignmentTd'>"+"<p style='margin-top:10px; margin-bottom:0px; padding:0px; "+clustal[oneAlignment[i][0]]+"'>"+oneAlignment[i][0]+"</p>"+"<p style='margin:0px; padding:0px; "+clustal[oneAlignment[i][1]]+"'>"+oneAlignment[i][1]+"</p>"+"</td>");
	}
	sequence0 += "</tr>";
	sequence1 += "</tr>";
	sequenceTable = sequenceTable + sequence0 + sequence1;
	sequenceTable += "</table>";
	document.getElementById(htmlElementID).innerHTML += sequenceTable;
}

function printMultipleAlignments(MultipleAlignments, sequenceName, htmlElementID){
	for(var i =0; i < MultipleAlignments.length; i++){
		printOneAlignment(MultipleAlignments[i], sequenceName, htmlElementID);
	}
}

function printAllAlignments(AllAlignments, sequenceNames, htmlElementID){
	AllAlignments = JSON.parse(AllAlignments.replace(/&quot;/g, '\"'));
	sequenceNames = JSON.parse(sequenceNames.replace(/&quot;/g, '\"'));
	for(var i =0; i < AllAlignments.length; i++){
		printMultipleAlignments(AllAlignments[i], sequenceNames[i].split("/").pop(), htmlElementID);
	}
}




