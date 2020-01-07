import qrcode
import qrcode.image.svg
import sys


def qr_codes_png(begin, end):
	for i in range(begin, end):
		img = qrcode.make(i)
		file_name = str(i) + ".png"
		file_type = "PNG"
		img.save(file_name, file_type)

	count = end - begin
	print(f"{count} QRCodes generated")


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

	count = end - begin
	print(f"{count} QRCodes generated")


def qr_codes_svg(begin, end):
	factory = qrcode.image.svg.SvgImage
	for i in range(begin, end):
		img = qrcode.make(i, image_factory=factory)
		file_name = str(i) + ".svg"
		img.save(file_name)

	count = end - begin
	print(f"{count} QRCodes generated")


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

	count = end - begin
	print(f"{count} QRCodes generated")


if __name__ == '__main__':
	sys_argv_count = len(sys.argv) - 1
	
	file_type = sys.argv[1]
	begin = int(sys.argv[2])
	end = int(sys.argv[3])

	print(f"File Type: {file_type}")
	print(f"First: {begin}")
	print(f"Last: {end}")

	# Increment end to generate QRCodes until end - 1
	end = end + 1

	if(file_type == "png"):
		if(sys_argv_count == 3):
			qr_codes_png(begin, end)
		elif(sys_argv_count == 4):
			box_size = int(sys.argv[4])
			qr_codes_png_box_size(begin, end, box_size)
		else:
			print("Invalid number of arguments")
	elif(file_type == "svg"):
		if(sys_argv_count == 3):
			qr_codes_svg(begin, end)
		elif(sys_argv_count == 4):
			box_size = int(sys.argv[4])
			qr_codes_svg_box_size(begin, end, box_size)
		else: 
			print("Invalid number of arguments")
	else:
		print("Invalid file type")
