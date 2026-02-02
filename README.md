# CCDS Tech for Good Hackathon 2026

Welcome to the CCDS Tech for Good Hackathon 2026! This repository provides the foundation for building impactful solutions using Beautiful Soup, Pygame and LangChain!

## Before You Start
Make sure you have the following installed on your computer:

- **[Visual Studio Code](https://code.visualstudio.com/download/)** (VS Code)
- **[Python](https://www.python.org/downloads/)** (version 3.10 or later)
- **[Git](https://git-scm.com/install/)** 
- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** (Python package manager) 

You can check if they’re installed by running these commands in a terminal:

```
python --version
git --version
uv --version
```

## Project Setup

Follow these steps to run your project locally:

#### 1. Create a Project Folder
- Go to your Desktop
- Create a new folder
- Rename it to `CCDS-Hackathon`

#### 2. Open the Folder in VS Code

- Open **VS Code**
- Click File → Open Folder
- Select the `CCDS-Hackathon` folder

#### 3. Open the VS Code Terminal

- Click Toggle Panel (Ctrl + J) → Select Terminal
- Select **Command Prompt** for Windows

#### 4. Clone the Repository

- Run the following command in the terminal:
 ```
 git clone https://github.com/Alvin0523/CCDS_Tech_for_Good_Hackathon_2026.git
 ```

#### 5. Open the Cloned Project Folder
- Click File → Open Folder
- Select the `CCDS_Tech_for_Good_Hackathon_2026` folder inside `CCDS-Hackathon`

#### 6. Install Dependencies with uv
```
uv sync
```

#### 7. Activate the Virtual Environment
- For Windows
```
.venv\Scripts\activate.bat
```
- For macOS / Linux
```
source .venv/bin/activate
```
You should see `(ccds-tech-for-good-2026)` before the working directory in your terminal

#### 8. Set Up Environment Variables
- Rename the `.env.example` file to `.env`
- Open `.env`and replace the Azure OpenAI API Key with
```
c72e9614a1b54c38b836046ec01ec7de
```
**DO NOT** misuse this API Key<br>
**DO NOT** push this API Key to Github<br>
Always ensure `.env` is included in `.gitignore` before pushing to Github

#### 9. AI Models Available for Use
- gpt-4.1-nano
- gpt-5-mini
- gpt-5-nano

## Workshop Objectives

By the end of this hackathon workshop, you will be able to:

- Understand how to scrape data using **Beautiful Soup**
- Build simple games and simulations using **Pygame**
- Create AI-powered applications using **LangChain**
- Manage Python dependencies using **uv**
- Collaborate using **Git and GitHub**

## Project Structure 

This repository is organised as follows:

```text
CCDS_Tech_for_Good_Hackathon_2026/
├── src/
│   ├── beautiful_soup/     # Web scraping workshop resources
│   ├── langchain/          # LangChain & chatbot workshop resources
│   ├── pygame/             # Pygame workshop resources
│   └── resources/          # uv setup and supporting materials
│
├── .env.example            # Example environment variables (API keys)
├── .gitignore              # Git ignore rules
├── .python-version         # Python version used for this project
├── README.md               # Project documentation
├── pyproject.toml          # Project configuration & dependencies
└── uv.lock                 # Locked dependency versions (uv)
```

## More Resources

- Beautiful Soup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Pygame Documentation: https://www.pygame.org/docs/
- LangChain Documentation: https://python.langchain.com/
- uv Documentation: https://docs.astral.sh/uv/
