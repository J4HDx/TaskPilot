import time
from playwright.sync_api import sync_playwright, Page, expect

def verify_dashboard(page: Page):
    """
    Verifies that the main dashboard of TaskPilot loads correctly.
    """
    # Navigate to the frontend application
    page.goto("http://localhost:3000")

    # Wait for the main header to be visible
    header = page.get_by_role("heading", name="TaskPilot Dashboard")
    expect(header).to_be_visible()

    # Wait for the "My Flows" section to appear
    my_flows_header = page.get_by_role("heading", name="My Flows")
    expect(my_flows_header).to_be_visible()

    # Wait for the "Create New Flow" form to appear
    create_flow_header = page.get_by_role("heading", name="Create New Flow")
    expect(create_flow_header).to_be_visible()

    # Give the page a moment to settle visually
    time.sleep(2)

    # Take a screenshot of the dashboard
    page.screenshot(path="jules-scratch/verification/verification.png")
    print("Screenshot taken and saved to jules-scratch/verification/verification.png")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        verify_dashboard(page)
        browser.close()

if __name__ == "__main__":
    main()