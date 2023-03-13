from django.conf import settings

def site_settings(request):
    return {
        'company_name': settings.COMPANY_NAME,
        'company_email': settings.COMPANY_EMAIL,
        'company_phone': settings.COMPANY_PHONE,
        'company_po_box': settings.COMPANY_PO_BOX,
        'company_description': settings.COMPANY_DESCRIPTION,
    }
