app_name = "service"
app_title = "Service Management"
app_publisher = "www.ossph.com"
app_description = "Service Management"
app_icon = "icon-truck"
app_color = "orange"
app_email = "info@ossph.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/service/css/service.css"
# app_include_js = "/assets/service/js/service.js"

# include js, css files in header of web template
# web_include_css = "/assets/service/css/service.css"
# web_include_js = "/assets/service/js/service.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "service.install.before_install"
# after_install = "service.install.after_install"

# Calendar
calendars = ["Appointment"]

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "service.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"service.tasks.all"
# 	],
# 	"daily": [
# 		"service.tasks.daily"
# 	],
# 	"hourly": [
# 		"service.tasks.hourly"
# 	],
# 	"weekly": [
# 		"service.tasks.weekly"
# 	]
# 	"monthly": [
# 		"service.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "service.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.core.doctype.event.event.get_events": "service.event.get_events"
# }

