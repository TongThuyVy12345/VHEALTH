 class Chatbox {

        constructor() {
            this.args = {
//                openButton: document.querySelector('.chatbox__button'),
                chatBox: document.querySelector('.chatbox__support'),
                sendButton: document.querySelector('.send__button')
            }
        this.state = false;
        this.messages = [];
        this.textField = null;
    }

    display() {
        const { chatBox, sendButton,fieldValue} = this.args;

        this.prompt(chatBox)
        sendButton.addEventListener('click', () => this.onSendButton(chatBox,fieldValue));
        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
               this.onSendButton(chatBox);
            }
        })

    }

    prompt(chatbox) {
        this.messages.push({ name: "Bot", titl: "Get Start." });
        this.updateChatText(chatbox)
    }




    updateChatText(chatbox) {
  const chatmessage = chatbox.querySelector('.chatbox__messages');
  chatmessage.innerHTML = '';

  this.messages.slice().reverse().forEach((item, index) => {
    var textField = chatbox.querySelector('input');
    let text1 = textField.value
    const messageItem = document.createElement('div');
    messageItem.classList.add('messages__item');

    if (item.name === 'Bot') {
      messageItem.classList.add('messages__item--visitor');
      messageItem.textContent = item.titl;
    } else
    {




      const operatorMessageItem = document.createElement('div');
      operatorMessageItem.classList.add('messages__item', 'messages__item--operator');
      operatorMessageItem.textContent = item.titl;
//      chatmessage.appendChild(buttonContainer);
      chatmessage.appendChild(operatorMessageItem);
    }



    chatmessage.appendChild(messageItem);
  });
}

onSendButton(chatbox,fieldValue) {
    var textField = chatbox.querySelector('input');
    let text1 = fieldValue;
    if (textField.value !== "") {
    text1 = textField.value;
    }
    if (text1 === "") {
        return;
    }

    fetch("/get_bot_response", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ titl: text1 })
})
      .then(response => response.json())
      .then(r => {
        let msg2 = { name: "Bot", titl:r.rps};
        let msg1 = { name: "User", titl: text1}
        this.messages.push(msg1);
        this.messages.push(msg2);
        this.updateChatText(chatbox)
        console.log(msg2)
        console.log(msg1)
        textField.value = ''
      })
      .catch( error => {
        console.log(error);
        this.updateChatText(chatbox)
        textField.value = ''
      });
}
}
const chatbox = new Chatbox();
chatbox.display();
