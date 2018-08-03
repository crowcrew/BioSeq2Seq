<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <link type="text/css" rel="stylesheet" href="static/css/app.css">
        <link type="text/css" rel="stylesheet" href="static/css/bootstrap.css">
        <script src="static/js/jquery-3.3.1.min.js"></script>
        <script src="static/js/bootstrap.js"></script>
        <script src="static/js/app.js"></script>
        <script src="static/js/seqHighlight.js"></script>
        <script src="https://d3js.org/d3.v4.min.js"></script>
        <title>Sequence Alignment Algorithms</title>
        <link rel="shortcut icon" href="static/image/favicon.ico" type="image/x-icon">
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
            <a class="navbar-brand" href="/">Sequence Alignment Algorithms: Applications and Implementation</a>
        </nav>
        <script>
        render("{{ alignment }}", "{{sequenceNames}}", "{{userFile}}");
        </script>
    </body>
</html>
