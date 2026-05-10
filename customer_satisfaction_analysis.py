import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

dF= pd.read_excel ("customer_feedback.xlsx")

avg_rating= dF.groupby("Department")["Rating"].mean()

worst_department=avg_rating.idxmin()
lowest_rating=avg_rating.min()

plt.figure(figsize=(8,5))
avg_rating.sort_values().plot(
    kind="bar",
    color=["red","orange","yellow","green","blue"]

)

plt.title("Customer Satisfaction by Department")
plt.xlabel("Departments")
plt.ylabel("Average Rating")

plt.tight_layout()

plt.savefig("feedback_chart.png")
plt.close()

pdf= FPDF()
pdf.add_page()

pdf.set_font("Arial", "B", 16)
pdf.cell(0,10,"Customer Satisfaction Report", ln=True)

pdf.ln(10)

pdf.set_font("Arial","",12)

pdf.cell(
    0,
    10,
    f"Lowest Rated Department:{worst_department}",
    ln=True

)

pdf.cell(
    0,
    10,
    f"Average Rating:{lowest_rating:.2f}",
    ln=True

)

pdf.ln(10)

pdf.image("feedback_chart.png", w=170)

pdf.ln(10)

pdf.multi_cell(
    0,
    10,
    f"{worst_department} received the lowest customer satisfaction score.\n"
    "Improving customer support and service quality is recommended."
)

pdf.output("customer_satisfaction_report.pdf")

print("Report generated successfully.")