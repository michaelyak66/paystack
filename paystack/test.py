import frappe
from frappe import _
import json

@frappe.whitelist(allow_guest=True)
def webhook():
    try:
        # Retrieve the JSON data sent by the webhook
        data = frappe.request.get_json()
        print(data)

        # Parse the JSON data
        data = json.loads(data)

        # Access specific information
        #payment_status = data['data']['status']
        #amount_paid = data['data']['amount']
        #currency = data['data']['currency']
        #payment_reference = data['data']['reference']
        customer_email = data['data']['customer']['email']
        #print(payment_status)


        # Check if the status field is "success"
        if payment_status == "sucess":
            # Assuming you have a function called enroll_user_by_email(email) for user enrollment
            enroll_user_by_email(customer_email)

        # Respond with a success message (status code 200) to acknowledge receipt
        return {"status": "success"}

    except Exception as e:
        # Handle any errors or exceptions that may occur during processing
        return {"status": "error", "message": str(e)}

def enroll_user_by_email(customer_email):
    try:
        # Check if the user with the given email already exists
        existing_user = frappe.get_doc("User", customer_email)

        if not existing_user:
            # Create a new user with the given email
            new_user = frappe.new_doc("User")
            new_user.email = customer_email
            new_user.first_name = "New"  # Replace with the desired first name
            new_user.insert(ignore_permissions=True)

        # Check if the course exists and retrieve its course ID
        course_id = "test"  # Replace with your function to get the course ID

        if not course_id:
            raise ValueError("Course not found")

        # Enroll the user in the course
        enrollment = frappe.new_doc("LMS Batch Meership")
        enrollment.course = course_id
        enrollment.member = customer_email
        enrollment.save(ignore_permissions=True)

        return {"status": "success"}

    except Exception as e:
        # Handle any errors or exceptions that may occur during user enrollment
        return {"status": "error", "message": str(e)}

def get_course_id(course_name):
    try:
        # Query the LMS Course document based on the course name
        course = frappe.get_doc("LMS Course", {"course_name": course_name})

        if course:
            return course.name
        else:
            return None

    except Exception as e:
        # Handle any errors or exceptions that may occur during the course lookup
        return None

