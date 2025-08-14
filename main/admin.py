from django.contrib import admin

# For now, we'll just register Django's built-in models
# Later you can add your custom models here

# Example of how to customize admin
admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin Portal"
admin.site.index_title = "Welcome to Portfolio Administration"
