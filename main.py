from fpdf import FPDF

#We create a pdf object

pdf = FPDF(orientation="L", unit="mm", format="A4")

#Now we have a pdf instance

pdf.add_page() #Used to add pages

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello There!", align="L",
 ln=1, border=1)

pdf.set_font(family="Times", style="B", size=10)
pdf.cell(w=0, h=12, txt="Hi There!", align="L",
 ln=1, border=1)
pdf.output("output.pdf")