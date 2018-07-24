<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link type="text/css" rel="stylesheet" href="static/css/app.css">
        <link type="text/css" rel="stylesheet" href="static/css/bootstrap.css">
        <script src="static/js/jquery-3.3.1.min.js"></script>
        <script src="static/js/bootstrap.js"></script>
        <script src="static/js/app.js"></script>
        <title>JS Bin</title>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
            <a class="navbar-brand" href="/">Sequence Alignment Algorithms: Applications and Implementation</a>
        </nav>
        <br>
        <main role="main" class="container">
            <div class="row">
                <div class="col-3">
                </div>
                <div class="col-6 card bg-dark modifiedCard">
                    <form method="POST" role="form" action="/getalignment" id="getalignment" enctype="multipart/form-data">
			  <div class="form-group card-block">
			      <input type="file" class="form-control-file bg-light" name="user_file" id="user_file" >
			      <br>
			      <select class="form-control form-control-lg" name="selected_algorithm" i="selected_algorithm">
					<option value="smith_waterman" selected="selected">Local Alignment</option>
					<option value="needleman_wunsch">Global Alignment</option>
			      </select>
			      <br>
			      <ul class="list bg-light">
			      %for link in links:
					<li class="" >{{link}}</li>
			      %end
                              </ul>
                              <br>
			      <button type="submit" class="btn btn-primary" id="submit">Submit</button>
			      <input type="hidden" name="selected_database_files" id="selected_database_files">
			  </div>
		    </form>
                </div>
            </div>
        </main>
    </body>
</html>

