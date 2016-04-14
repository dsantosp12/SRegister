$(document).ready(function(){
  $('.collapsible').collapsible({
    accordion : false
  });
});

$('.datepicker').pickadate({
    selectMonths: true,
    selectYears: 150
});

function emptyInputs() {
    for (var i = 0; i < arguments.length; i++)
        if (arguments[i].trim() == "") return true;
    return false;
}