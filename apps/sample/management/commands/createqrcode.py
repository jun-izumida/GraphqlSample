from django.core.management.base import BaseCommand
import qrcode

class Command(BaseCommand):
    help = "Create QR Command"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--file", required=True, type=str)

    def handle(self, *args, **options):
        filename = options['file']
        with open(filename, 'r') as f:
            for v in f:
                qr_str = v.strip()
                if qr_str == '':
                    continue

                print(qr_str)
                
                qr = qrcode.QRCode(
                    version=2,
                    error_correction=qrcode.constants.ERROR_CORRECT_L
                )
                qr.add_data(qr_str)
                qr.make()
                img = qr.make_image()
                img.save("{0}.png".format(qr_str))
