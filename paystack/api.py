import frappe
import requests


@frappe.whitelist(allow_guest=True)
def initialize_transaction(courseId, userEmail):
    url = "https://api.paystack.co/transaction/initialize"
    authorization = "Bearer sk_test_bdbc4fa530cb80cf0055f2554a14b92d99331e4f"
    content_type = "application/json"

    # Example usage
    user_email = userEmail
    course_id = courseId  # Replace with the actual course ID

    if not course_id or not user_email:
        frappe.throw(("Course ID and User Email are required."), title=("Invalid Input"))

    data = {
        "email": user_email,
        "amount": 20000 *100,  # Replace with the actual amount for the course
        "metadata": {
            "course_id": course_id,
            "user_email": user_email
        }
    }

    headers = {
        "Authorization": authorization,
        "Content-Type": content_type
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raises an exception for 4xx and 5xx status codes
        response_data = response.json()  # Get the JSON data from the response
        return response_data  # Return the JSON data directly
    except requests.exceptions.RequestException as e:
        print("Error initializing transaction:", e)
        return {"status": "error", "message": str(e)}
