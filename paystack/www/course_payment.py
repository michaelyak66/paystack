# course_payment.py
import frappe
from frappe import _

def get_context(context):
    # Fetch the list of courses using the custom function
    course_list = get_course_list()

    # Pass the list of courses to the template
    context.courses = course_list

    # Other context data if needed
    # ...
    
def get_course_list():
    courses = frappe.get_all("LMS Course", fields=["title", "image", "description", "name"])
    return courses

