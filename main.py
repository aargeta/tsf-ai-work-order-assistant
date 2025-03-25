import os
from dotenv import load_dotenv
from utils.openai_api import extract_work_order_data, generate_response_email
from utils.sheets import log_work_order  # ← Add this line

# Load environment variables from .env
load_dotenv()

def main():
    print("🔧 TSF AI Work Order Assistant is running...")

    # Sample placeholder email body (replace this with actual email fetching)
    sample_email = """
    Hello, I need a technician for the following:
    Client Name: TSF
    Project Name: TSFTest
    Project Location: Tampa, FL
    Site Contact: Tyler Gorman
    Site Contact Phone: 813-777-6425
    Test Type: AI Test
    Task Description: Please test this automation
    Requested Time/Date: 3/28/2025 - 10:00 AM
    Special Instructions: Let's see if we can automate this.
    """

    # Step 1: Extract work order data from the email
    extracted_data = extract_work_order_data(sample_email)
    print("\n📋 Extracted Work Order Data:")
    print(extracted_data)

    # Step 2: Generate email response
    response = generate_response_email(extracted_data)
    print("\n✉️ Suggested Email Reply:")
    print(response)

    # Step 3: Log to Google Sheets
    log_work_order(extracted_data)

if __name__ == "__main__":
    main()
