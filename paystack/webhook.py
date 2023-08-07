import frappe
import requests
import urllib.parse


@frappe.whitelist(allow_guest=True)
def webhook():
    try:
        data = frappe.request.get_json()
        print(data)
        
        payment_status = data['data']['status']
        customer_email = data['data']['metadata']['user_email']
        course_name = data['data']['metadata']['course_id']
        
        if payment_status == "success":
            enroll_user_in_course(customer_email, course_name)
            return {
                "status": "success",
                "message": "User enrolled successfully."
            }
        else:
            return {
                "status": "error",
                "message": "Payment not successful."
            }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


def enroll_user_in_course(customer_email, course_name):
    url = f"http://127.0.0.1:8008/api/resource/LMS Batch Membership"
    headers = {
        "Authorization": "token 52791821ca87b22:7dec8c41da44e8e",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    # URL encode the course_name
    course_name = urllib.parse.quote(course_name)

    
    data = {
            "course": course_name,
            "member": customer_email
        }

    try:
        response = requests.post(url, headers=headers, json=data)
        print(response)
        if response.status_code == 200 and response.json().get("data"):
            return {
                "status": "success",
                "message": "enrolled successfully."
            }
        else:
            return {
                "status": "error",
                "message": response.json().get("message") or "Failed to enroll."
            }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
