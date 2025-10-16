# 🤝 Contributing to TaskPilot

First off, thank you for considering contributing to TaskPilot! We're excited to build a community-driven automation platform, and your help is essential.

This document provides guidelines for contributing to the project, whether it's reporting a bug, proposing a new feature, or writing code.

## Code of Conduct

This project and everyone participating in it is governed by a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior.

## How Can I Contribute?

### 🐛 Reporting Bugs

If you find a bug, please make sure it hasn't already been reported by searching the GitHub Issues. If you can't find an open issue addressing the problem, please [open a new one](https://github.com/your-username/TaskPilot/issues/new).

When you are creating a bug report, please include as many details as possible:
*   A clear and descriptive title.
*   A description of the steps to reproduce the bug.
*   The expected behavior and what happened instead.
*   Your operating system, Docker version, and any other relevant environment details.

### ✨ Suggesting Enhancements

If you have an idea for a new feature or an improvement to an existing one, we'd love to hear about it! Please check the [Project Roadmap](ROADMAP.md) first to see if your idea is already planned.

If not, please [open a new issue](https://github.com/your-username/TaskPilot/issues/new) to start a discussion. This allows us to coordinate our efforts and prevent duplication of work.

### 🔌 Creating a New Connector

Connectors are the heart of TaskPilot! If you want to create a new connector, please follow these steps:
1.  **Open an issue** to propose the new connector and discuss its scope (triggers and actions).
2.  Create a new directory under `backend/connectors/your_connector_name/`.
3.  Create a `connector.py` file inside that directory.
4.  Your new connector class must inherit from `BaseConnector` and implement the required `trigger` and `action` methods.
5.  Add any new dependencies to `requirements.txt`.
6.  (Optional but recommended) Add a new entry to the `availableConnectors` object in `frontend/src/components/FlowForm.js` to make it selectable in the UI.

### 💻 Pull Request Process

1.  Fork the repository and create your branch from `main`.
2.  Make your changes, ensuring your code follows the project's style.
3.  Add or update documentation as needed.
4.  Ensure your code is tested. (We are working on a formal testing framework).
5.  Submit a pull request with a clear description of the changes.

---

We look forward to your contributions!