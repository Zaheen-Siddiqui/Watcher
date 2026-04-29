# Watcher

Watcher is a lightweight CLI-based dependency monitoring tool that helps developers track updates for frameworks, libraries, and packages. Users can add packages they want to monitor, check for new versions, and receive update notifications through the terminal or email.

## Features (Initial Phase)

- CLI-based package tracking  
- Add packages manually  
- Remove tracked packages  
- List all tracked packages  
- Check for latest versions  
- Show updates since last login  
- JSON import for package lists  
- Optional email notifications  
- Multi-user ready backend structure  

## Supported Ecosystems (Initial Phase)

- PyPI  
- npm  

More package registries may be added later.

## Tech Stack

### CLI
- Python  
- Typer or Click  

### Backend
- FastAPI  

### Database
- SQLite  

### Scheduler
- APScheduler  

### Email
- SMTP  

## Project Structure

```text
watcher/
├── watcher_cli/
├── server/
├── tests/
├── docs/
└── data/
```

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/watcher.git
cd watcher
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

Windows:

```powershell
venv\Scripts\activate
```

Linux or macOS:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Run the backend server

```bash
uvicorn server.app:app --reload
```

### Run the CLI

```bash
python -m watcher_cli.main
```

## Example Commands

```bash
watcher register
watcher login
watcher add react npm
watcher add numpy pypi
watcher list
watcher updates
watcher remove react
watcher import watchlist.json
watcher email on
```

## Current Status

Initial development phase.

## Working On

- Authentication
- Package tracking
- Version checking
- Update filtering
- Email alerts

## Roadmap

- package.json import
- requirements.txt import
- More ecosystems
- Better terminal UI
- Security alerts
- GitHub repository scanning

## Goal

Provide developers with a simple way to stay informed about dependency updates without needing a heavy dashboard.

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 PrintHub Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---
