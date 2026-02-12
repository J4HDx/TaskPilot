import httpx
from typing import Any, Dict, List

from ..base import BaseConnector
from ...core.config import settings

class TelegramConnector(BaseConnector):
    """
    Connector for Telegram to send messages.
    """

    def __init__(self, config: Dict[str, Any] = {}):
        """
        Initializes the Telegram connector.
        The bot token is read from the global settings.
        """
        super().__init__(config)
        self.bot_token = settings.TELEGRAM_BOT_TOKEN
        if not self.bot_token:
            # This check is important for when the connector is initialized.
            raise ValueError("TELEGRAM_BOT_TOKEN is not set in the environment.")
        self.api_url = f"https://api.telegram.org/bot{self.bot_token}"

    async def trigger(self, event: str, event_config: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Telegram triggers are not implemented in this version (e.g., listening for new messages).
        """
        # In the future, this could be implemented using webhooks.
        return []

    async def action(self, action: str, action_config: Dict[str, Any], data: Dict[str, Any] = {}):
        """
        Executes an action, such as sending a message.

        Args:
            action (str): The name of the action to perform (e.g., "send_message").
            action_config (dict): Configuration for the action.
                                  Expected keys: "chat_id", "text".
            data (dict): Data from the trigger, can be used to format the message.
        """
        if action != "send_message":
            raise ValueError(f"Unsupported Telegram action: {action}")

        # Use chat_id from config, or fall back to the global one from .env
        chat_id = action_config.get("chat_id") or settings.TELEGRAM_CHAT_ID
        text_template = action_config.get("text")

        if not chat_id or not text_template:
            raise ValueError("Missing 'chat_id' or 'text' in action_config for Telegram.")

        # Simple templating to insert trigger data into the message
        # Example: "New email from {from} with subject: {subject}"
        try:
            text_to_send = text_template.format(**data)
        except KeyError as e:
            print(f"Warning: Key {e} not found in trigger data for templating. Sending raw text.")
            text_to_send = text_template


        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.api_url}/sendMessage",
                    json={"chat_id": chat_id, "text": text_to_send},
                )
                response.raise_for_status()
                print(f"Message sent to Telegram chat {chat_id}")
            except httpx.HTTPStatusError as e:
                print(f"Error sending message to Telegram: {e.response.text}")
                raise
            except Exception as e:
                print(f"An unexpected error occurred while sending message to Telegram: {e}")
                raise