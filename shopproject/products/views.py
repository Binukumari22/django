from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags
from xhtml2pdf import pisa
from io import BytesIO

from .models import Product
from .forms import ProductForm

def product_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrieveproduct')
    return render(request, 'create.html', {'form': form})

def product_read(request):
    product_list = Product.objects.all()
    return render(request, 'retrieve.html', {'product_list': product_list})

def generate_pdf(request, pk):
    product = get_object_or_404(Product, pk=pk)

    template = get_template('product_pdf.html')
    html = template.render({'product': product})

    buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=buffer)

    if pisa_status.err:
        return HttpResponse('PDF creation error!')
    else:
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{product.name}.pdf"'
        return response

def send_product_email(request, pk):
    product = Product.objects.get(pk=pk)

    subject = f"New Product: {product.name}"
    from_email = "user123@gmail.com"
    recipient_list = ["your_mailtrap_inbox@mailtrap.io"]

    html_message = render_to_string('product_email.html', {'product': product})
    plain_message = strip_tags(html_message)

    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

    return HttpResponse("Email sent successfully")


