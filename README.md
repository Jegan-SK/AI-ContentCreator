# ✍️ AI Content Creator Suite

An intuitive Streamlit application powered by the Google Gemini API (`google-genai` SDK) that automatically generates tailored multi-channel content, including social media posts, emails, blog outlines, and presentation decks.

---

## LIVE DEMO :
   https://ai-contentcreator-1008.streamlit.app/

## 🌟 Key Features

* **6 Content Formats Supported:**
  * 💼 **LinkedIn Posts:** Structured, engaging, professional posts with clear CTAs.
  * 📸 **Instagram Captions:** Complete with hooks, emojis, and target hashtags.
  * 🐦 **Twitter/X Posts:** Punchy, concise messages tuned for character limits.
  * 📧 **Email Drafts:** Professional email copies with subject lines and greetings.
  * 📝 **Blog Outlines:** Detailed structural breakdown with titles, subsections, and key points.
  * 📊 **Presentation Content:** Slide-by-slide structure with titles and concise bullet points.
* **Dynamic Customization & Bonus Features:**
  * **Tone Selector:** Switch between *Professional* and *Casual* writing styles dynamically.
  * **Emoji Mode:** Toggle appropriate emojis on or off.
  * **Character & Word Counter:** Live stats for generated text.
  * **Export Utility:** One-click TXT download of generated output.

---

## 🛠️ Project Structure

AI-Content-Creator-Suite/
│
├── app.py              # Streamlit core application & logic
├── .env                # Environment variables (API keys)
├── .gitignore          # Keeps secrets and unnecessary files out of Git
└── requirements.txt    # Python dependencies

---

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have **Python 3.10+** installed on your machine.

### 2. Clone the Repository
git clone https://github.com/your-username/AI-Content-Creator-Suite.git
cd AI-Content-Creator-Suite

### 3. Create a Virtual Environment
* **macOS / Linux:**
  python3 -m venv venv
  source venv/bin/activate

* **Windows:**
  python -m venv venv
  venv\Scripts\activate

### 4. Install Dependencies
pip install -r requirements.txt

---

## 🔑 Environment Configuration

1. Locate or create the `.env` file in the root directory:
   touch .env

2. Add your Google Gemini API Key:
   GEMINI_API_KEY=your_gemini_api_key_here

> ⚠️ **Note:** Never commit your `.env` file to version control. The `.gitignore` file included in this repository ensures your secrets stay private.

---

## 🖥️ Running the Application

Launch the Streamlit app locally:

streamlit run app.py

The application will open automatically in your default browser at `http://localhost:8501`.

---

## ⚙️ How It Works

1. **Select Settings:** Use the sidebar controls to pick your desired target platform (LinkedIn, Instagram, Email, etc.), tone, and emoji preferences.
2. **Provide Prompt Context:** Enter your target topic, key notes, or audience details into the main text box.
3. **Generate & Export:** Click **✨ Generate Content** to trigger the Gemini request (`gemini-2.5-flash`). View live character/word statistics and click **⬇️ Download Content** to save your output locally.

---

## 🧰 Tech Stack

* **UI Framework:** Streamlit
* **LLM Engine:** Google Gemini API (`google-genai` SDK)
* **Model:** `gemini-3.5-flash`
* **Configuration:** `python-dotenv`
