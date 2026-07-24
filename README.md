# Agentic Blog Content Generator (CrewAI Multi-Agent System)

An autonomous multi-agent pipeline that transforms YouTube video content into publication-ready blog posts. Built using **CrewAI** to orchestrate specialized AI agents that collaborate sequentially — one agent researches, the other writes — with **Gemini 2.5 Flash** powering reasoning and generation.

## 🚀 Features

- **Multi-Agent Orchestration** — Two specialized agents (Researcher & Writer) work sequentially using CrewAI's `Process.sequential` pipeline.
- **YouTube Content Extraction** — Custom `YoutubeChannelSearchTool` integration retrieves and synthesizes video transcriptions for a given topic.
- **LLM-Powered Reasoning** — Gemini 2.5 Flash handles both research synthesis and blog writing, with configurable temperature for tone control.
- **Agent Memory & Caching** — Persistent memory and response caching reduce redundant LLM calls and improve efficiency.
- **Rate-Limited Execution** — Configurable `max_rpm` ensures stable, cost-controlled API usage.
- **Automated Output Export** — Final blog posts are written directly to a markdown file, ready for publishing.

## 🧠 How It Works

1. **Research Agent** searches a specified YouTube channel for videos relevant to a given topic and extracts a structured, comprehensive research report from the video transcript.
2. **Writer Agent** takes that research report and crafts an engaging, well-structured blog post summarizing the video content.
3. The final blog post is saved automatically to `new-blog-post.md`.

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Agent Orchestration | CrewAI |
| LLM | Gemini 2.5 Flash (via `langchain_google_genai`) |
| Tooling | CrewAI Tools (`YoutubeChannelSearchTool`) |
| Language | Python |
| Config Management | python-dotenv |

## 📂 Project Structure

```
├── main.py              # Entry point — sets up LLM, agents, tasks, and crew
├── agents.py            # Agent definitions (Researcher, Writer)
├── tasks.py             # Task definitions for each agent
├── tools.py             # YouTube channel search tool configuration
├── .env                 # API keys (not committed)
└── new-blog-post.md     # Generated output (created at runtime)
```

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install dependencies**
   ```bash
   pip install crewai crewai-tools langchain-google-genai python-dotenv
   ```

3. **Configure environment variables**

   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Run the pipeline**
   ```bash
   python main.py
   ```

## 🔧 Configuration

- **YouTube Channel**: Update the `youtube_channel_handle` parameter in the tool setup to target a different channel.
- **Topic**: Pass a custom topic via the `inputs` dictionary in `crew.kickoff()`.
- **Model Temperature**: Adjust `temperature` in the `ChatGoogleGenerativeAI` setup to control creativity vs. factual accuracy.
- **Rate Limiting**: Modify `max_rpm` in the `Crew` configuration to control API request throughput.

## 📌 Example Usage

```python
result = crew.kickoff(
    inputs={"topic": "AI vs ML vs DL vs Data Science"}
)
print(result)
```

This generates a structured blog post based on relevant videos from the configured YouTube channel and saves it to `new-blog-post.md`.

## 📄 License

This project is open source and available for personal and educational use.

## 👤 Author

**Sufiyan Sikander**
AI Engineer
[GitHub](#) • [LinkedIn](#) • [Portfolio](#)
