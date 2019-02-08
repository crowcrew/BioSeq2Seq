<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link type="text/css" rel="stylesheet" href="static/css/app.css">
        <link type="text/css" rel="stylesheet" href="static/css/bootstrap.css">
        <script src="static/js/jquery-3.3.1.min.js"></script>
        <script src="static/js/bootstrap.js"></script>
        <script src="static/js/app.js"></script>
        <script src="static/js/protenizer.js"></script>
        <script src="https://d3js.org/d3.v4.min.js"></script>
        <title>Sequence Alignment Algorithms</title>
        <link rel="shortcut icon" href="static/image/favicon.ico" type="image/x-icon">
    </head>
    <body>
        <nav class=
        "navbar navbar-expand-sm navbar-dark bg-dark static-top">
            <a  href="/">BioSeq2Seq</a>
        </nav><br>
        <script>
        render("{{ protein_sequence }}",  "{{userFile}}");
        </script>
         <footer class="footer centered bg-dark customFooter fixed-bottom">
                Copyright (c) 2018-2019 Ruaa Sleiman, Aly Shmahell.
        </footer>
    </body>
</html>
