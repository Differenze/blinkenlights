<html>
<script type=text/javascript src="{{
  url_for('static', filename='jquery-3.5.1.min.js') }}"></script>

<head>
    <title>Blinkenlights</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='stylesheet.css') }}">
</head>
<body>

Some text!

<script>
function updateLed(name, value) {
    $.post("api/post", {name: name, value: value/10}, function(result){
        $("span").html(result);
  });
};

function renderLed(name) {
    return '<div class="led"><div class="name_label">'+name+'</div><input type="range" min="0" max="10" value="0" class="slider" oninput="updateLed(\''+name+'\', this.value)" onchange="updateLed(\''+name+'\', this.value)" id="myRange"></div>';
};

$.getJSON( "api/led_names", function( data ) {
  var items = [];
  $.each( data, function( key, val ) {
    items.push(renderLed(key))
  });

//  $( "<ul/>", {
//    "class": "my-new-list",
//    html: items.join( "" )
//  }).appendTo( "body" );
    $(items.join("")).appendTo("body")
});



function myFunction(x) {
    $.post("api/post", {name: x}, function(result){
        $("span").html(result);
  });


}
</script>


</body>


</html>