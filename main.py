from fpdf import FPDF
import pandas as pd
#We create a pdf object

pdf = FPDF(orientation="L", unit="mm", format="A4")

#Create a dataframe object

df = pd.read_csv("topics.csv")

#Now we iterate

for index, row in df.iterrows():
    pdf.add_page() #Used to add pages

    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)

    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
    ln=1)

    pdf.line(10, 21, 200, 21)

    for i in range(row["Pages"] - 1 ):
        pdf.add_page()
    
#Now we have a pdf instance

pdf.output("output.pdf")





# pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=0, h=12, txt="Hello There!", align="L",
#  ln=1, border=1)

# pdf.set_font(family="Times", style="B", size=10)
# pdf.cell(w=0, h=12, txt="Hi There!", align="L",
#  ln=1, border=1)