<a id="readme-top"></a>

<div align="center">

  <h1>Task Manager CLI</h1>

  <p>
    A simple and lightweight command-line task manager — runs fully inside Docker, no Python setup needed.
    <br />
    <a href="https://github.com/jamsshid/cli-task-tracker/issues/new?labels=bug">Report Bug</a>
    &middot;
    <a href="https://github.com/jamsshid/cli-task-tracker/issues/new?labels=enhancement">Request Feature</a>
  </p>

  [![Python][python-shield]][python-url]
  [![Docker][docker-shield]][docker-url]
  [![MIT License][license-shield]][license-url]

</div>

---

## Table of Contents

<details>
  <summary>Click to expand</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#error-handling">Error Handling</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

---

## About The Project

Task Manager CLI is a minimal task tracker that runs entirely inside a Docker container. You can add, update, delete, and list tasks — all from PowerShell, with no Python installation required on your machine.

**Why this project?**

- Practice building CLI tools with Python
- Learn how to containerize a simple app with Docker
- Persistent local storage via a mounted volume

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Built With

[![Python][python-shield]][python-url]
[![Docker][docker-shield]][docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- Windows PowerShell

### Installation

1. Clone the repository

   ```powershell
   git clone https://github.com/jamsshid/cli-task-tracker.git
   cd cli-task-tracker
   ```

2. Build the Docker image

   ```powershell
   docker build -t task-cli .
   ```

3. Set up the `task` shortcut function in PowerShell

   ```powershell
   function task { docker run --rm -v "$(pwd)/data:/app/data" task-cli @args }
   ```

   > Add this line to your `$PROFILE` file to make it permanent across all PowerShell sessions.

That's it — no need to create a `data/` folder manually. Docker handles it automatically.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Usage

> All commands use the `task` shortcut. If you haven't set it up, replace `task` with:
> `docker run --rm -v "$(pwd)/data:/app/data" task-cli`

Your tasks are saved in `data/tasks.json` and persist between runs.

---

### Add a task

New tasks are automatically assigned an ID and start with `todo` status.

```powershell
task add "Buy coffee"
```

```
Task added succesfully! ID: 1
```

---

### Update a task

```powershell
task update 1 "Buy cappuccino"
```

```
Task 1 updated.
```

---

### Change status

Accepted values: `todo`, `in-progress`, `done`

```powershell
task status 1 done
```

```
Task 1 status marked as done.
```

---

### List all tasks

```powershell
task list
```

```
ID    Status      Created                   Updated                   Description
----------------------------------------------------------------------------------
1     done        01/06/2024, 08:00:00      01/06/2024, 09:15:00      Buy cappuccino
2     in-progress 01/06/2024, 09:00:00      01/06/2024, 10:02:33      Write unit tests
3     todo        01/06/2024, 08:45:00      01/06/2024, 08:45:00      Update README
```

---

### Filter by status

```powershell
task list todo
```

```
ID    Status   Created                   Updated                   Description
---------------------------------------------------------------------------
3     todo     01/06/2024, 08:45:00      01/06/2024, 08:45:00      Update README
```

---

### Delete a task

```powershell
task delete 1
```

```
Task 1 deleted.
```

---

### Show help

```powershell
task
```

```
Usage: task [command] [arguments]

The commands: add, update, status, list, delete

Examples:
- Add a task:          task add "Buy coffee"
- Update a task:       task update 1 "Buy cappuccino"
- Change status:       task status 1 done
- List all tasks:      task list
- Filter by status:    task list todo
- Delete a task:       task delete 1
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Error Handling

| Situation | Message |
|---|---|
| Task ID not found | `Error: 99 not found` |
| Invalid command or missing arguments | `Invalid command or missing arguments.` |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Project Structure

```
cli-task-tracker/
├── task.py          # CLI script
├── Dockerfile       # Docker image configuration
├── .dockerignore    # Files excluded from the Docker image
├── .gitignore       # Files excluded from Git
└── README.md
```

> `data/tasks.json` is created automatically on first use and is excluded from Git.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Roadmap

- [x] Add, update, delete tasks
- [x] Change task status
- [x] Filter tasks by status
- [x] Docker support
- [ ] Due dates for tasks
- [ ] Priority levels (low, medium, high)
- [ ] Export tasks to CSV


<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contributing

Contributions are welcome! If you have a suggestion, please fork the repo and create a pull request, or open an issue with the tag `enhancement`.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Acknowledgments

- [roadmap.sh — Task Tracker Project](https://roadmap.sh/projects/task-tracker)
- [Docker Documentation](https://docs.docker.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- SHIELDS -->
[python-shield]: https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[docker-shield]: https://img.shields.io/badge/Docker-ready-2496ED?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/
[license-shield]: https://img.shields.io/badge/License-MIT-green?style=for-the-badge
[license-url]: https://github.com/jamsshid/cli_task_tracker/blob/main/LICENSE