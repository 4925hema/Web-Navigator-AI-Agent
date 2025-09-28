# Web Navigator Agent

A high-performance LangChain-powered web browsing agent that can search and navigate websites.

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


