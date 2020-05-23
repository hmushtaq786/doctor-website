from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .models import Service, FAQ, ClientTestimonial, Blog, Subscriber
import datetime
from django.core.mail import send_mail

# Create your views here.


def index(request):
    appointment_form = forms.AppointmentForm()
    subscriber_form = forms.SubscriberForm()
    a_html = None
    s_html = None

    if request.method == 'POST':
        appointment_form = forms.AppointmentForm(request.POST)
        subscriber_form = forms.SubscriberForm(request.POST)
        if appointment_form.is_valid():
            appointment_form.save(commit=True)
            appointment = request.POST.copy()
            request.method = "GET2"
            send_email(appointment)
            return index(request)

        if subscriber_form.is_valid():
            subscriber_form.save(commit=True)
            request.method = "GET3"
            return index(request)

    if request.method == 'GET2':
        a_html = """
            <div id="appoint_modal" class="modal" style="display:block;">
                <div class="modal-content" style="top: 200px;">
                    <span id="appoint_close" class="close">&times;</span>
                    <p>Appointment scheduled for given time.</p>
                </div>
            </div>
        """
    if request.method == 'GET3':
        s_html = """
            <div id="subscribe_modal" class="modal" style="display:block;">
                <div class="modal-content" style="top: 200px;">
                    <span id="subscribe_close" class="close">&times;</span>
                    <p>Subscribed to the newsletter.</p>
                </div>
            </div>
        """
    data = {'page': 'Home', 'home': True, 'appointment_form': appointment_form,
            'subscriber_form': subscriber_form, 'a_html': a_html, 's_html': s_html}
    return render(request, 'index.html', context=data)


def about(request):
    subscriber_form = forms.SubscriberForm()

    s_html = None

    if request.method == 'POST':
        subscriber_form = forms.SubscriberForm(request.POST)

        if subscriber_form.is_valid():
            subscriber_form.save(commit=True)
            request.method = "GET3"
            return about(request)

    if request.method == 'GET3':
        s_html = """
            <div id="subscribe_modal" class="modal" style="display:block;">
                <div class="modal-content" style="top: 200px;">
                    <span id="subscribe_close" class="close">&times;</span>
                    <p>Subscribed to the newsletter.</p>
                </div>
            </div>
        """
    testimonials_list = ClientTestimonial.objects.order_by('client_name')
    data = {'page': 'About', 'about': True,
            'testimonials': testimonials_list, 'subscriber_form': subscriber_form, 's_html': s_html}
    return render(request, 'about.html', context=data)


def blog(request):
    subscriber_form = forms.SubscriberForm()

    s_html = None

    if request.method == 'POST':
        subscriber_form = forms.SubscriberForm(request.POST)

        if subscriber_form.is_valid():
            subscriber_form.save(commit=True)
            request.method = "GET3"
            return blog(request)

    if request.method == 'GET3':
        s_html = """
            <div id="subscribe_modal" class="modal" style="display:block;">
                <div class="modal-content" style="top: 200px;">
                    <span id="subscribe_close" class="close">&times;</span>
                    <p>Subscribed to the newsletter.</p>
                </div>
            </div>
        """
    blogs_list = Blog.objects.order_by('-posted_date')
    data = {'page': 'Blog', 'blog': True, 'blogs': blogs_list,
            'subscriber_form': subscriber_form, 's_html': s_html}
    return render(request, 'blog.html', context=data)


def services(request):
    subscriber_form = forms.SubscriberForm()

    s_html = None

    if request.method == 'POST':
        subscriber_form = forms.SubscriberForm(request.POST)

        if subscriber_form.is_valid():
            subscriber_form.save(commit=True)
            request.method = "GET3"
            return services(request)

    if request.method == 'GET3':
        s_html = """
            <div id="subscribe_modal" class="modal" style="display:block;">
                <div class="modal-content" style="top: 200px;">
                    <span id="subscribe_close" class="close">&times;</span>
                    <p>Subscribed to the newsletter.</p>
                </div>
            </div>
        """
    services_list = Service.objects.order_by('service_heading')
    faqs_list = FAQ.objects.order_by('question')
    data = {'page': 'Services', 'services': True,
            'services': services_list, 'faqs': faqs_list,  'subscriber_form': subscriber_form, 's_html': s_html}
    return render(request, 'services.html', context=data)


def contact(request):
    appointment_form = forms.AppointmentForm()
    subscriber_form = forms.SubscriberForm()

    a_html = None
    s_html = None

    if request.method == 'POST':
        appointment_form = forms.AppointmentForm(request.POST)
        subscriber_form = forms.SubscriberForm(request.POST)
        if appointment_form.is_valid():
            appointment_form.save(commit=True)
            appointment = request.POST.copy()
            request.method = "GET2"
            send_email(appointment)
            return contact(request)

        if subscriber_form.is_valid():
            subscriber_form.save(commit=True)
            request.method = "GET3"
            return contact(request)

    if request.method == 'GET2':
        a_html = """
            <div id="appoint_modal" class="modal" style="display:block;">
                <div class="modal-content" style="top: 200px;">
                    <span id="appoint_close" class="close">&times;</span>
                    <p>Appointment scheduled for given time.</p>
                </div>
            </div>
        """
    if request.method == 'GET3':
        s_html = """
            <div id="subscribe_modal" class="modal" style="display:block;">
                <div class="modal-content" style="top: 200px;">
                    <span id="subscribe_close" class="close">&times;</span>
                    <p>Subscribed to the newsletter.</p>
                </div>
            </div>
        """
    data = {'page': 'Contact', 'contact': True,  'appointment_form': appointment_form,
            'subscriber_form': subscriber_form, 'a_html': a_html, 's_html': s_html}
    return render(request, 'contact.html', context=data)


def send_email(appointment):
    send_mail(
        'Appointments for Dr. Imran Adeel',
        f'''
                        Good day!
                    ''',
        'Dr. Imran Adeel',
        ['imran_adeel17@yahoo.com'],
        fail_silently=False,
        html_message=email_template(appointment)
    )


def email_template(instance):
    email = '''
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Blogs from Dr. Imran Adeel</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <style type="text/css">
      * {{
        -ms-text-size-adjust: 100%;
        -webkit-text-size-adjust: none;
        -webkit-text-resize: 100%;
        text-resize: 100%;
      }}
      a {{
        outline: none;
        color: #40aceb;
        text-decoration: underline;
      }}
      a:hover {{
        text-decoration: none !important;
      }}
      .nav a:hover {{
        text-decoration: underline !important;
      }}
      .title a:hover {{
        text-decoration: underline !important;
      }}
      .title-2 a:hover {{
        text-decoration: underline !important;
      }}
      .btn:hover {{
        opacity: 0.8;
      }}
      .btn a:hover {{
        text-decoration: none !important;
      }}
      .btn {{
        -webkit-transition: all 0.3s ease;
        -moz-transition: all 0.3s ease;
        -ms-transition: all 0.3s ease;
        transition: all 0.3s ease;
      }}
      table td {{
        border-collapse: collapse !important;
      }}
      .ExternalClass,
      .ExternalClass a,
      .ExternalClass span,
      .ExternalClass b,
      .ExternalClass br,
      .ExternalClass p,
      .ExternalClass div {{
        line-height: inherit;
      }}
      @media only screen and (max-width: 500px) {{
        table[class='flexible'] {{
          width: 100% !important;
        }}
        table[class='center'] {{
          float: none !important;
          margin: 0 auto !important;
        }}
        *[class='hide'] {{
          display: none !important;
          width: 0 !important;
          height: 0 !important;
          padding: 0 !important;
          font-size: 0 !important;
          line-height: 0 !important;
        }}
        td[class='img-flex'] img {{
          width: 100% !important;
          height: auto !important;
        }}
        td[class='aligncenter'] {{
          text-align: center !important;
        }}
        th[class='flex'] {{
          display: block !important;
          width: 100% !important;
        }}
        td[class='wrapper'] {{
          padding: 0 !important;
        }}
        td[class='holder'] {{
          padding: 30px 15px 20px !important;
        }}
        td[class='nav'] {{
          padding: 20px 0 0 !important;
          text-align: center !important;
        }}
        td[class='h-auto'] {{
          height: auto !important;
        }}
        td[class='description'] {{
          padding: 30px 20px !important;
        }}
        td[class='i-120'] img {{
          width: 120px !important;
          height: auto !important;
        }}
        td[class='footer'] {{
          padding: 5px 20px 20px !important;
        }}
        td[class='footer'] td[class='aligncenter'] {{
          line-height: 25px !important;
          padding: 20px 0 0 !important;
        }}
        tr[class='table-holder'] {{
          display: table !important;
          width: 100% !important;
        }}
        th[class='thead'] {{
          display: table-header-group !important;
          width: 100% !important;
        }}
        th[class='tfoot'] {{
          display: table-footer-group !important;
          width: 100% !important;
        }}
      }}
    </style>
  </head>
  <body>
    <table data-module="module-3" data-thumb="thumbnails/03.png" width="100%" cellpadding="0" cellspacing="0">
      <tr>
        <td data-bgcolor="bg-module" bgcolor="#eaeced">
          <table class="flexible" width="600" align="center" style="margin: 0 auto;" cellpadding="0" cellspacing="0">
            <tr>
              <td class="img-flex">
                <img src="images/img-02.jpg" style="vertical-align: top;" width="600" height="249" alt="" />
              </td>
            </tr>
            <tr>
              <td data-bgcolor="bg-block" class="holder" style="padding: 65px 60px 50px;" bgcolor="#f9f9f9">
                <table width="100%" cellpadding="0" cellspacing="0">
                  <tr>
                    <td
                      data-color="title"
                      data-size="size title"
                      data-min="20"
                      data-max="40"
                      data-link-color="link title color"
                      data-link-style="text-decoration:none; color:#292c34;"
                      class="title"
                      align="center"
                      style="font: 30px/33px Arial, Helvetica, sans-serif; color: #292c34; padding: 0 0 24px;"
                    >
                      You have a new appointment!
                    </td>
                  </tr>
                  <tr>
                    <td
                      data-color="text"
                      data-size="size text"
                      data-min="10"
                      data-max="26"
                      data-link-color="link text color"
                      data-link-style="font-weight:bold; text-decoration:underline; color:#40aceb;"
                      align="center"
                      style="font: 16px/29px Arial, Helvetica, sans-serif; color: #888; padding: 0 0 21px;"
                    >
                      Name: {}
                      Email: {}
                      Phone: {}
                      Time: {}
                      Date: {}
                    </td>
                  </tr>
                  <tr>
                    <td style="padding: 0 0 20px;">
                      <table width="134" align="center" style="margin: 0 auto;" cellpadding="0" cellspacing="0">
                        <tr>
                          <td
                            data-bgcolor="bg-button"
                            data-size="size button"
                            data-min="10"
                            data-max="16"
                            class="btn"
                            align="center"
                            style="
                              font: 12px/14px Arial, Helvetica, sans-serif;
                              color: #f8f9fb;
                              text-transform: uppercase;
                              mso-padding-alt: 12px 10px 10px;
                              border-radius: 2px;
                            "
                            bgcolor="#f5ba1c"
                          >
                            <a
                              target="_blank"
                              style="text-decoration: none; color: #f8f9fb; display: block; padding: 12px 10px 10px;"
                              href="http://127.0.0.1:8000/admin/"
                              >See More</a
                            >
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
            <tr>
              <td height="28"></td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>
    '''
    return email.format(instance.get('name'), instance.get('email'), instance.get('phone_number'), instance.get('time'), instance.get('date'))
