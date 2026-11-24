# AI Learning – Day 1

**Environment:** Windows + Git Bash + VS Code  
**Python:** 3.14.4

## Project Setup

### 1. Create Virtual Environment

```bash
py -m venv venv
```

### 2. Activate Environment (Git Bash)

```bash
source venv/Scripts/activate
```

### 3. Select Interpreter in VS Code

- Press `Ctrl + Shift + P`
- Select `Python: Select Interpreter`
- Choose `venv/Scripts/python.exe`

### 4. Install Dependencies

```bash
python -m pip install numpy pandas matplotlib jupyter scikit-learn
```

### 5. Save Dependencies

```bash
python -m pip freeze > requirements.txt
```

## Running the Project Again

Every time you reopen the project:

```bash
source venv/Scripts/activate
python main.py
```

To reinstall dependencies if needed:

```bash
python -m pip install -r requirements.txt
```

## Useful Commands

| Command | Purpose |
|---|---|
| `py --version` | Check Python |
| `python --version` | Check active Python |
| `python -m pip list` | List packages |
| `deactivate` | Exit virtual environment |

**Note:** Use `python`, not `python3`, in Git Bash on this Windows setup.