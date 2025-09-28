# Web Navigator Agent

A high-performance LangChain-powered web browsing agent that can search and navigate websites.

# Web Navigator - Browser Automation Agent

A powerful browser automation system that uses AI to perform web tasks automatically using natural language commands.

## a) Problem Statement Reference

### Problem Statement Chosen
Manual web browsing and data extraction tasks are time-consuming and repetitive. Users need an intelligent system that can understand natural language instructions and perform complex web interactions automatically.

### Reason to Choose the Problem Statement
- **Efficiency**: Automates repetitive web tasks that normally take hours
- **Accessibility**: Allows non-technical users to perform complex web operations
- **Scalability**: Can handle multiple tasks simultaneously without human intervention
- **Accuracy**: Reduces human errors in data extraction and web interactions

## b) Solution Overview

### Proposed Approach
We developed an AI-powered browser automation agent that uses Ollama's Gemma model to understand natural language instructions and perform web tasks through automated browser interactions.

### Key Features / Modules
- **Task Runner**: Executes user-defined web automation tasks
- **Browser Controller**: Manages Edge browser interactions and navigation
- **AI Agent**: Processes natural language and makes intelligent decisions
- **Error Handler**: Provides robust error handling and retry mechanisms
- **Status Monitor**: Tracks task execution and provides real-time feedback
- **Interactive Mode**: Allows real-time user interaction with the agent

## c) System Architecture

### Architecture Diagram / Workflow
```
User Input (Natural Language)
        ↓
   Task Processor
        ↓
   Ollama Gemma Model (AI Decision Making)
        ↓
   Browser Controller (Edge Browser)
        ↓
   Web Page Interaction
        ↓
   Result Extraction & Processing
        ↓
   Output to User
```

### Data Flow Explanation
1. **Input Processing**: User provides natural language task description
2. **AI Analysis**: Ollama Gemma model analyzes the task and creates action plan
3. **Browser Automation**: System controls Edge browser to execute planned actions
4. **Content Extraction**: Extracts relevant information from web pages
5. **Result Processing**: Formats and presents results to the user
6. **Error Handling**: Manages failures and provides meaningful feedback

## d) Technology Stack

### Backend
- **Python 3.11**: Core programming language
- **Browser-Use Library**: Browser automation framework
- **Asyncio**: Asynchronous programming for efficient task handling

### Frontend
- **Microsoft Edge**: Browser engine for web interactions
- **Command Line Interface**: User interaction interface

### Databases
- **Environment Variables**: Configuration storage (.env files)
- **Local File System**: Task logs and temporary data storage

### ML/AI Frameworks
- **Ollama**: Local AI model hosting platform
- **Gemma Model**: Google's open-source language model
- **Browser-Use Agent**: AI-powered browser automation framework

### APIs / Libraries
- **Selenium WebDriver**: Web browser automation
- **Python-dotenv**: Environment variable management
- **Asyncio**: Asynchronous programming support
- **Time**: Task timing and delays

## e) Algorithms & Models

### Algorithm(s) Chosen
- **Reinforcement Learning**: Agent learns from browser interactions
- **Natural Language Processing**: Text understanding and command parsing
- **Computer Vision**: Web element detection and interaction
- **Decision Trees**: Task planning and execution flow

### Reason for Choice
- **Ollama Gemma**: Runs locally, ensuring privacy and no API costs
- **Open Source**: Free to use and customize
- **Offline Capability**: Works without internet connection to AI services
- **Lightweight**: Efficient resource usage compared to cloud-based models

### Model Training & Testing Approach
- **Pre-trained Model**: Uses Ollama's pre-configured Gemma model
- **Fine-tuning**: Adapts to specific web automation tasks through usage
- **Testing Strategy**: Validates against common web interaction scenarios
- **Performance Monitoring**: Tracks success rates and execution times

## f) Data Handling

### Data Sources Used (APIs/Datasets)
- **Web Pages**: Live web content from various websites
- **Search Engines**: DuckDuckGo for information retrieval
- **User Input**: Natural language task descriptions
- **Browser State**: Current page content and navigation history

### Preprocessing Methods
- **Text Sanitization**: Cleans extracted web content
- **HTML Parsing**: Extracts meaningful data from web pages
- **Content Filtering**: Removes irrelevant information
- **Data Validation**: Ensures extracted data quality

### Storage / Pipeline Setup
- **Environment Configuration**: Stores API keys and settings in .env files
- **Session Management**: Maintains browser state during task execution
- **Log Files**: Records task execution history and errors
- **Temporary Storage**: Handles intermediate processing data

## g) Implementation Plan

### Initial Setup & Environment
1. **Python Environment**: Set up Python 3.11 with virtual environment
2. **Ollama Installation**: Install and configure Ollama with Gemma model
3. **Browser Setup**: Configure Microsoft Edge for automation
4. **Dependencies**: Install required Python packages from requirements

### Core Module Development
1. **Agent Core**: Develop main browser automation agent
2. **Task Processor**: Build natural language task interpreter
3. **Browser Controller**: Implement web page interaction logic
4. **Error Handler**: Create robust error handling system

### Integration & Testing
1. **Unit Testing**: Test individual components
2. **Integration Testing**: Verify component interactions
3. **End-to-End Testing**: Validate complete task workflows
4. **Performance Testing**: Optimize execution speed and accuracy

### Final Deployment-ready Build
1. **Code Optimization**: Refine algorithms for better performance
2. **Documentation**: Complete user guides and API documentation
3. **Package Distribution**: Create installable packages
4. **Production Setup**: Configure for production environment

## h) Performance & Validation

### Evaluation Metrics
- **Task Success Rate**: Percentage of successfully completed tasks
- **Execution Time**: Average time to complete different task types
- **Error Rate**: Frequency of failures and error types
- **User Satisfaction**: Feedback on result accuracy and usefulness

### Testing Strategy
- **Functional Testing**: Verify all features work as expected
- **Stress Testing**: Test with multiple concurrent tasks
- **Compatibility Testing**: Ensure works across different websites
- **Regression Testing**: Validate updates don't break existing functionality

## i) Deployment & Scalability

### Deployment Plan
- **Local Installation**: Users install on their personal computers
- **Docker Containers**: Containerized deployment for consistency
- **Virtual Environments**: Isolated Python environments for each user
- **Configuration Management**: Easy setup through environment files

### Scalability Considerations
- **Multi-threading**: Handle multiple tasks simultaneously
- **Resource Management**: Optimize memory and CPU usage
- **Queue System**: Manage task queues for high-volume scenarios
- **Load Balancing**: Distribute tasks across multiple browser instances

---

## Quick Start Guide

### Prerequisites
- Python 3.11 or higher
- Ollama installed with Gemma model
- Microsoft Edge browser

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd Web_Navigator

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
copy .env.example .env
# Edit .env file with your configurations
```

### Usage
```bash
# Run simple task
python simple_task_runner.py

# Run interactive mode
python interactive_agent.py

# Check system status
python status_check.py
```

### Example Tasks
- "Navigate to Google and search for weather"
- "Go to GitHub and find trending repositories"
- "Visit news website and summarize top headlines"
- "Find contact information on company website"

---

## Contributing
1. Fork the repository
2. Create feature branch
3. Make changes and test thoroughly
4. Submit pull request with detailed description

## License
This project is licensed under MIT License - see LICENSE file for details.

## Support
For issues and questions, please create an issue in the GitHub repository or contact the development team.

## Features

- ⚡ **Optimized Performance**: Browser instance reuse, lighter AI model, and efficient resource management
- 🌐 **Multi-Platform Support**: Amazon, Flipkart, and Google search integration
- 🧠 **Smart AI**: Uses Ollama with LangChain for intelligent task processing
- 🎯 **Fast Response**: Headless browsing and optimized timeouts for quick results
- 📊 **Performance Monitoring**: Built-in performance testing and resource cleanup tools

## Quick Start

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Install Playwright browsers:**
```bash
playwright install
```

3. **Start Ollama and pull the optimized model:**
```bash
ollama pull llama3.2:1b  # Much faster than gemma
```

4. **Run the agent:**
```bash
python run_agent.py
```

## Performance Optimizations

### 🚀 Speed Improvements
- **Browser Reuse**: Single browser instance instead of creating new ones
- **Lighter AI Model**: `llama3.2:1b` instead of `gemma` for faster processing
- **Headless Mode**: No GUI rendering for better performance
- **Optimized Timeouts**: Reduced wait times for faster responses
- **Memory Management**: Proper cleanup and resource management

### 📊 Performance Monitoring
```bash
# Test performance with sample queries
python performance_test.py

# Clean up Ollama processes if needed
python cleanup_ollama.py
```

## Usage

Enter your search queries when prompted. The agent will automatically:
- Detect if you want to search Amazon, Flipkart, or use Google
- Navigate to the appropriate website
- Perform the search efficiently
- Return the results URL with timing information

**Example queries:**
- "search for laptops on amazon"
- "find mobile phones on flipkart"
- "search for python programming books"

Type 'exit' to quit.

## Troubleshooting

### High CPU Usage
If you notice high CPU usage from Ollama:
```bash
python cleanup_ollama.py
```

### Slow Performance
1. Ensure you're using the lighter model: `llama3.2:1b`
2. Check available system memory
3. Close other browser instances
4. Run the performance test to identify bottlenecks

### Memory Issues
The agent now includes automatic cleanup, but you can manually restart if needed.

## Technical Details

- **AI Model**: `llama3.2:1b` (optimized for speed)
- **Browser**: Chromium with performance flags
- **Timeout**: 15 seconds (reduced from 30)
- **Memory**: Optimized with proper cleanup
- **Concurrency**: Single-threaded with efficient resource sharing
![Uploading image.png…]()


Uploading 28.09.2025_19.00.13_REC WEB.......mp4…





