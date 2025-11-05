import datetime
import uuid
from typing import Any, Dict, List

from ..base import BaseConnector
from ...core.config import settings

# In-memory store to keep track of processed email IDs for this session
# This is a simple solution for the MVP. In a real scenario, you'd use a
# persistent store (like Redis or a database) to avoid reprocessing emails
# after a server restart.
processed_email_ids = set()

class GmailConnector(BaseConnector):
    """
    Connector for Gmail to check for new emails.

    NOTE: For the MVP, this connector SIMULATES checking emails with mock data.
    A real implementation requires OAuth2, which is planned for a future version.
    """

    def __init__(self, config: Dict[str, Any] = {}):
        """
        Initializes the Gmail connector.
        """
        super().__init__(config)
        # In a real scenario, you would initialize the Gmail API client here
        # using credentials stored securely.
        # e.g., self.service = build('gmail', 'v1', credentials=...)

    async def trigger(self, event: str, event_config: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Checks for new emails based on specified criteria.

        Args:
            event (str): The name of the event (e.g., "new_email").
            event_config (dict): Configuration for the trigger.
                                 Expected keys: "subject_contains", "from_address".

        Returns:
            A list of dictionaries, where each dictionary represents a new email.
        """
        if event != "new_email":
            raise ValueError(f"Unsupported Gmail event: {event}")

        print("Checking for new Gmail emails (mock implementation)...")

        # --- MOCK DATA ---
        # This simulates a new email appearing that matches the criteria.
        # A unique ID is generated each time to ensure it's processed.
        mock_emails = [
            {
                "id": f"email_{uuid.uuid4()}",
                "subject": "Your monthly invoice is here",
                "from": "billing@example.com",
                "body": "Please find your invoice attached.",
                "received_at": datetime.datetime.now().isoformat()
            },
            {
                "id": f"email_{uuid.uuid4()}",
                "subject": "Project Update",
                "from": "team@example.com",
                "body": "Here is the latest update on the project.",
                "received_at": datetime.datetime.now().isoformat()
            }
        ]
        # --- END MOCK DATA ---

        new_events = []
        subject_filter = event_config.get("subject_contains", "").lower()
        from_filter = event_config.get("from_address", "").lower()

        for email in mock_emails:
            if email["id"] in processed_email_ids:
                continue

            match_subject = subject_filter in email["subject"].lower() if subject_filter else True
            match_from = from_filter in email["from"].lower() if from_filter else True

            if match_subject and match_from:
                new_events.append(email)
                # Mark as processed so it's not picked up again in the same session
                processed_email_ids.add(email["id"])

        if new_events:
            print(f"Found {len(new_events)} new emails matching criteria.")

        return new_events

    async def action(self, action: str, action_config: Dict[str, Any], data: Dict[str, Any] = {}):
        """
        Gmail actions (e.g., send email) are not implemented in this version.
        """
        print(f"Gmail action '{action}' is not yet implemented.")
        return