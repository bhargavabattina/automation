
import datetime
import pytest
import os
import requests
import json
import time
import allure
from playwright.sync_api import sync_playwright, Page

import cloudscraper

# Report directory configuration
REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)

# Allure results directory
ALLURE_RESULTS_DIR = "allure-results"
ALLURE_REPORT_DIR = "allure-report"

# Microsoft Teams webhook URL
TEAMS_WEBHOOK_URL = "https://srslivetech.webhook.office.com/webhookb2/e16c66cb-8396-4759-befc-8d4462ee1d31@4f1f5a9f-f6a8-4bc9-a157-7fddfe22b5f6/IncomingWebhook/60bfc1d3c89d4f72bdc44e674ee9b38d/3e17875b-b12b-400d-adc2-eefc03796a3a/V27HSL3GH65e9-gmNmRADasY76FK4I1nYMKvpJylj74RE1"


@pytest.fixture(scope="function")
def browser():
    """Fixture to launch the browser, bypass Cloudflare, and create a new context"""
    with sync_playwright() as p:
        #browser = p.chromium.launch(headless=False, slow_mo=300)
        browser = p.chromium.launch()
        # Create video directory
        video_dir = "videos/"
        if not os.path.exists(video_dir):
            os.makedirs(video_dir, exist_ok=True)
        print(f"🎥 Video directory: {os.path.abspath(video_dir)}")
        context = browser.new_context(record_video_dir=video_dir)
        yield context  # Provide the context for tests

        context.close()
        browser.close()


@pytest.fixture
def page(browser):
    """Fixture to initialize the Client Test Page with Cloudflare bypass"""
    page = browser.new_page()

    page.goto("https://settlepaisa-internal.sabpaisa.in/sign-in")
    yield page

    page.close()


@pytest.fixture
def page_with_screenshot(page, request):
    """Fixture to capture screenshots and attach videos to Allure"""
    yield page  # Allow test execution

    # Get test report from request
    outcome = request.node.__dict__.get("test_outcome", None)
    screenshot_name = "Pass Screenshot" if outcome == "passed" else "Fail Screenshot"

    # Capture and attach screenshot
    allure.attach(
        page.screenshot(full_page=True),
        name=screenshot_name,
        attachment_type=allure.attachment_type.PNG,
    )

    # **Ensure page is closed before accessing the video**
    page.close()
    time.sleep(2)

    # Capture video (ensure the page is closed before accessing `video.path()`)
    if page.video:
        video_path = page.video.path()
        allure.attach.file(video_path, name="Test Execution Video", attachment_type=allure.attachment_type.WEBM)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test status and store it in request.node"""
    outcome = yield
    report = outcome.get_result()
    item.__dict__["test_outcome"] = report.outcome  # Store the test outcome in the request object

# # Report directory configuration
# REPORT_DIR = "reports"
# os.makedirs(REPORT_DIR, exist_ok=True)
#
# # Teams webhook URL
# TEAMS_WEBHOOK_URL = "https://srslivetech.webhook.office.com/webhookb2/e16c66cb-8396-4759-befc-8d4462ee1d31@4f1f5a9f-f6a8-4bc9-a157-7fddfe22b5f6/IncomingWebhook/60bfc1d3c89d4f72bdc44e674ee9b38d/3e17875b-b12b-400d-adc2-eefc03796a3a/V27HSL3GH65e9-gmNmRADasY76FK4I1nYMKvpJylj74RE1"  # Replace with your actual URL
#
# @pytest.fixture(scope="session")  # Changed to session scope for one report and notification
# def generate_html_report():
#     results = []
#
#     def _generate_report(test_results):
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#         report_filename = os.path.join(REPORT_DIR, f"test_report_{timestamp}.html")
#
#         with open(report_filename, "w") as file:
#             # ... (HTML report generation code - same as before) ...
#             print(f"HTML report generated: {report_filename}")
#
#         # Send notification to Teams after report generation
#         try:
#             message = {
#                 "text": f"Test report generated: {report_filename}. Check the {REPORT_DIR} folder."
#             }
#             headers = {"Content-Type": "application/json"}
#             response = requests.post(TEAMS_WEBHOOK_URL, data=json.dumps(message), headers=headers)
#             if response.status_code == 200:
#                 print("Teams notification sent successfully!")
#             else:
#                 print(f"Failed to send Teams notification. Status code: {response.status_code}")
#                 # Optionally log the error message for debugging:
#                 print(response.text) # Print the response from the server
#
#         except Exception as e:
#             print(f"Error sending Teams notification: {e}")
#
#
#     def add_result(test_name, status, error_message=""):
#         results.append((test_name, status, error_message))
#
#     yield _generate_report, add_result
#     _generate_report(results)  # Generate report *after* all tests are done (session scope)





# @pytest.hookimpl(trylast=True)
# def pytest_sessionfinish(session, exitstatus):
#     """Generate Allure report and send a webhook notification to Teams."""
#     print("📢 Generating Allure Report...")
#
#     # # Generate Allure report
#     # try:
#     #     subprocess.run(["allure", "generate", ALLURE_RESULTS_DIR, "-o", ALLURE_REPORT_DIR, "--clean"], check=True)
#     #     print("✅ Allure report generated successfully!")
#     # except subprocess.CalledProcessError as e:
#     #     print(f"❌ Failed to generate Allure report: {e}")
#     #     return
#
#     # Prepare and send webhook notification
#     report_url = "https://bhargavabattina.github.io/automation/allure-report/index.html"  # Local report URL
#
#     try:
#         message = {
#             "text": f"✅ Test Execution Completed!\n\n📊 **Payment Gateway Test Report:** [View Report]({report_url})"
#         }
#         headers = {"Content-Type": "application/json"}
#         response = requests.post(TEAMS_WEBHOOK_URL, data=json.dumps(message), headers=headers)
#
#         if response.status_code == 200:
#             print("📩 Teams notification sent successfully!")
#         else:
#             print(f"❌ Failed to send Teams notification. Status code: {response.status_code}")
#             print(response.text)
#
#     except Exception as e:
#         print(f"❌ Error sending Teams notification: {e}")
