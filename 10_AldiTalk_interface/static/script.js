// On load, check dark mode preference

window.onload = function () {
  if (localStorage.getItem('darkMode') === 'enabled') {
    document.body.classList.add('dark-mode');
    document.getElementById('themeSwitch').checked = true;
  }
};

function toggleTheme() {
  document.body.classList.toggle('dark-mode');
  localStorage.setItem('darkMode', document.body.classList.contains('dark-mode') ? 'enabled' : 'disabled');
}

function translateText() {
  let inputText = document.getElementById("inputText").value;
  let translateTo = document.getElementById("translateTo").value;
  let apiEndpoint = "/translate";  
  let requestBody = { text: inputText, target_lang: translateTo };

  if (translateTo === "zh-hokkien") { 
      apiEndpoint = "/translate_hokkien";
  }

  console.log("Sending translation request to:", apiEndpoint, "with data:", requestBody);

  fetch(apiEndpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(requestBody)
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById("outputText").value = data.translation || `[Error]: ${data.error}`;

      if (data.translation) {
          console.log("✅ Translation Successful:", data.translation);

          
          storedAudio = null;
          document.getElementById("playAudioButton").disabled = true;  

         
          playTTS();
      }
  })
  .catch(err => {
      console.error("Translation fetch error:", err);
      document.getElementById("outputText").value = "[Error]: Unable to connect to server.";
  });
}


function translatePhrase(phrase) {
  document.getElementById("inputText").value = phrase; 
  document.getElementById("outputText").value = `[Translating]: ${phrase}`;

  console.log("✅ [DEBUG] Quick Translation Requested:", phrase);


  storedAudio = null;
  document.getElementById("playAudioButton").disabled = true;
  document.getElementById("playAudioButton").style.opacity = "0.5";

  
  fetch("/translate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: phrase, target_lang: document.getElementById("translateTo").value })
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById("outputText").value = data.translation || `[Error]: ${data.error}`;
      console.log("✅ [DEBUG] Quick Translation Result:", data.translation);
  })
  .catch(() => {
      document.getElementById("outputText").value = "[Error]: Unable to connect to server.";
  });

  // deleted the old file to have the play audio button reset
  fetch("/delete_old_tts", { method: "POST" })
  .then(response => response.json())
  .then(data => console.log("✅ [DEBUG] Deleted Old TTS:", data))
  .catch(err => console.error("❌ [ERROR] Deleting Old TTS:", err));
}

function clearTranslation() {
  document.getElementById("inputText").value = "";
  document.getElementById("outputText").value = "";
}

function startRecording() {
  const recordButton = document.getElementById('recordButton');
  const recordingIndicator = document.getElementById('recordingIndicator');
  let translateFrom = document.getElementById("translateFrom").value;
  let apiEndpoint = "/stt_autodetect"; // Default STT API
  let requestBody = {};

  // This is for Hindi or Cantonese (can be expanded to other languages)
  if (translateFrom === "hi-IN" || translateFrom === "yue-CN") { 
    apiEndpoint = "/stt_basic";
    requestBody = { target_lang: translateFrom };
  } 
  // This is for Hokkien
  else if (translateFrom === "zh-hokkien") {
    apiEndpoint = "/stt_hokkien";
    requestBody = { target_lang: "zh-CN" }; // Mandarin is used for Hokkien STT
  }

  console.log("🎤 Sending STT request to:", apiEndpoint, "with data:", requestBody); // Debugging

  // UI: Show recording indicator
  recordButton.style.backgroundColor = "green";
  recordingIndicator.classList.remove('hidden');

  // Send request to Flask backend
  fetch(apiEndpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(requestBody)
  })
    .then(response => response.json())
    .then(data => {
      if (data.recognized_text) {
        document.getElementById("inputText").value = data.recognized_text; // Display recognized speech

        // ✅ Automatically trigger translation after transcription
        translateText();
      } else {
        document.getElementById("outputText").value = `[Error]: ${data.error}`;
      }
    })
    .catch(err => {
      console.error("STT fetch error:", err);
      document.getElementById("outputText").value = "[Error]: Unable to connect to server.";
    })
    .finally(() => {
      // UI: Hide recording indicator
      recordButton.style.backgroundColor = "#007bff";
      recordingIndicator.classList.add('hidden');
    });
}

function addNewPhrase() {
  let newPhrase = prompt("Enter the new phrase:");
  if (newPhrase && newPhrase.trim() !== "") {
    let phraseList = document.querySelector(".phrase-list");
    let newDiv = document.createElement("div");
    newDiv.classList.add("phrase-item", "user-phrase");
    newDiv.innerHTML = `<p>${newPhrase}</p>
      <button class="phrase-delete-button" onclick="deletePhrase(this)">Delete</button>
      <button class="phrase-translate-button" onclick="translatePhrase(${JSON.stringify(newPhrase)})">Translate</button>`;
    phraseList.appendChild(newDiv);
  }
}

function deletePhrase(button) {
  button.parentNode.remove();
}


let storedAudio = null; // Global variable to store the TTS audio

function playTTS() {
  let text = document.getElementById("outputText").value;
  let language = document.getElementById("translateTo").value;
  let playButton = document.getElementById("playAudioButton");

  console.log("🎙 Sending TTS request for:", language, "Text:", text);

  fetch("/tts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: text, language: language })
  })
  .then(response => response.json())
  .then(data => {
      if (data.audio_url) {
          storedAudio = new Audio(data.audio_url);
          storedAudio.play()
          playButton.disabled = false;  // 
          playButton.style.opacity = "1";  // 
          console.log("✅ TTS Audio Ready:", data.audio_url);
      } else {
          document.getElementById("outputText").value = `[Error]: ${data.error}`;
          playButton.disabled = true; 
          playButton.style.opacity = "0.5";  
      }
  })
  .catch(err => {
      // it will catch an error due to there being no hokkien audio file just pass it
  });
}

function playStoredAudio() {
if (storedAudio) {
  storedAudio.play();
}
}

// clearing the audio when the clear txt button is pressed
function clearTranslation() {
  document.getElementById("inputText").value = "";
  document.getElementById("outputText").value = "";
  storedAudio = null;
  let playButton = document.getElementById("playAudioButton");
  playButton.disabled = true;  
  playButton.style.opacity = "0.5";
}
