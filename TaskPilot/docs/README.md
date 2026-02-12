<div align="center">

```
  _____           _      ____  _           _
 |_   _|_ _ _ __ | | __ / ___|(_) __ _ ___| |_
   | |/ _` | '_ \| |/ / \___ \| |/ _` / __| __|
   | | (_| | | | |   <   ___) | | (_| \__ \ |_
   |_|\__,_|_| |_|_|\_\ |____/|_|\__,_|___/\__|

```

**TaskPilot: Your Open-Source Automation Companion**

</div>

---

**TaskPilot** is a free, open-source, and self-hostable automation platform designed to be a simple, fast, and customizable alternative to services like Zapier or Make. It allows you to connect different applications and automate workflows using a simple "If This, Then That" logic.

> "If a new email with 'invoice' arrives in Gmail → save the attachment to Google Drive."

> "If someone mentions you on Twitter → send a notification to your Telegram."

Built with a modular architecture, TaskPilot is designed for developers and tech enthusiasts who want full control over their automations.

## 🚀 Key Features (MVP v1.0.0)

*   **Simple Flow Management:** Easily create, view, edit, and delete automation flows.
*   **Reliable Execution:** Automatic trigger-to-action execution powered by a robust backend.
*   **RESTful API:** A fully functional API built with FastAPI for managing your flows.
*   **Basic Logging:** Track the status and history of each flow execution.
*   **Initial Connectors:** Fully functional **Telegram** and **Gmail** connectors to get you started.
*   **Docker-Ready:** Comes with a `docker-compose.yml` for quick and easy setup.

## 🛠️ Installation & Setup

Get TaskPilot running on your local machine in just a few steps.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/TaskPilot.git
    cd TaskPilot
    ```

2.  **Configure Your Environment:**
    *   Create a `.env` file by copying the example:
        ```bash
        cp .env.example .env
        ```
    *   Open the `.env` file and add your credentials. At a minimum, you'll need a **Telegram Bot Token** and **Chat ID** to test the full example flow.
        ```env
        TELEGRAM_BOT_TOKEN=your_super_secret_token
        TELEGRAM_CHAT_ID=your_telegram_chat_id
        ```

3.  **Run with Docker Compose:**
    *   This is the recommended way to run TaskPilot. It starts the backend, frontend, and all necessary services.
        ```bash
        docker-compose up --build
        ```

4.  **Access the Application:**
    *   **Frontend Dashboard:** [http://localhost:3000](http://localhost:3000)
    *   **Backend API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

## 🧩 Example Flow: Get Telegram Alerts for New Invoices

Let's create a simple flow that sends a Telegram message whenever a new email with the word "invoice" in the subject arrives.

1.  **Navigate to the Dashboard:** Open your browser to [http://localhost:3000](http://localhost:3000).
2.  **Create a New Flow:**
    *   In the "Create New Flow" form, give your flow a name, like `Invoice Alert`.
    *   The **Trigger** (`Gmail: New Email`) and **Action** (`Telegram: Send Message`) are selected by default for the MVP.
    *   Click **Create Flow**.
3.  **See it in Action:**
    *   The Gmail trigger is currently simulated. Every 30 seconds, it will check for "new" emails.
    *   When it finds a mock email containing "invoice" in the subject, it will trigger the action.
    *   You will receive a message in your configured Telegram chat!

## 🤝 Contributing

We welcome contributions! Please read our `CONTRIBUTING.md` file to learn how you can help grow the TaskPilot ecosystem.

## 🗺️ Project Roadmap

Check out our `ROADMAP.md` to see what features are planned for future versions.

## 📄 License

This project is licensed under the MIT License.