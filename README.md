# 🦜🔗 YT & Website URL Summarizer  
A Streamlit app that extracts content from **web pages** or **YouTube videos** and generates a **clean, concise summary** using **LangChain** + **Groq LLM**.

---
## Live App

You can use the deployed version here:  
**[Live App](https://hrmpw9uaqtjueagqydtfju.streamlit.app/)**

### ▶️ How to Use the Live Streamlit App:
1. Open the above link in your browser.
2. On the left sidebar, enter your **GROQ API Key**.
3. In the main input box, paste any:
   - YouTube video URL  
   - Website URL  
4. Click the **"Summarize the content from YT or Website"** button.
5. Wait a few seconds.
6. Your summary will appear below in a formatted output.

That's it — no installation required. Just paste a URL and get a summary!

---

## 🚀 Features
- 🔗 Summarize the content of **any website URL**
- ▶️ Extract & summarize **YouTube video transcripts**
- ⚡ Uses **Groq's ultra-fast Llama model**
- 🧠 Built using **LangChain latest version**
- 🎨 Simple & clean Streamlit UI

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit**
- **LangChain**
- **Groq LLM- 'llama-3.1-8b-instant'**
- **YouTube Transcript API**
- **Web loaders**

---

## 📦 Installation

```bash
git clone https://github.com/sush-sp777/YT-Website-URL-Summarizer.git
cd YT-Website-URL-Summarizer
pip install -r requirements.txt
```
▶️ Run the Application:

```bash
streamlit run app.py
```
---

## 🛠️ How It Works
- URL Input
User enters either:
1. A YouTube link
2. Any website URL

- Content Extraction
1. YouTube → transcript fetched using YoutubeLoader
2. Website → HTML parsed using UnstructuredURLLoader

- Chunking
1. Long text is split into overlapping chunks

- Chunk Summaries
1. Each chunk is summarized individually using:
Prompt template &
Groq Llama-3.1-8B-Instant model

- Final Combined Summary
1. All chunk summaries are merged into a polished 350–400 word final summary.

- 📌 Example Output

✔ Clear bullet-point summary
✔ Organized logic
✔ No repetitions
✔ Only the most important concepts

