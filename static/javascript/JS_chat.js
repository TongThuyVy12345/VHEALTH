const msgerChat = get(".msger-chat");
function botResponse() {

  var input = $(".msger-input").val();
  if (!input) {
    return;
  }

  // Display the user's message in the chat window
  appendMessage(USER_NAME, USER_IMG, "left", input);

  // Send the user's message to the server
  $.ajax({
    type: "POST",
    url: "/get_bot_response",
    contentType: "application/json",
    data: JSON.stringify({ message: input }),
    success: function (response) {
    success: function (response) {
      // Display the bot's message in the chat window
      var botResponse = response["message"];
      var question = response["question_test"];
      appendMessage(USER_NAME, USER_IMG, "right", question);
      appendMessage(BOT_NAME, BOT_IMG, "left", botResponse);

      // Clear the input field
      $(".msger-input").val("");

      // Scroll to the bottom of the chat window
      $(".msger-chat").scrollTop($(".msger-chat").prop("scrollHeight"));

    },
    error: function (error) {
      console.log(error);
    },
  });
}
var messages = document.querySelectorAll('.msg, .left-msg');

var fadeIn = function() {
  var opacity = 0;
  var intervalID = setInterval(function() {
    opacity += 0.1;
    for (var i = 0; i < messages.length; i++) {
      messages[i].style.opacity = opacity;
    }
    if (opacity >= 1) {
      clearInterval(intervalID);
    }
  }, 50);
};

fadeIn();
