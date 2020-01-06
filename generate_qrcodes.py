import sys
import qrcode
import qrcode.image.svg

def qr_codes_png(begin, end):
	for i in range(begin, end):
		img = qrcode.make(i)
		file_name = str(i) + ".png"
		file_type = "PNG"
		img.save(file_name, file_type)


def qr_codes_png_box_size(begin, end, box_size):
	qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=box_size,
    border=4,
)
	for i in range(begin, end):
		qr.add_data(i)
		qr.make(fit=True)
		file_name = str(i) + ".png"
		file_type = "PNG"
		img = qr.make_image(fill_color ="black", back_color="white")
		img.save(file_name, file_type)


def qr_codes_svg(begin, end):
	factory = qrcode.image.svg.SvgImage
	for i in range(begin, end):
		img = qrcode.make(i, image_factory=factory)
		file_name = str(i) + ".svg"
		img.save(file_name)


def qr_codes_svg_box_size(begin, end, box_size):
	qr = qrcode.QRCode(
	    version=1,
	    error_correction=qrcode.constants.ERROR_CORRECT_L,
	    box_size=box_size,
	    border=4,
	)

	factory = qrcode.image.svg.SvgImage
	for i in range(begin, end):
		qr.add_data(i)
		qr.make(fit=True)
		file_name = str(i) + ".svg"
		img = qr.make_image(fill_color ="black", back_color="white", image_factory=factory)
		img.save(file_name)
