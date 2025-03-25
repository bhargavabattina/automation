import time

import pytest
import allure
from pageObjects.Client_test import ClientTest


@allure.epic("Payment Gateway")
@allure.feature("Error Message Validations")
class TestClientValidation:
    """Test class for Client Validation scenarios."""

    @allure.story("Payer Name Validations")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Test Empty Payer Name Validation")
    @pytest.mark.ui
    @pytest.mark.critical
    def test_empty_payer_name_validation(self, page_with_screenshot: ClientTest):
        """Test Payer Name Field Validation"""
        try:
            with allure.step("Filling Client Code"):
                page_with_screenshot.fill_client_code("LPSD1")


            with allure.step("Selecting Environment"):
                page_with_screenshot.select_environment("STAGING")

            with allure.step("Clicking Show Detail"):
                page_with_screenshot.click_show_detail()

            with allure.step("Entering Payment Details"):
                page_with_screenshot.fill_amount("10")
                page_with_screenshot.fill_contact("1234567890")
                page_with_screenshot.fill_email("wI9oX@example.com")

            with allure.step("Clicking Pay Button"):
                page_with_screenshot.click_pay()

            with allure.step("Verifying Error Message"):
                expected_error_message = "Error : Payer name is not passed correctly in the payment request."
                actual_error_message = page_with_screenshot.get_error_message_text()
                assert expected_error_message in actual_error_message, "Error message text is incorrect"

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            raise

    # @allure.story("Payer Name Validations")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title("Test Correct Payer Name Validation")
    # @pytest.mark.ui
    # @pytest.mark.critical
    # def test_payer_name_validation(self, page_with_screenshot: ClientTest):
    #     """Test Payer Name Field Validation"""
    #     try:
    #         with allure.step("Filling Client Code"):
    #             page_with_screenshot.fill_client_code("TM001")
    #
    #         with allure.step("Selecting Environment"):
    #             page_with_screenshot.select_environment("STAGING")
    #
    #         with allure.step("Clicking Show Detail"):
    #             page_with_screenshot.click_show_detail()
    #
    #         with allure.step("Entering Payment Details"):
    #             page_with_screenshot.fill_first_name("Bhargav")
    #             page_with_screenshot.fill_amount("10")
    #             page_with_screenshot.fill_contact("1234567890")
    #             page_with_screenshot.fill_email("wI9oX@example.com")
    #
    #         with allure.step("Clicking Pay Button"):
    #             page_with_screenshot.click_pay()
    #
    #         with allure.step("Verifying Error Message"):
    #             expected_error_message = "Bhargav"
    #             actual_error_message = page_with_screenshot.get_name_text()
    #             assert expected_error_message in actual_error_message, "Error message text is incorrect"
    #
    #     except Exception as e:
    #         allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
    #         raise
    #
    # @allure.story("Payer Name Validations")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title("Test Payer Name Special Character Allow")
    # @pytest.mark.ui
    # @pytest.mark.critical
    # def test_payer_name_spca_validation(self, page_with_screenshot: ClientTest):
    #     """Test Payer Name Field Validation"""
    #     try:
    #         with allure.step("Filling Client Code"):
    #             page_with_screenshot.fill_client_code("TM001")
    #
    #         with allure.step("Selecting Environment"):
    #             page_with_screenshot.select_environment("STAGING")
    #
    #         with allure.step("Clicking Show Detail"):
    #             page_with_screenshot.click_show_detail()
    #
    #         with allure.step("Entering Payment Details"):
    #             page_with_screenshot.fill_first_name("Bhargav@b")
    #             page_with_screenshot.fill_amount("10")
    #             page_with_screenshot.fill_contact("1234567890")
    #             page_with_screenshot.fill_email("wI9oX@example.com")
    #
    #         with allure.step("Clicking Pay Button"):
    #             page_with_screenshot.click_pay()
    #
    #         with allure.step("Verifying Error Message"):
    #             expected_error_message = "Bhargav@b"
    #             actual_error_message = page_with_screenshot.get_name_text()
    #             assert expected_error_message in actual_error_message, "Error message text is incorrect"
    #
    #     except Exception as e:
    #         allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
    #         raise
    #
    # @allure.story("Payer Name Validations")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title("Test Payer Name Special Character NotAllow Validation")
    # @pytest.mark.ui
    # @pytest.mark.critical
    # def test_empty_payer_name_span_validation(self, page_with_screenshot: ClientTest):
    #     """Test Payer Name Field Validation"""
    #     try:
    #         with allure.step("Filling Client Code"):
    #             page_with_screenshot.fill_client_code("DJ031")
    #
    #         with allure.step("Selecting Environment"):
    #             page_with_screenshot.select_environment("STAGING")
    #
    #         with allure.step("Clicking Show Detail"):
    #             page_with_screenshot.click_show_detail()
    #
    #         with allure.step("Entering Payment Details"):
    #             page_with_screenshot.fill_first_name("Bhargav@b")
    #             page_with_screenshot.fill_amount("10")
    #             page_with_screenshot.fill_contact("1234567890")
    #             page_with_screenshot.fill_email("wI9oX@example.com")
    #
    #         with allure.step("Clicking Pay Button"):
    #             page_with_screenshot.click_pay()
    #
    #         with allure.step("Verifying Error Message"):
    #             expected_error_message = "Error : Payer name is not passed correctly in the payment request."
    #             actual_error_message = page_with_screenshot.get_error_message_text()
    #             assert expected_error_message in actual_error_message, "Error message text is incorrect"
    #
    #     except Exception as e:
    #         allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
    #         raise
    #
    # @allure.story("Client Code Validation")
    # @allure.severity(allure.severity_level.NORMAL)
    # @allure.title("Test Wrong Client Code Validation")
    # @pytest.mark.ui
    # @pytest.mark.regression
    # def test_worng_client_code_validation(self, page_with_screenshot: ClientTest):
    #     """Test Client Code Field Validation"""
    #     try:
    #         with allure.step("Filling Client Code"):
    #             page_with_screenshot.fill_client_code("LPSD1")
    #
    #         with allure.step("Selecting Environment"):
    #             page_with_screenshot.select_environment("STAGING")
    #
    #         with allure.step("Clicking Show Detail"):
    #             page_with_screenshot.click_show_detail()
    #
    #         with allure.step("Entering Invalid Client Code"):
    #             page_with_screenshot.enter_client_code("ff")
    #
    #         with allure.step("Filling User Details"):
    #             page_with_screenshot.fill_first_name("Bhargav")
    #             page_with_screenshot.fill_amount("10")
    #             page_with_screenshot.fill_contact("1234567890")
    #             page_with_screenshot.fill_email("wI9oX@example.com")
    #
    #         with allure.step("Clicking Pay Button"):
    #             page_with_screenshot.click_pay()
    #
    #         with allure.step("Verifying Error Message"):
    #             expected_error_message = "You are not passing a valid Client Code in the payment request. Please check.."
    #             actual_error_message = page_with_screenshot.get_error_message_text()
    #             assert expected_error_message in actual_error_message, "Error message text is incorrect"
    #
    #     except Exception as e:
    #         allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
    #         raise
    #
    # @allure.story("Client Code Validation")
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.title("Test Correct Client Code Validation")
    # @pytest.mark.ui
    # @pytest.mark.critical
    # def test_correct_client_validation(self, page_with_screenshot: ClientTest):
    #     """Test Payer Name Field Validation"""
    #     try:
    #         with allure.step("Filling Client Code"):
    #             page_with_screenshot.fill_client_code("TM001")
    #
    #         with allure.step("Selecting Environment"):
    #             page_with_screenshot.select_environment("STAGING")
    #
    #         with allure.step("Clicking Show Detail"):
    #             page_with_screenshot.click_show_detail()
    #
    #         with allure.step("Entering Payment Details"):
    #             page_with_screenshot.fill_first_name("Bhargav")
    #             page_with_screenshot.fill_amount("10")
    #             page_with_screenshot.fill_contact("1234567890")
    #             page_with_screenshot.fill_email("wI9oX@example.com")
    #
    #         with allure.step("Clicking Pay Button"):
    #             page_with_screenshot.click_pay()
    #
    #         with allure.step("Verifying Error Message"):
    #             expected_error_message = "Bhargav"
    #             actual_error_message = page_with_screenshot.get_name_text()
    #             assert expected_error_message in actual_error_message, "Error message text is incorrect"
    #
    #     except Exception as e:
    #         allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
    #         raise
    #
    # @allure.story("Client Code Validation")
    # @allure.severity(allure.severity_level.NORMAL)
    # @allure.title("Test Empty Client Code Validation")
    # @pytest.mark.ui
    # @pytest.mark.regression
    # def test_empty_client_code_validation(self, page_with_screenshot: ClientTest):
    #     """Test Client Code Field Validation"""
    #     try:
    #         with allure.step("Filling Client Code"):
    #             page_with_screenshot.fill_client_code("TM001")
    #
    #         with allure.step("Selecting Environment"):
    #             page_with_screenshot.select_environment("STAGING")
    #
    #         with allure.step("Clicking Show Detail"):
    #             page_with_screenshot.click_show_detail()
    #
    #         with allure.step("Entering Invalid Client Code"):
    #             page_with_screenshot.enter_client_code("")
    #
    #         with allure.step("Filling User Details"):
    #             page_with_screenshot.fill_first_name("Bhargav")
    #             page_with_screenshot.fill_amount("10")
    #             page_with_screenshot.fill_contact("1234567890")
    #             page_with_screenshot.fill_email("wI9oX@example.com")
    #
    #         with allure.step("Clicking Pay Button"):
    #             page_with_screenshot.click_pay()
    #
    #         with allure.step("Verifying Error Message"):
    #             expected_error_message = "You are not passing a valid Client Code in the payment request. Please check.."
    #             actual_error_message = page_with_screenshot.get_error_message_text()
    #             assert expected_error_message in actual_error_message, "Error message text is incorrect"
    #
    #     except Exception as e:
    #         allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
    #         raise
    #
