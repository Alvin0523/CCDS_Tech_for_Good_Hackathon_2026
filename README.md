# CCDS Tech for Good Hackathon 2026 🚀

## 🏆 Hackathon Results
### Top 3 Winners
| Rank | Team Name |
|------|-----------|
| 🥇 1 | Sirius |
| 🥈 2 | 2 JC 1 Poly |
| 🥉 3 | JAB |

### Finalists (Unranked)
| S.No | Team Name |
|------|-----------|
| 1 | Internal Pointer Variable |
| 2 | Debuggerz |
| 3 | Makan Quest |
| 4 | Ctrl Alt Win |
| 5 | Ask AI |
| 6 | Ri JiKa |
| 7 | Cooked for Cooking |

## 📰 Latest News
| Title | Link |
|-------|------|
| How Pathways in Python Initiative is Empowering the Next Generation of Computing Talent | [Read More](https://www.ntu.edu.sg/computing/news-events/news/detail/how-pathways-in-python-initiative-is-empowering-the-next-generation-of-computing-talent) |
| Team Sirius wins first place at Pathways in Python “Tech for Good” Hackathon | [Read More](https://www.ntu.edu.sg/computing/news-events/news/detail/team-sirius-wins-first-place-at-pathways-in-python--tech-for-good--hackathon) |

Welcome to the CCDS Tech for Good Hackathon 2026! This repository provides the foundation for building impactful solutions using Beautiful Soup, Pygame and LangChain!

---

## ✅ Before You Start
Ensure the following tools are installed on your computer (version requirements included):

| Tool | Download Link | Minimum Version | Check Command |
|------|---------------|-----------------|---------------|
| Visual Studio Code (VS Code) | [Download](https://code.visualstudio.com/download/) | - | - |
| Python | [Download](https://www.python.org/downloads/) | 3.10 | `python --version` |
| Git | [Download](https://git-scm.com/install/) | - | `git --version` |
| uv (Python Package Manager) | [Download](https://docs.astral.sh/uv/getting-started/installation/) | - | `uv --version` |

Run the check commands in your terminal to verify successful installation.

---

## 🛠️ Project Setup
Follow these step-by-step instructions to run your project locally:

### Step 1: Create a Project Folder
- Navigate to your Desktop
- Create a new folder
- Rename it to `CCDS-Hackathon`

### Step 2: Open the Folder in VS Code
- Launch **VS Code**
- Click `File → Open Folder`
- Select the `CCDS-Hackathon` folder

### Step 3: Open the VS Code Terminal
- Click `Toggle Panel (Ctrl + J) → Select Terminal`
- For Windows users: Select **Command Prompt** as the terminal type

### Step 4: Clone the Repository
Run the following command in the terminal:
```bash
git clone https://github.com/Alvin0523/CCDS_Tech_for_Good_Hackathon_2026.git
```

### Step 5: Open the Cloned Project Folder
- Click `File → Open Folder`
- Select the `CCDS_Tech_for_Good_Hackathon_2026` folder inside the parent `CCDS-Hackathon` folder

### Step 6: Install Dependencies with uv
```bash
uv sync
```

### Step 7: Activate the Virtual Environment
| Operating System | Activation Command |
|------------------|--------------------|
| Windows | `.venv\Scripts\activate.bat` |
| macOS / Linux | `source .venv/bin/activate` |

✅ **Verification**: You will see `(ccds-tech-for-good-2026)` prefix before the working directory in your terminal once activated.

### Step 8: Set Up Environment Variables 🔑
1. Rename the `.env.example` file to `.env`
2. Open the `.env` file and replace the placeholder with the Azure OpenAI API Key:
   ```
   c72e9614a1b54c38b836046ec01ec7de
   ```
> ⚠️ **Important Notes**:
> - DO NOT misuse this API Key
> - DO NOT push this API Key to Github
> - Always ensure `.env` is included in `.gitignore` before pushing to Github

### Step 9: AI Models Available for Use 🤖
| Model Name |
|------------|
| gpt-4.1-nano |
| gpt-5-mini |
| gpt-5-nano |

---

## 🎯 Workshop Objectives
By the end of this hackathon workshop, you will be able to:
- Understand how to scrape data using **Beautiful Soup**
- Build simple games and simulations using **Pygame**
- Create AI-powered applications using **LangChain**
- Manage Python dependencies using **uv**
- Collaborate using **Git and GitHub**

---

## 📁 Project Structure 
This repository is organised as follows:
```text
CCDS_Tech_for_Good_Hackathon_2026/
├── src/
│   ├── beautiful_soup/     # Web scraping workshop resources 🕸️
│   ├── langchain/          # LangChain & chatbot workshop resources 🤖
│   ├── pygame/             # Pygame workshop resources 🎮
│   └── resources/          # uv setup and supporting materials 📦
│
├── .env.example            # Example environment variables (API keys) 🔑
├── .gitignore              # Git ignore rules 🚫
├── .python-version         # Python version used for this project 🐍
├── README.md               # Project documentation 📖
├── pyproject.toml          # Project configuration & dependencies ⚙️
└── uv.lock                 # Locked dependency versions (uv) 🔒
```

---

## 📚 More Resources
| Tool/Library | Documentation Link |
|--------------|--------------------|
| Beautiful Soup | [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) |
| Pygame | [https://www.pygame.org/docs/](https://www.pygame.org/docs/) |
| LangChain | [https://python.langchain.com/](https://python.langchain.com/) |
| uv | [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/) |
