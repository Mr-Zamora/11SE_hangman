# 🎮 Hangman Game Project Scaffold

## 📚 Course Information
**Instructor:** Mr Zamora  
**Email:** 📧 rzamora@rj.nsw.edu.au  
**Course:** Year 11 Software Engineering  
**Institution:** Richard Johnson College  

This repository contains a basic implementation of a Hangman game that you'll extend and enhance as part of your assessment. The scaffold provides core functionality that you can build upon while adding your own features.

## 🚀 Getting Started: Step-by-Step Guide

### Prerequisites
1. Install these tools first:
   - [Git](https://git-scm.com/downloads) - For managing your code
   - [Python](https://www.python.org/downloads/) (Version 3.8 or higher)
   - [VSCode](https://code.visualstudio.com/) or [Windsurf](https://windsurf.codeium.com/) - Code editor

### Setting Up Your Project (Choose VSCode OR Windsurf)

#### 🌟 Step 1: Fork on GitHub
1. **Sign in to GitHub**
   - Go to [github.com](https://github.com)
   - Click "Sign In" (or create account if needed)
   - Use your school email for registration

2. **Create Your Fork**
   - Visit the project repository: [https://github.com/Mr-Zamora/11SE_hangman]
   - Click the "Fork" button in the top-right corner
   - Select your account as the destination
   - Wait for GitHub to create your copy
   - You'll be redirected to your fork: `github.com/YOUR_USERNAME/hangman`

3. **Configure Repository**
   - On your forked repository page:
     - Click "Settings" tab
     - Rename repository if desired (e.g., "hangman-YOUR_NAME")
     - Make sure repository is "Public"
     - Copy your repository URL (green "Code" button)

#### 🔄 Option 1: Using VSCode
1. **Clone Your Fork**
   - Open Command Prompt (Windows)
   - Navigate to your preferred location:
     ```bash
     cd Documents
     ```
   - Clone using YOUR fork's URL:
     ```bash
     git clone https://github.com/YOUR_USERNAME/hangman.git
     cd hangman
     ```

2. **Open in VSCode**
   - Open VSCode
   - Go to File → Open Folder
   - Select your cloned hangman folder
   - Install recommended extensions:
     - Python extension
     - Git extension

3. **Set Up Python Environment**
   - Open VSCode terminal (View → Terminal)
   - Create virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate virtual environment:
     ```bash
     # On Windows:
     .\venv\Scripts\activate
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

#### 🌊 Option 2: Using Windsurf
1. **Fork the Repository**
   - Same as VSCode step 1

2. **Open in Windsurf**
   - Go to [windsurf.codeium.com](https://windsurf.codeium.com/)
   - Click "Open Repository"
   - Paste your forked repository URL
   - Windsurf will automatically:
     - Clone the repository
     - Set up the Python environment
     - Install dependencies

### 🎯 Verify Setup
1. **Test Python**
   - Open `h3-scaffold.py`
   - Run the file:
     - VSCode: Click ▶️ (Run) button
     - Windsurf: Click "Run" in top menu
   - You should see the game menu

2. **Test Git**
   - Make a small change (add a comment)
   - Commit the change:
     ```bash
     git add .
     git commit -m "Test commit"
     git push
     ```

### 🆘 Common Issues
1. **Python Not Found**
   - Make sure Python is added to PATH during installation
   - Restart VSCode/Windsurf after installing Python

2. **Git Not Found**
   - Restart computer after installing Git
   - Make sure Git is added to PATH

3. **Permission Errors**
   - Run Command Prompt as Administrator
   - Check file permissions

4. **Need Help?**
   - Ask your instructor (Mr Zamora)
   - Check error messages carefully
   - Google the exact error message

## 📁 Project Structure

```
hangman/
├── hangman-scaffold.py       # Core game implementation
├── requirements.txt     # Project dependencies
├── README.md           # Project guide
├── LOGBOOK.md          # Development log template
├── REFLECTION.md       # Reflection report template
├── .gitignore          # Git ignore rules
└── docs/               # Documentation templates
    ├── STORYBOARD.md   # Game flow documentation
    ├── DATA_FLOW.md    # Data flow diagram documentation
    ├── FLOWCHART.md    # Game logic flowchart
    └── DATA_DICTIONARY.md  # Variable and structure definitions
```

### 📚 Documentation Templates
The `docs/` directory contains templates for required documentation:

1. 🎨 **STORYBOARD.md**
   - Game flow visualization
   - Interface descriptions
   - Feature documentation

2. 🔄 **DATA_FLOW.md**
   - Input processing flow
   - Data transformation documentation
   - Output generation description

3. 📈 **FLOWCHART.md**
   - Detailed game logic flowchart
   - Decision paths
   - Loop structures

4. 📊 **DATA_DICTIONARY.md**
   - Variable definitions
   - Data structure documentation
   - Function parameter descriptions

Use these templates as starting points for your documentation. Each template includes:
- Required sections
- Example content
- Implementation notes
- Formatting guidelines

## 📋 Assessment Overview

### 📝 Part 1: Documentation (40 marks)

#### 1. 🎨 Storyboard (5 marks)
Create a diagram showing the game flow:
- Difficulty selection
- Gameplay progression
- Win/lose conditions
- Optional feature interactions

#### 2. 🔄 Data Flow Diagram (5 marks)
Create a diagram showing:
- Input processing (player guesses)
- Data transformation (guess validation, score updates)
- Output generation (game state, messages)

#### 3. 📊 Data Dictionary (5 marks)
Document key variables in a table format:
| Variable | Type | Purpose |
|----------|------|---------|
| score | integer | Tracks player's current score |
| guessed_letters | set | Stores unique letters guessed |
| current_word | string | The word player needs to guess |

#### 4. 📈 Flowchart (10 marks)
Create a detailed flowchart showing:
- Game initialization
- Main game loop
- Decision points
- Win/lose conditions

#### 5. 💭 Reflection Report (5 marks)
Write a one-page report covering:
- AI usage examples and contributions
- Challenges and solutions
- Learning outcomes

#### 6. 💬 Code Comments (5 marks)
Add clear, informative comments explaining:
- Function purposes
- Complex logic
- Implementation decisions

#### 7. 📔 Logbook (5 marks)
Maintain a development log with:
- ⏰ Timestamps
- ✅ Task descriptions
- 🔍 Problem-solving approaches
- 🤖 AI usage documentation

#### 8. 📚 Bibliography
List all resources used:
- Tutorials
- Documentation
- Code references
- AI tools

### 💻 Part 2: Development (40 marks)

#### ⭐ Minimum Features (20 marks)
1. Three difficulty levels
2. Game progress display
3. Letter/word guessing
4. Score system
5. Documented AI integration

#### 🌟 Additional Features (20 marks)
Implement at least TWO:
1. ⏱️ Guess timer
2. 💡 Word hints
3. 📄 Custom word list (CSV)
4. 🤖 AI API integration
5. 💾 Save game state
6. 🖥️ Flask GUI

### 📝 Part 3: Code Understanding Exam (20 marks)

A 30-minute in-class assessment covering:
1. 🔍 Code explanation (10 marks)
2. 🐛 Debugging knowledge (5 marks)
3. 🤖 AI reflection (5 marks)

## ⚠️ Important Notes

1. 🤖 **AI Usage**: Document all AI interactions in your reflection report and logbook
2. 📚 **Code Understanding**: Your exam performance affects your final grade
3. ⚖️ **Academic Integrity**: AI misuse will result in zero marks until demonstrated understanding

## 🤖 AI Integration Guidelines

### Available AI Tools
1. **OpenAI (ChatGPT)**
   - Access: [chat.openai.com](https://chat.openai.com)
   - Features: Code generation, debugging, optimization
   - API Cost: ~$20/month for ChatGPT Plus

2. **Google Gemini**
   - Access: [gemini.google.com](https://gemini.google.com)
   - Features: Code analysis, multi-modal understanding
   - Free tier available

3. **Windsurf IDE with Cascade**
   - Integrated development environment
   - Real-time code suggestions
   - Context-aware assistance
   - Available through school license

### Best Practices for AI Usage
1. **Planning & Design**
   - Use AI to brainstorm features
   - Get feedback on architecture decisions
   - Review documentation structure

2. **Implementation**
   - Break down complex problems
   - Request code explanations
   - Get help with debugging
   - Always review and understand generated code

3. **Documentation**
   - Log all AI interactions
   - Note which parts were AI-assisted
   - Explain how you modified AI suggestions

4. **Common Pitfalls to Avoid**
   - Don't copy code without understanding
   - Don't rely solely on AI for debugging
   - Don't skip documentation of AI usage

## 📤 Submission Guidelines

### 1. Documentation Package
Create a single Word document containing:
- All documentation from `/docs` folder
- Completed REFLECTION.md
- Final LOGBOOK.md entries
- Screenshots of key features
- Bibliography of resources used

### 2. Code Submission
1. **GitHub Repository**
   - Clean, documented code
   - All required files and folders
   - README.md updated with your details
   - Public repository link

2. **Canvas Submission**
   - Word document with documentation
   - GitHub repository link
   - Any additional notes or comments

### 3. Submission Checklist
- [ ] Documentation Word file complete
- [ ] Code thoroughly commented
- [ ] All files pushed to GitHub
- [ ] Repository is public
- [ ] Canvas submission includes all links
- [ ] AI usage properly documented
- [ ] Logbook up to date
- [ ] Reflection report complete

### 4. Due Dates
- Documentation Package: [Date]
- Code Submission: [Date]
- In-Class Exam: [Date]

*Note: Late submissions may incur penalties unless prior arrangements are made.*

## 🆘 Getting Help

1. 📖 Review the scaffold code comments
2. 🔍 Check Python documentation
3. 👨‍🏫 Consult your instructor
4. 📝 Document all external resources used

## 📜 License

This project scaffold is provided for educational purposes. Students are free to modify and extend it as required for their assessment.

---
*Note: This README serves as your project guide. Refer to it regularly to ensure you're meeting all assessment requirements.* ✨
