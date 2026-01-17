# AI-Powered Code Reviewer & Quality Assistant

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![AI/NLP](https://img.shields.io/badge/AI-NLP-green.svg)
![LLM](https://img.shields.io/badge/LLM-Powered-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Project Description

The AI-Powered Code Reviewer & Quality Assistant is an intelligent system that leverages advanced Large Language Models (LLMs) and Natural Language Processing techniques to automatically analyze, review, and provide actionable feedback on source code. This project streamlines the code review process by identifying bugs, suggesting improvements, enforcing coding standards, and offering optimization recommendations, thereby enhancing code quality and developer productivity.

## Features

- **Automated Code Analysis**: Performs comprehensive analysis of source code files to identify potential issues, bugs, and vulnerabilities
- **Intelligent Code Review**: Generates detailed review comments with specific improvement suggestions
- **Multi-Language Support**: Capable of reviewing code written in multiple programming languages
- **Quality Metrics**: Provides code quality scores and metrics based on industry best practices
- **Best Practice Recommendations**: Suggests adherence to coding standards, design patterns, and software engineering principles
- **Performance Optimization**: Identifies opportunities for code optimization and performance enhancement
- **Security Vulnerability Detection**: Highlights potential security risks and vulnerabilities in the codebase
- **Documentation Suggestions**: Recommends improvements for code documentation and comments
- **Configurable LLM Backend**: Supports multiple LLM providers with easy configuration options

## Techniques Used

### Natural Language Processing (NLP)

- **Code Tokenization**: Breaking down source code into meaningful tokens for analysis
- **Semantic Analysis**: Understanding code context and relationships between different components
- **Pattern Recognition**: Identifying common code patterns, anti-patterns, and code smells
- **Text Classification**: Categorizing code issues by severity, type, and priority

### Prompt Engineering

- **Structured Prompting**: Crafting detailed prompts to guide LLMs in generating accurate code reviews
- **Context-Aware Prompts**: Including relevant code context and background information in prompts
- **Few-Shot Learning**: Providing example reviews to improve LLM output quality
- **Chain-of-Thought Reasoning**: Encouraging step-by-step analysis for complex code evaluation

### LLM-based Text Generation

- **Code Review Generation**: Producing human-readable, actionable code review comments
- **Explanation Synthesis**: Creating clear explanations for identified issues and suggestions
- **Documentation Enhancement**: Generating improved documentation and inline comments
- **Adaptive Response Formatting**: Structuring output in various formats based on requirements

## Tech Stack

### Programming Language

- **Python 3.8+**: Core programming language for application development

### Libraries / Frameworks

- **Streamlit**: Interactive web-based user interface for code submission and review display
- **LangChain**: Framework for building LLM-powered applications and managing prompt workflows
- **OpenAI API / Anthropic API**: Integration with leading LLM providers
- **Google Generative AI**: Support for Google's Gemini models
- **Python-dotenv**: Environment variable management for secure API key handling
- **Pandas**: Data manipulation and analysis for code metrics
- **AST (Abstract Syntax Tree)**: Python code parsing and structural analysis

### AI / ML Technologies

- **Transformer-based Large Language Models**: GPT-4, Claude, Gemini, and other state-of-the-art LLMs
- **Prompt Template Engineering**: Structured templates for consistent and effective LLM interactions
- **Retrieval-Augmented Generation (RAG)**: Enhanced context retrieval for more accurate reviews

## LLM Details

This project utilizes **transformer-based Large Language Models** that have been trained on vast amounts of code and natural language data. These models excel at understanding code semantics, identifying patterns, and generating human-like review feedback.

**Configurable LLM Support**: The application is designed with a configurable LLM backend, allowing users to choose from multiple providers including:

- OpenAI (GPT-4, GPT-3.5)
- Anthropic (Claude)
- Google (Gemini)
- Other compatible LLM APIs

Users can easily switch between different LLMs by updating the configuration file or environment variables, making the system flexible and adaptable to different use cases and budget requirements.

## Project Structure

```
AI-Powered-Code-Reviewer-Quality-Assistant/
│
├── app.py                          # Main Streamlit application entry point
├── code_reviewer.py                # Core code review logic and LLM integration
├── prompts.py                      # Prompt templates for different review types
├── config.py                       # Configuration settings and LLM parameters
├── utils.py                        # Utility functions for code parsing and processing
│
├── requirements.txt                # Python dependencies
├── .env.example                    # Example environment variables file
├── .gitignore                      # Git ignore file
│
├── models/                         # LLM integration modules
│   ├── __init__.py
│   ├── openai_model.py
│   ├── anthropic_model.py
│   └── google_model.py
│
├── static/                         # Static assets for UI
│   ├── css/
│   └── images/
│
├── tests/                          # Unit tests and test cases
│   ├── test_code_reviewer.py
│   └── sample_code/
│
└── README.md                       # Project documentation
```

## Installation Steps

Follow these steps to set up the project locally:

1. **Clone the repository**

```bash
git clone https://github.com/RAMAKRISHNA-448/AI-Powered-Code-Reviewer-Quality-Assistant.git
cd AI-Powered-Code-Reviewer-Quality-Assistant
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory and add your API keys:

```
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

5. **Verify installation**

```bash
python -c "import streamlit; import langchain; print('Installation successful!')"
```

## How to Run the Project Locally

1. **Ensure you are in the project directory with the virtual environment activated**

```bash
cd AI-Powered-Code-Reviewer-Quality-Assistant
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Run the Streamlit application**

```bash
streamlit run app.py
```

3. **Access the application**

Open your web browser and navigate to:

```
http://localhost:8501
```

4. **Using the application**

- Upload or paste your code in the provided text area
- Select your preferred LLM model from the dropdown menu
- Choose the type of review (general, security-focused, performance-focused, etc.)
- Click "Review Code" to generate the analysis
- View the detailed review results with suggestions and recommendations

5. **Optional: Run tests**

```bash
pytest tests/
```

## Certification Use Case

This project is designed to meet Infosys certification requirements and demonstrates proficiency in:

- **Artificial Intelligence & Machine Learning**: Implementation of LLM-based solutions for practical software engineering problems
- **Natural Language Processing**: Application of NLP techniques for code understanding and analysis
- **Prompt Engineering**: Advanced prompt design and optimization for LLM interactions
- **Software Development Best Practices**: Clean code architecture, modular design, and comprehensive documentation
- **API Integration**: Seamless integration with multiple third-party AI services
- **Full-Stack Development**: End-to-end application development from backend logic to frontend interface

The project showcases the ability to leverage cutting-edge AI technologies to solve real-world challenges in software development, aligning with industry standards and certification objectives.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

**Developed by**: RAMAKRISHNA

**Contact**: For questions or collaboration opportunities, please open an issue on GitHub.

**Contributions**: Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
