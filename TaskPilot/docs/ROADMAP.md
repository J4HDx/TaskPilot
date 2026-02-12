# 🗺️ TaskPilot Project Roadmap

This document outlines the planned features and improvements for future versions of TaskPilot. Our goal is to build a powerful, flexible, and community-driven automation platform.

---

### 🚀 Version 1.1 (Quality of Life & Expansion)

*   [ ] Advanced Visual Editor: Transition from simple forms to a drag-and-drop canvas interface (using a library like React Flow) for a more intuitive flow creation experience.
*   [ ] More Connectors:
    *   [ ] Discord (Actions & Triggers)
    *   [ ] Google Drive (Actions)
    *   [ ] Twitter (Triggers)
*   [ ] User-Managed Credentials: Implement a secure way for users to add and manage their service credentials (API keys, etc.) directly from the frontend.
*   [ ] Enhanced Logging: More detailed and searchable logs with better filtering options.
*   [ ] Testing Framework: Introduce a dedicated testing framework for connectors to ensure reliability.

---

### 📦 Version 2.0 (Maturity & Scalability)

*   [ ] Full User Authentication:
    *   [ ] Implement a complete user authentication system with JWT (login, registration, password recovery).
    *   [ ] Introduce multi-tenancy, allowing multiple users to manage their own flows securely.
*   [ ] OAuth2 for Connectors: Implement OAuth2 for services that support it (like Google, GitHub, etc.) to provide a more secure and user-friendly connection experience.
*   [ ] Webhook Triggers: Introduce support for webhook-based triggers for real-time notifications from external services.
*   [ ] Connector Marketplace:
    *   [ ] Develop a system where the community can submit, share, and install new connectors.
    *   [ ] Create a simple CLI tool to help developers bootstrap new connectors.
*   [ ] Database Migration: Migrate from SQLite to a more robust database solution like **MongoDB** or **PostgreSQL** to handle larger loads and more complex data.

---

### 🧠 Version 3.0 and Beyond (Intelligence & Ecosystem)

*   [ ] AI-Powered Suggestions: Integrate AI to suggest useful flows based on the user's connected services or common patterns.
*   [ ] Multi-Step Flows: Allow flows with more than one action (e.g., Trigger -> Action 1 -> Action 2).
*   [ ] Conditional Logic: Add conditional logic (if/else, filters) within flows.
*   [ ] OpenAgent Integration: Explore integration with OpenAgent for more complex, AI-driven task execution.
*   [ ] Enterprise Features:
    *   [ ] Role-Based Access Control (RBAC).
    *   [ ] Audit Logs.
    *   [ ] High-availability deployment options.

---

We welcome community feedback and contributions to help shape this roadmap!