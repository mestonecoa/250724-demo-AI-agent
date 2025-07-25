# AI Agent Demo

This repository contains a Python-based AI agent that acts as a research assistant, built by replicating [Tech With Tim's YouTube tutorial](https://www.youtube.com/watch?v=bTMPwUgLZf0). The agent uses [LangChain](https://www.langchain.com/) to query Wikipedia and DuckDuckGo, processes user queries with a large language model (LLM) like OpenAI's GPT-4o, and saves structured research output to a text file with timestamps.

## Features
- Performs web searches using DuckDuckGo and Wikipedia.
- Integrates with LLMs (e.g., OpenAI GPT-4o or Anthropic Claude) via LangChain.
- Saves research results to a text file (`research_output.txt`) with a timestamp.
- Outputs structured data (title, summary, sources, tools used) using Pydantic.
- Beginner-friendly command-line interface for entering research queries.

## Prerequisites
- Python 3.10 or higher (3.11 recommended, as used in development)
- A code editor like [Visual Studio Code](https://code.visualstudio.com/)
- API keys for OpenAI or Anthropic (optional, depending on the LLM used)
- Git installed for cloning the repository

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/mestonecoa/250724-demo-AI-agent.git
   cd 250724-demo-AI-agent
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # On Mac/Linux
   python3.11 -m venv venv
   source venv/bin/activate
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API keys**:
   - Create a `.env` file in the project root.
   - Add your OpenAI or Anthropic API key (get keys from [OpenAI](https://platform.openai.com/api-keys) or [Anthropic](https://console.anthropic.com/settings/keys)):
     ```env
     OPENAI_API_KEY=your_openai_key
     ANTHROPIC_API_KEY=your_anthropic_key
     ```
   - **Important**: Do not commit `.env` to GitHub. It’s included in `.gitignore`.

## Usage
1. Run the main script:
   ```bash
   python main.py
   ```

2. Enter a research query when prompted, e.g., "Tell me about John Mayer and save to a file".
3. The agent will:
   - Query Wikipedia and/or DuckDuckGo.
   - Generate a structured response (title, summary, sources, tools used).
   - Save the output to `research_output.txt` if instructed.
4. Check the console for the agent’s thought process (verbose mode) and `research_output.txt` for saved results.

**Example Output**:
See `examples/example_output.txt` for a sample of `research_output.txt`, which might look like:
```
---Research Output---
2025-07-24 22:05:49

John Mayer's most successful record is often considered to be 'Continuum,' released in 2006. The album received critical acclaim and includes popular tracks like 'Gravity' and 'Waiting on the World to Change.' It showcases Mayer's skills as a guitarist and songwriter, contributing significantly to his reputation in the music industry.
```

## Project Structure
- `main.py`: Core script to initialize and run the AI agent with LangChain.
- `tools.py`: Defines tools for DuckDuckGo search, Wikipedia queries, and saving output to a text file.
- `requirements.txt`: Lists Python dependencies required to run the project.
- `research_output.txt`: Sample output file showing the agent’s research results.
- `.env`: Stores API keys for OpenAI or Anthropic (not committed).
- `random_notes.md`: Developer notes on setup and Git commands (optional documentation).

## Credits
This project replicates the AI agent tutorial by [Tech With Tim](https://www.youtube.com/watch?v=bTMPwUgLZf0). All code is adapted from the tutorial’s [GitHub repository](https://github.com/techwithtim/PythonAIAgentFromScratch) with minor modifications.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to open issues or submit pull requests for improvements. As this is a learning project, contributions are welcome but should align with the tutorial’s scope.

## Contact
For questions, reach out via [GitHub Issues](https://github.com/mestonecoa/250724-demo-AI-agent/issues).