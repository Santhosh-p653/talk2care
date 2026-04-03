let chatHistory=[];


function startListening() {

    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";

    recognition.start();

    recognition.onresult = function(event) {
        const text = event.results[0][0].transcript;

        addMessage(text, "user-msg");

        // send to backend
        fetch("/process", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: text })
        })
        .then(res => res.text())
        .then(data => {
            addMessage(data, "bot-msg");
			speak(data);
        });
    };
}

function addMessage(text, className) {
    const chatBox = document.getElementById("chatBox");

    const msg = document.createElement("div");
    msg.className = className;
    msg.innerText = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
	chatHistory.push({
		type:className=== "user-msg"?"user":"bot",text:text
	});
}

function speak(text){
	const speech=new SpeechSynthesisUtterance(text);
	speech.lang="en-US";
	window.speechSynthesis.speak(speech);
}

function downloadSummary() {

    fetch("/summary", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(chatHistory)
    })
    .then(res => res.text())
    .then(summary => {

        const blob = new Blob([summary], { type: "text/plain" });
        const url = window.URL.createObjectURL(blob);

        const a = document.createElement("a");
        a.href = url;
        a.download = "Talk2Care_Report.txt";
        a.click();
    });
}
