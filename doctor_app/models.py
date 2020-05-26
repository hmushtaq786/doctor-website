from django.db import models
from django.conf import settings
from django.apps import apps
import datetime
from django.db.models.signals import post_save, post_init
from django.core.mail import send_mail
# Create your models here.


class Subscriber(models.Model):
    email = models.EmailField(verbose_name='Email', blank=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ClientTestimonial(models.Model):
    client_name = models.CharField(
        max_length=50, verbose_name='Client name', blank=True)
    client_testimonial = models.TextField(
        verbose_name='Client testimonial', blank=True)
    client_picture = models.ImageField(
        verbose_name='Client picture', upload_to='blogs/', blank=True, default='blogs/default-client.png')

    def __str__(self):
        return self.client_name


class FAQ(models.Model):
    question = models.CharField(
        max_length=100, verbose_name='Question', blank=True)
    answer = models.TextField(verbose_name='Answer', blank=True)

    def __str__(self):
        return self.question


class Service(models.Model):
    service_heading = models.CharField(
        max_length=40, verbose_name='Service heading', blank=True)
    service_description = models.TextField(
        verbose_name='Service description', blank=True)

    def __str__(self):
        return self.service_heading


class Blog(models.Model):
    blog_title = models.CharField(
        max_length=50, verbose_name='Blog title', blank=True)
    blog_author = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, verbose_name='Blog author')
    blog_topic = models.CharField(
        max_length=20, verbose_name='Blog topic', blank=True)
    blog_content = models.TextField(verbose_name='Blog content', blank=True)
    blog_picture = models.ImageField(
        verbose_name='Blog picture', upload_to='blogs/', null=True, blank=True, default='blogs/blog_2.jpg')
    posted_date = models.DateField(auto_now_add=True)

    @staticmethod
    def post_save(sender, instance, **kwargs):
        subscribers = Subscriber.objects.all()

        with open('email_template.txt', 'r') as temp:
            for subscriber in subscribers:
                send_mail(
                    'Blogs from Dr. Imran Adeel',
                    f'''
                        Good day!
                    ''',
                    'Dr. Imran Adeel',
                    [subscriber.email],
                    fail_silently=False,
                    html_message=email_template(instance)
                )

    def __str__(self):
        return self.blog_title


post_save.connect(Blog.post_save, sender=Blog)


class Appointment(models.Model):

    name = models.CharField(max_length=50, verbose_name='Name', blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)
    phone_number = models.CharField(
        max_length=50, verbose_name='Phone number', blank=True)
    time = models.CharField(max_length=20, verbose_name='Time', blank=True)
    date = models.DateField(verbose_name='Date', blank=True)

    def __str__(self):
        return self.name + " | "+self.date.strftime("%b %d %Y")


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
                      {}
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
                      {}
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
                              href="http://www.drimranadeel.com/blog/"
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
    return email.format(instance.blog_topic, instance.blog_content)
