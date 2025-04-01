import time
import pytest
import allure
from pageObjects.loginpage import LoginPage


@allure.epic("Settle Paisa")
@allure.feature("Authentication")
class TestLoginValidation:
    """Test class for Client Validation scenarios."""

    @allure.story("Login Function Validations")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Correct Login Credentials Validation")
    @pytest.mark.ui
    @pytest.mark.critical
    def test_correct_login(self, page_with_screenshot):
        """Test Payer Name Field Validation"""
        login_page = LoginPage(page_with_screenshot)
        try:
            with allure.step("Filling Username"):
                login_page.fill_email("bala.subrahmanyam@sabpaisa.in")

            with allure.step("Filling Password"):
                login_page.fill_password("Bala@123")

            with allure.step("Clicking Login Button"):
                login_page.click_login()

            with allure.step("Verifying Dashboard "):
                expected_error_message = "Dashboard"
                actual_error_message = login_page.get_valid_message_text()
                assert expected_error_message in actual_error_message, "Error message text is incorrect"

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.story("Login Function Validations")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Wrong Login Credentials Validation")
    @pytest.mark.ui
    @pytest.mark.critical
    def test_wrong_login(self, page_with_screenshot):
        """Test Payer Name Field Validation"""
        login_page = LoginPage(page_with_screenshot)
        try:
            with allure.step("Filling Username"):
                login_page.fill_email("bala.subrahmanyam@sabpaisa.in")

            with allure.step("Filling Password"):
                login_page.fill_password("Bal")

            with allure.step("Clicking Login Button"):
                login_page.click_login()

            with allure.step("Verifying Dashboard "):
                expected_text = "Dashboard"

                try:
                    actual_text = login_page.get_valid_message_text()
                    assert expected_text == actual_text, f"Expected '{expected_text}', but got '{actual_text}'"
                except AssertionError as e:
                    pytest.fail(f"Test failed: {str(e)}")  # Fails test if element is missing or text is incorrect

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            raise

