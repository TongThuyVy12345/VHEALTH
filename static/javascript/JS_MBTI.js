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
        this.messages.push({ name: "Bot", message: "Get Start to Holland Quiz." });
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
      messageItem.textContent = item.message;
    } else
    {
    const buttonContainer = document.createElement('div');
      buttonContainer.classList.add('messages__item--visitor');

     for (let i = 0; i < 2; i++) {
        const button = document.createElement('button');
        button.id = 'btn' + i;
        const span = document.createElement('span');
        span.id = 'choice' + i;
        span.textContent = item['choiceValue' + (i + 1)];
        button.appendChild(span);
        buttonContainer.appendChild(button);
        button.addEventListener('click', () => {
          const fieldValue = textField.value;

          if(span.textContent==item['choiceValue1'])
          {    textField.value ="A";
          }
          if(span.textContent==item['choiceValue2'])
          {    textField.value ="B";
          }
          this.onSendButton(chatbox, textField.value);


          console.log(span.textContent);
        });

      }

      const operatorMessageItem = document.createElement('div');
      operatorMessageItem.classList.add('messages__item', 'messages__item--operator');
      operatorMessageItem.textContent = item.message;
      chatmessage.appendChild(buttonContainer);
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

    fetch("/mbti", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: text1 })
})
      .then(response => response.json())
      .then(r => {
        let msg2 = { name: "Bot", message:r.question};
        let msg1 = { name: "User", message: text1,'choiceValue1':r.choice1,'choiceValue2':r.choice2,}
        this.messages.push(msg1);
        this.messages.push(msg2);
        this.updateChatText(chatbox)
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