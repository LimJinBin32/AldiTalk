# 🎧 AldiTalk: Singapore Dialect Translator for Elderly Use

**AldiTalk** is a full-stack, speech-to-speech translation web app designed to enhance communication between caregivers and elderly residents in care homes. It focuses on real-time translation of **local dialects** such as **Hokkien** and **Cantonese**, which are not well supported by standard AI services, while ensuring an accessible, senior-friendly user interface.

---

## 💡 Motivation
In facilities like **Apex Harmony Lodge**, many elderly residents speak in dialects while caregivers use standard English. This linguistic mismatch can lead to misunderstandings, stress, and reduced care quality. AldiTalk bridges this communication gap by translating spoken language and dialects in real time.

---

## 🧰 Supported Languages
- **Standard Languages**: English, Mandarin, Malay, Tamil, Hindi  
- **Dialects**: Cantonese, **Hokkien** (custom-supported)

---

## 🧱 Architecture Overview

```text
[User Speech Input]
    ⇓
Azure STT / Custom STT (Hokkien)
    ⇓
Azure Translator / GPT-4o (dialect logic)
    ⇓
TTS: Azure Neural Voices / Meta MMS-TTS-NAN (for Hokkien)
    ⇓
[Spoken Output to User]
```

---

## 🔧 Key Features
- One-click **speech-to-speech** translation between dialects and standard languages
- Elderly-friendly UI (large buttons, dark/light mode, minimal clicks)
- Real-time translation using Azure + custom AI integrations
- Custom **Hokkien STT + TTS pipeline** via:
  - Azure Custom Speech
  - Pe̍h-ōe-jī romanization (via GPT-4o)
  - Meta's mms-tts-nan model
- Flask backend + RESTful API architecture

---

## 📺 Demo Video
Watch the full app demo here: [YouTube – AldiTalk: Connecting Voices, even the Silent Ones](https://www.youtube.com/watch?v=GFAS6MAVhic)

---

## 🧬 Technologies Used

| Area               | Tools/Frameworks                        |
|--------------------|-----------------------------------------|
| Backend            | Flask, Python                           |
| Frontend           | HTML, CSS, JavaScript                   |
| Speech & AI        | Azure STT/TTS, Azure Translator, OpenAI GPT-4o |
| Hokkien TTS        | Meta MMS-TTS-NAN (via Hugging Face)     |
| Data Collection    | YouTube OCR, Volunteer recordings       |
| Model Training     | Azure Custom Speech (Mandarin)          |
| Deployment         | Flask + Gunicorn (production ready)     |

---

## 📊 Data Collection & Processing
- **YouTube Dramas**: Frame segmentation → OCR → transcript alignment → audio segmentation
- **Volunteer Speech**: Custom-built recorder app for Hokkien phrases
- **Augmentation**: Speed, pitch, volume, noise — to simulate diverse conditions

> Final dataset: 21 hours YouTube + 3 hours augmented speech data

---

## 🎯 Model Performance
- **Initial WER (YouTube only)**: 65.89%
- **Final WER (YouTube + Volunteer + Augmentation)**: **13.01%**

---

## 📌 Challenges

- Lack of native Hokkien support in Azure  
- Budget constraints: $10/hr for model training, OCR costs ~$2 per episode [We spent ~$400 for this project (provided by School and Azure).]  
- Limited publicly available annotated Hokkien datasets  

---

## 🛋️ Read the docs
All related documents from project proposal to report and slides are uploaded to this repository as well. Please refer to those in case of doubt as they provide more details in depth than this README.md.

---

## 🛡️ Securit & Privacy  Notice
API keys and credentials are excluded and managed via `.env` files. Please create your own `.env` based on `env.example` before running the Flask app.
This repository is soley for learning and showcase purposes and must not be monetized in any way unless authorized.
---

## 🚀 Run Locally
1. Clone the repo:
```bash
git clone https://github.com/yourusername/alditalk.git
cd AldiTalk
cd 10_AldiTalk_Interface
```
2. Create `.env` with your Azure credentials
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run Flask app:
```bash
python app.py
```

---

## 🌐 Future Improvements
- Support more dialects (e.g., Teochew)
- Collect data from Hokkien foundations
- Improve accent/context handling in medical care
- Explore deployment via wearable devices

---

## 💎 Authors & Credits
[Year 2, AI Engineering Project, Diploma in AI & Data Engineering, Nanyang Polytechnic]
- **[Min Phyo Thura]**(https://github.com/your-github-handle)  
- [Lim Jin Bin](https://github.com/LimJinBin32)  
- [Alexander Chan](https://github.com/Redbeanchan)  
- [Mohammad Habib](https://github.com/habibmohammad35) 
Data soucring and engineering is mostly done by **Min** while video, model training, Flask integration, and UI/UX were jointly developed.

---

Thanks for checking out **AldiTalk** — a step towards inclusive, elder-friendly technology in Singapore 🇸🇬!
