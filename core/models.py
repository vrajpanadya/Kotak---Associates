from django.db import models


class ContactMessage(models.Model):
    SERVICE_CHOICES = [
        ('', 'Select a service'),
        ('virtual_cfo', 'Virtual CFO Services'),
        ('tax_planning', 'Tax Planning & Compliance'),
        ('business_advisory', 'Business Advisory'),
        ('accounting', 'Accounting & Bookkeeping'),
        ('audit', 'Audit & Assurance'),
        ('gst', 'GST Compliance'),
        ('company_formation', 'Company Formation'),
        ('other', 'Other'),
    ]

    BUDGET_CHOICES = [
        ('', 'Select budget range'),
        ('below_25k', 'Below 25,000/month'),
        ('25k_50k', '25,000 - 50,000/month'),
        ('50k_1l', '50,000 - 1,00,000/month'),
        ('above_1l', 'Above 1,00,000/month'),
        ('discuss', 'Prefer to discuss'),
    ]

    URGENCY_CHOICES = [
        ('', 'Select timeline'),
        ('immediate', 'Immediate (Within a week)'),
        ('short', 'Short-term (1-2 months)'),
        ('medium', 'Medium-term (3-6 months)'),
        ('flexible', 'Flexible / No rush'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company_name = models.CharField(max_length=200, blank=True)
    service_interested = models.CharField(max_length=50, choices=SERVICE_CHOICES, blank=True)
    budget_range = models.CharField(max_length=30, choices=BUDGET_CHOICES, blank=True)
    urgency = models.CharField(max_length=20, choices=URGENCY_CHOICES, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at:%Y-%m-%d}"

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email