$(document).ready(function(){
    // make socket object
    var socket = io();

    // send info that socketio has been connected
    socket.on('connect', function(){
        socket.send(data = "I am Connected!!")
    });

    // show message on receiving message in 'message' event bucket
    socket.on('response',function(data){        
        printUserMsg(data);
        printBotMsg(data);

        // scroll chat window automatically
        scrollDownChatWindow();
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

    function printUserMsg(msg) {
        var message = $("<div class=\"msg-text\"></div>").text(msg.user_query)
        var user_icon = $('<div class="msg-img" style="background-image: url(https://image.flaticon.com/icons/svg/145/145867.svg)"></div>')
        var username_span = $("<div class=\"msg-info-name\"></div>").text("You")
        var timestamp_span = $("<div class=\"msg-info-time\"></div>").text(msg.timestamp)
        var message_info = $("<div class=\"msg-info\"></div>").append(username_span, timestamp_span);
        var message_bubble = $("<div class=\"msg-bubble\"></div>").append(message_info, message);
        var message_div = $("<div class=\"msg right-msg\"></div>").append(user_icon, message_bubble);
        $('#display-chat-section').append(message_div);
        // console.log(message_div);
    }

    function printBotMsg(msg) {
        var message = $("<div class=\"msg-text\"></div>").text(msg.bot_response)
        var bot_icon = $('<div class="msg-img" style="background-image: url(https://image.flaticon.com/icons/svg/327/327779.svg)"></div>')
        var username_span = $("<div class=\"msg-info-name\"></div>").text("GCSBot")
        var timestamp_span = $("<div class=\"msg-info-time\"></div>").text(msg.timestamp)
        var message_info = $("<div class=\"msg-info\"></div>").append(username_span, timestamp_span);
        var message_bubble = $("<div class=\"msg-bubble\"></div>").append(message_info, message);
        var message_div = $("<div class=\"msg left-msg\"></div>").append(bot_icon, message_bubble);
        $('#display-chat-section').append(message_div);
        // console.log(message_div);
    }

    // auto-scroll function
    function scrollDownChatWindow() {
        const chatWindow = document.querySelector("#display-chat-section");
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
})

