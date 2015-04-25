$(document ).ready(function() {
  lat = $('#id_lat');
  lng = $('#id_lng');
  $('#map_canvas').locationpicker({radius: 0,
                                  enableAutocomplete: true, 
                                  location: { latitude: lat[0].value, longitude: lng[0].value},
                                  inputBinding: { locationNameInput: $('#locationinput'), 
                                                  latitudeInput: lat,
                                                  longitudeInput: lng}});
});
