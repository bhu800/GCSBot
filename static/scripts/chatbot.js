$(document).ready(function(){
    // make socket object
    var socket = io();

    // send info that socketio has been connected
    socket.on('connect', function(){
        socket.send(data = "I am Connected!!")
    });

    // show message on receiving message in 'message' event bucket
    socket.on('response',function(data){
        console.log(data);
    });

    // send message on pressing submit button
    $('#send_query').click(function(){

        socket.emit('query', {'msg': $('#user_query').val()});
        // Clear the input area
        $('#user_query').val("");
    });

    // send message on pressing 'enter'
    $('#user_query').keypress(function(e){
        if(e.keyCode==13){

            socket.emit('query', {'msg': $('#user_query').val()});
            // Clear the input area
            $('#user_query').val("");
        }
    });

    
})