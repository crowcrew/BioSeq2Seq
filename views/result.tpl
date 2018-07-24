<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link type="text/css" rel="stylesheet" href="static/css/app.css">
        <link type="text/css" rel="stylesheet" href="static/css/bootstrap.css">
        <script src="static/js/jquery-3.3.1.min.js"></script>
        <script src="static/js/bootstrap.js"></script>
        <script src="static/js/app.js"></script>
        <script src="static/js/seqHighlight.js"></script>
        <title>JS Bin</title>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
            <a class="navbar-brand" href="/">Sequence Alignment Algorithms: Applications and Implementation</a>
        </nav>
        <br>
        <span></span>
        <div class="alignmentWrapper">
        	<div id="alignmentDiv" class="alignmentDiv"></div>
        </div>
        <script>
        printAllAlignments("{{ alignment }}", "{{sequenceNames}}", "alignmentDiv");
        </script>
    </body>
</html>

