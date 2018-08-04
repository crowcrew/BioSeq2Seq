/**
    credit for Array.prototype.remove goes to: https://stackoverflow.com/questions/3954438/how-to-remove-item-from-array-by-value
 */
Array.prototype.remove = function() {
  var what,
    a = arguments,
    L = a.length,
    ax;
  while (L && this.length) {
    what = a[--L];
    while ((ax = this.indexOf(what)) !== -1) {
      this.splice(ax, 1);
    }
  }
  return this;
};

$(document).ready(function() {
  $("#getalignment").submit(function() {
    if ($("#user_file").val() == "") {
      alert("please choose a file to upload first");
      return false;
    }
    return true;
  });
  $("#getProtein").submit(function() {
    if ($("#user_file_to_protein").val() == "") {
      alert("please choose a file to upload first");
      return false;
    }
    return true;
  });
  var selected_database_files = new Array();
  $(".list li").click(function(e) {
    if ($(this).is(".selected")) {
      $(this).removeClass("selected");
      selected_database_files.remove($(this).html());
    } else {
      $(this).addClass("selected");
      selected_database_files.push($(this).html());
    }
    $("#selected_database_files").val(selected_database_files);
    console.log($("#selected_database_files").val());
  });
});
