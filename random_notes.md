# Using md to memo stuff

Within three backticks (next to 1, with ~, on the keyboard) is called a code block
By identifying the language, it'll achieve "syntax highlighting"

^ + ` to open Terminal on VS Code
">" at the search bar at the top of VS code for more directions.


```bash
cd another_folder
git commit -m "Initial commit"
```

```python
print('hello world') #prints hello world
def addition(a, b):
    return a+b
```

# Actual memos
```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
git init
git add .
git commit -m "some commit comment"
git add main.ipynb random_notes.md
git push origin main
git diff main.ipynb random_notes.md
```