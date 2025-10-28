import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# 1️⃣ Read data
data = pd.read_csv("data.csv")

# 2️⃣ Analyze
summary = data.describe()

# 3️⃣ Create PDF
doc = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()
story = [Paragraph("Data Analysis Report", styles["Title"]), Spacer(1, 20)]

for col in summary.columns:
    story.append(Paragraph(f"<b>{col}</b>: {summary[col].to_dict()}", styles["Normal"]))
    story.append(Spacer(1, 10))

doc.build(story)
print("✅ Report saved as report.pdf")
