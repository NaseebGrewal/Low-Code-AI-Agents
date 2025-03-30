# No-Code-AI-Agents
<img src="https://imgur.com/stvLg4e.png" alt="Kid playing with puppies" width="100%" />

<p align="center">
  <img src="https://i.imgur.com/6pxhhot.png" alt="Kid Riding a dragon" width="45%" />
  <img src="https://imgur.com/yoK4RSc.png" alt="Cyborgs in Future" width="45%" />
</p>
<img src="https://imgur.com/HMU49Vi.png" alt="Football Ground in apocalypse" width="100%" />
<img src="https://imgur.com/MPPU7zU.png" alt="Unicorn in beautiful landscape" width="100%" />


# 🤖 AI Agent with n8n: Automate Your Workflow Like a Pro!

## 🚀 Overview
I built an AI-powered agent using [n8n](https://n8n.io/) to streamline my workflow like never before! This agent seamlessly integrates with Google services to:

- 📅 **Schedule meetings** on Google Calendar effortlessly.
- 📂 **Retrieve relevant files** from Google Drive using Retrieval-Augmented Generation (RAG).
- 🎨 **Generate AI-powered images** directly in chat.

With n8n's powerful automation capabilities, this AI agent acts as a personal assistant, saving time and effort while optimizing productivity.



## 🛠️ Tech Stack
- [n8n](https://n8n.io/) - Low-code automation tool
- **Google Calendar API** - For scheduling meetings
- **Google Drive API** - For document retrieval and RAG
- **AI Model (LLM & Image Generator)** - For generating responses and images

## 🔥 Why This is Awesome
✅ **No more manual scheduling** – AI handles your calendar.
✅ **Smart document retrieval** – No need to dig through files.
✅ **Creativity on demand** – Generate images right from chat.
✅ **Fully customizable** – Expand and tweak workflows as needed.

## 📌 How It Works
1. **User Request**: The AI agent receives a command (e.g., "Book a meeting for tomorrow at 10 AM").
2. **n8n Workflow Execution**: The request is processed, triggering Google APIs for scheduling and file retrieval.
3. **AI-Powered RAG**: If needed, the agent fetches and summarizes relevant files from Google Drive.
4. **Image Generation**: For creative tasks, it generates images and sends them in chat.

## 🔧 Setup & Installation
To set up this AI agent on your own:
1. Install n8n: `npm install -g n8n`
2. Set up Google API credentials.
3. Configure the n8n workflows for:
   - Google Calendar scheduling
   - Google Drive RAG
   - AI-powered chat and image generation
4. Deploy and enjoy automation magic! ✨

## 💡 Future Improvements
🔹 Integrate with more AI models (e.g., GPT-4, Gemini, etc.)
🔹 Add support for voice commands
🔹 Enhance personalization for different users

## New Updates

### New Folders and Features
- **Converted_Images/**: A new folder that now stores processed images.
- **Images/**: Contains source images; these are used by the image generation process in [`image_generation.py`](Low-Code-AI-Agents/image_generation.py).
- **Langchain/** and **Pydantic/**: New integrations are being developed to enhance prompt processing and data validation.

### Updated Functionalities
- **Prompt Processing**: Changes have been made to [`prompt_processing.py`](Low-Code-AI-Agents/prompt_processing.py) to improve handling of input prompts.
- **Improved Workflow**: With the latest updates, the project now better organizes image assets and supports advanced language chain functionality.

## Getting Started

1. Install dependencies from [`requirements.txt`](Low-Code-AI-Agents/requirements.txt):
   ````sh
   pip install -r requirements.txt

2. Configure the environment by updating the .env file.
3. Run the main scripts as needed, for example:
python image_generation.py