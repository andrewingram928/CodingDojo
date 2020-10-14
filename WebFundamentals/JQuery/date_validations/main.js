$(document).ready(function() {

    $( function() {
        var dateFormat = "mm/dd/yy",
          from = $( "#from" )
            .datepicker({
              defaultDate: "+1w",
              changeMonth: true,
              numberOfMonths: 1
            })
            .on( "change", function() {
              to.datepicker( "option", "minDate", getDate( this ) );
            }),
          to = $( "#to" ).datepicker({
            defaultDate: "+1w",
            changeMonth: true,
            numberOfMonths: 1
          })
          .on( "change", function() {
            from.datepicker( "option", "maxDate", getDate( this ) );
          });
     
        function getDate( element ) {
          var date;
          try {
            date = $.datepicker.parseDate( dateFormat, element.value );
          } catch( error ) {
            date = null;
          }
     
          return date;
        }
    });
    $("form").submit(function() {
        return false;
    })

    $( "form" ).submit(function( event ) {
        var name_length = $(".name").val().length;
            if(name_length==0) {
                alert( "Please input your name before submitting!" );
                event.preventDefault();
                return false;
            }
    });
        

});