from fpdf import FPDF
import pandas as pd
#We create a pdf object

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

#Create a dataframe object

df = pd.read_csv("topics.csv")

#Now we iterate

for index, row in df.iterrows():
    pdf.add_page() #Used to add pages

    #Set the header

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
    ln=1)

    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)
    

    #Set the footer

    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


    for i in range(row["Pages"] - 1 ):
        pdf.add_page()

        #Set the footer

        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)
 
#Now we have a pdf instance

pdf.output("output.pdf")





# pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=0, h=12, txt="Hello There!", align="L",
#  ln=1, border=1)

# pdf.set_font(family="Times", style="B", size=10)
# pdf.cell(w=0, h=12, txt="Hi There!", align="L",
#  ln=1, border=1)