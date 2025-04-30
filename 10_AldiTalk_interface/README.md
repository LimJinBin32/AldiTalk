# Alditalk

## 🌟 Introduction  
**Alditalk** is an **AI-powered web application** designed to help users in **Singapore eldercare facilities** communicate seamlessly. It leverages **Azure AI Speech and Translation**, **OpenAI**, and **Meta AI APIs** to provide **real-time, accurate speech recognition, translation, and text-to-speech conversion**. The application supports **real-time Hokkien translation**, making it accessible to a wider audience while ensuring **effortless multilingual communication** in eldercare settings.

---

## 🔥 Key Features  
- **Real-Time Hokkien Translation** – One of the first **live Hokkien** translation tools, trained on localized datasets.  
- **Seamless Speech Recognition** – Converts spoken dialects into text with **Azure AI Speech**.  
- **Multi-Language Support** – Supports **English, Mandarin, Malay, Tamil, Cantonese, and Hokkien**, improving accessibility for diverse users.  
- **Specialized Vocabulary** – Focuses on **care-specific and medical terms** to enhance communication accuracy in eldercare scenarios.  
- **User-Friendly Interface** – Large buttons, clear fonts, and intuitive navigation for elderly users.  
- **Secure and Private** – No unnecessary data collection, ensuring **privacy and ethical AI use**.  
- **Scalable and Extensible** – Built on **Flask**, with RESTful APIs for easy expansion and cloud deployment.  

---

## 📖 Table of Contents  
- [🔧 Installation Guide](#-installation-guide)  
- [📖 User Manual](#-user-manual)  
- [🔮 Future Developments](#-future-developments)  
- [🛠️ Troubleshooting](#-troubleshooting)  
- [📜 License](#-license)  
- [📧 Contact](#-contact)  

---

## 🔧 Installation Guide  
Underlined words have embedded links to download the necessary software, and black-boxed lines indicate commands to run in the terminal.

### **1️⃣ Prerequisites**  
Ensure you have the following installed:  
- **Anaconda** → <a href="https://www.anaconda.com/products/distribution" target="_blank">Download Anaconda</a>  
- **Git** → <a href="https://git-scm.com/downloads" target="_blank">Download here</a>  

### **2️⃣ Download, unzip and open the folder in terminal**  
```bash
cd /PATH/TO/ALDITALK_INTERFACE
```  

### **3️⃣ Install Dependencies**  
#### **Windows, Mac & Linux Users**  
1. **Create and activate a Conda virtual environment:**  
    ```bash
    conda create -n alditalk-env python=3.12.8 -y
    conda activate alditalk-env
    ```  
2. Install the dependencies:  
    ```bash
    pip install requirements.txt
    ```    
3. Start the Flask application:  
    ```bash
    python app.py
    ```  

---

## 📖 User Manual  

### 🏠 Alditalk Homepage  
1. Toggle between **dark and light mode** for a comfortable viewing experience.  
2. Click the **blue microphone button** to **start recording your voice** and begin the translation process.  
3. Use the navigation menu to access:  
   - **Supported Languages** – View a list of languages and dialects Alditalk supports.  
   - **User Guide** – Learn how to use the application effectively.  
   - **About Alditalk** – Read more about the project and its development.  

---

### 🎙️ Speech-to-Text and Translation  
1. **Click the blue microphone button** to **start recording your voice**.  
2. **Alditalk will automatically detect** spoken **English, Mandarin, Malay, and Tamil**.  
3. For **Hindi, Cantonese, and Hokkien**, you must **manually select** the spoken language before recording.  
4. The detected speech is converted into text and translated into the selected output language.  
5. **The translated text will be played automatically** using text-to-speech.  
6. To listen again, press the **"Replay Audio"** button.  

---

### 📝 Text-to-Text Translation  
1. **Enter text** into the input box.  
2. Select the **source language** and the **target language**.  
3. Click the **"Translate"** button to generate the translated text.  
4. The translated text will appear in the output box and will be **played automatically** using text-to-speech.  
5. To replay the translation, click the **"Replay Audio"** button.  

---

### 🔊 Text-to-Speech (TTS)  
1. After translation, the **audio will play automatically**.  
2. To listen again, click the **"Replay Audio"** button.  
3. Alditalk will generate speech using **Azure Speech Service** or **Meta API** for dialect-based text-to-speech.  

---

## 🔮 Future Developments  
🚀 **Planned Features:**  
- **Mobile App Version** – Develop a mobile-friendly version for **Android & iOS** to improve accessibility.  
- **Custom Speech Models** – Train **custom AI models** for **all supported languages**, ensuring **better recognition of Singaporean accents and dialects**.  
- **Enhanced Hokkien Speech Recognition** – Improve **Hokkien STT accuracy** with larger datasets and optimized AI models.  
- **Expanded Dialect Support** – Add **more local dialects** beyond the current languages supported.  
- **Cloud Deployment for Scalability** – Host **Alditalk** on **cloud platforms** like AWS or Azure for broader accessibility.  
- **Offline Mode** – Enable **basic translation functionality without an internet connection**, improving usability in areas with limited connectivity.  

---

## 🛠️ Troubleshooting  

### **2️⃣ Conda Environment Not Activating**  
If you cannot activate the Conda environment:  
```bash
conda activate alditalk-env
```  

#### ✅ Solution:  
- **Windows Users:**  
  - **Use Anaconda Prompt** instead of the regular Command Prompt or PowerShell.  
  - If you see an error like:  
    ```bash
    CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'
    ```
    **Run the following command in Anaconda Prompt (or PowerShell as Admin):**  
    ```powershell
    conda init
    ```  
    Then restart **Anaconda Prompt** and try again.

- **Mac/Linux Users:**  
  - If Conda is not recognized, ensure it's properly initialized:  
    ```bash
    source ~/anaconda3/bin/activate
    conda activate alditalk-env
    ```  

---

### **3️⃣ Port 5001 Already in Use**  
If Flask fails to start due to the port being in use:  
```bash
OSError: [Errno 98] Address already in use
```  

#### ✅ Solution:  
- Find and kill the process using **port 5001**:  

    **Mac/Linux:**  
    ```bash
    lsof -i :5001  
    kill -9 <PID>
    ```  

    **Windows:**  
    ```powershell
    netstat -ano | findstr :5001  
    taskkill /PID <PID> /F
    ```  

- Then, restart the Flask server on **port 5001**:  
    ```bash
    python app.py
    ```  

---
# 📜 License

© 2025 Habib, Jin Bin, Alex, Min.  
All rights reserved.

This software, **Alditalk**, is proprietary and confidential. Unauthorized copying, distribution, modification, or commercial use of this software, via any medium, is **strictly prohibited** without prior written consent from the authors.

Permission is granted to use this software for **personal, educational, and internal business purposes only**. Any **commercial deployment, resale, or redistribution** requires a formal licensing agreement.

This software is provided **"as is,"** without warranty of any kind, express or implied, including but not limited to **the warranties of merchantability, fitness for a particular purpose, and non-infringement**. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability arising from the use of this software.

---

# 📧 Contact

For **business inquiries, partnerships, or licensing discussions**, please contact us:

📩 **Email:** [minmyrios@gmail.com](mailto:minmyrios@gmail.com)  

For general inquiries, feel free to reach out to any of the authors via the provided **email address**.