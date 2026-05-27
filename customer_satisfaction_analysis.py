# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF


df = pd.read_excel("customer_feedback.xlsx")

avg_rating = df.groupby("Department")["Rating"].mean()

worst_department = avg_rating.idxmin()
lowest_rating = avg_rating.min()
highest_rating = avg_rating.max()
average_rating = avg_rating.mean()


plt.style.use("dark_background")

fig, ax = plt.subplots(figsize=(11, 6))

colors = ["#00F5FF", "#FF00FF", "#39FF14", "#FFD700", "#FF4500"]

bars = ax.bar(
    avg_rating.index,
    avg_rating.values,
    color=colors[:len(avg_rating)],
    width=0.32,
    edgecolor="white",
    linewidth=1.2
)

ax.set_title(
    "Customer Satisfaction Analysis",
    fontsize=24,
    color="#00F5FF",
    weight="bold",
    pad=20
)

ax.set_xlabel(
    "Departments",
    fontsize=14,
    color="white"
)

ax.set_ylabel(
    "Average Rating",
    fontsize=14,
    color="white"
)

ax.tick_params(colors='white', labelsize=12)

ax.grid(
    color="#333333",
    linestyle="--",
    alpha=0.4
)

for spine in ax.spines.values():
    spine.set_color("white")
    spine.set_linewidth(1.5)

for bar in bars:
    yval = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width()/2,
        yval + 0.08,
        f"{yval:.2f}",
        ha='center',
        color='white',
        fontsize=12,
        weight='bold'
    )

fig.patch.set_facecolor("#050514")
ax.set_facecolor("#050514")

plt.tight_layout()

plt.savefig(
    "feedback_chart_neon.png",
    dpi=300,
    facecolor="#050514",
    bbox_inches="tight"
)

plt.close()


pdf = FPDF()
pdf.add_page()

pdf.set_fill_color(5, 5, 20)
pdf.rect(0, 0, 210, 297, "F")


pdf.set_text_color(0, 255, 255)
pdf.set_font("Arial", "B", 26)

pdf.cell(
    0,
    18,
    "CUSTOMER SATISFACTION REPORT",
    ln=True,
    align="C"
)


pdf.set_text_color(255, 255, 255)
pdf.set_font("Arial", "B", 14)

pdf.cell(
    0,
    10,
    "Automated Customer Feedback Dashboard",
    ln=True,
    align="C"
)

pdf.ln(12)



stats = [
    ("Worst Department", worst_department),
    ("Lowest Rating", f"{lowest_rating:.2f}"),
    ("Highest Rating", f"{highest_rating:.2f}"),
    ("Average Rating", f"{average_rating:.2f}")
]

box_colors = [
    (0,255,255),
    (255,0,255),
    (57,255,20),
    (255,215,0)
]

x_positions = [12, 58, 104, 150]

for i, (title, value) in enumerate(stats):

    r, g, b = box_colors[i]

    pdf.set_draw_color(r, g, b)
    pdf.set_line_width(1.6)

    pdf.rect(x_positions[i], 48, 38, 24)

    pdf.set_xy(x_positions[i], 54)

    pdf.set_text_color(255,255,255)
    pdf.set_font("Arial", "B", 8)

    pdf.multi_cell(
        38,
        4,
        title,
        align="C"
    )

    pdf.set_x(x_positions[i])

    pdf.set_text_color(r, g, b)
    pdf.set_font("Arial", "B", 13)

    pdf.cell(
        38,
        8,
        value,
        align="C"
    )



pdf.image(
    "feedback_chart_neon.png",
    x=15,
    y=90,
    w=180
)


pdf.output("customer_satisfaction_neon_report.pdf")

print("Single-page neon PDF generated successfully.")