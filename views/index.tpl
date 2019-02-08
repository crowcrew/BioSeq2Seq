<!DOCTYPE html>
<html>
<head>
  <meta name="generator" content=
  "HTML Tidy for HTML5 for Linux version 5.2.0">
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link type="text/css" rel="stylesheet" href="static/css/app.css">
  <link type="text/css" rel="stylesheet" href=
  "static/css/bootstrap.css">
  <script src="static/js/jquery-3.3.1.min.js">
  </script>
  <script src="static/js/bootstrap.js">
  </script>
  <script src="static/js/app.js">
  </script>
  <title>Sequence Alignment Algorithms</title>
  <link rel="shortcut icon" href="static/image/favicon.ico" type=
  "image/x-icon">
</head>
<body>
  <nav class=
  "navbar navbar-expand-sm navbar-dark bg-dark static-top">
    <a  href="/">BioSeq2Seq</a>
  </nav><br>
  <main role="main" class="container">
    <div class="row">
      <div class="col-12 card bg-dark centered">
        <label class="customLabel">Download Alignment Examples</label>
        <ul class="list bg-light">
          %for file in alignment_user_input_files:
            <li class=""><a href={{file}} download>{{file.split('/')[-1]}}</a></li>
          %end
        </ul>
        <label class="customLabel">Download Protein Production Examples</label>
        <ul class="list bg-light">
          %for file in protein_production_user_input_files:
            <li class=""><a href={{file}} download>{{file.split('/')[-1]}}</a></li>
          %end
        </ul>
      </div>
      
    </div>
    <br>
    <div class="row">
      <div class="col-4 card bg-dark">
        <label class="customLabel">Sequence Alignment</label>
        <form method="post" role="form" action="/getalignment" id=
        "getalignment" enctype="multipart/form-data" name=
        "getalignment">
          <div class="form-group card-block">
            <input type="file" class="form-control-file bg-light"
            name="user_file" id="user_file"><br>
            <select class="form-control form-control-lg" name=
            "selected_algorithm" i="selected_algorithm">
              <option value="smith_waterman" selected="selected">
                Local Alignment
              </option>
              <option value="needleman_wunsch">
                Global Alignment
              </option>
            </select><br>
            <ul class="list bg-light">
              %for link in links:
              <li class="">{{link}}</li>
              %end
            </ul><br>
            <button type="submit" class="btn btn-primary" id=
            "submit">Submit</button> <input type="hidden" name=
            "selected_database_files" id="selected_database_files">
          </div>
        </form>
      </div>
      <div class="col-4"></div>
      <div class="col-4 card bg-dark">
        <label class="customLabel">Protein Production</label>
        <form method="post" role="form" action="/getProtein" id=
        "getProtein" enctype="multipart/form-data" name=
        "getProtein">
          <div class="form-group card-block">
            <input type="file" class="form-control-file bg-light"
            name="user_file_to_protein" id="user_file_to_protein">
            <br>
            <button type="submit" class="btn btn-primary" id=
            "submit">Submit</button>
          </div>
        </form>
      </div>
    </div>
    <div class="row">
      <footer class="col-12 footer centered bg-dark customFooter">
      Copyright (c) 2018-2019 Ruaa Sleiman, Aly Shmahell.
      </footer>
    </div>
  </main>
</body>
</html>
