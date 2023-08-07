import frappe

@frappe.whitelist(allow_guest=True)
def sign_up():
    # create a new document
    doc = frappe.new_doc('Task')
    doc.subject = 'New Task 2'
    doc.insert(ignore_permissions=True)
    doc.save(
    ignore_permissions=True, # ignore write permissions during insert
    ignore_version=True # do not create a version record
    )



def test():
    # create a new document
    doc = frappe.get_doc({
        'doctype': 'Task',
        'title': 'New Task',
        "subject": "Test Task",
    })
    doc.insert(ignore_permissions=True)
    doc.submit()


