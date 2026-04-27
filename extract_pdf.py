import pdfplumber
import os

pdf_path = r'd:\project\《依托 AI 网页读取技术的大学生求职迷茫痛点挖掘与系统性解决方案研究》\当代大学生求职迷茫现状分析及解决方案指南.pdf'
output_path = r'd:\project\《依托 AI 网页读取技术的大学生求职迷茫痛点挖掘与系统性解决方案研究》\pdf_extracted.txt'

with pdfplumber.open(pdf_path) as pdf:
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"Total pages: {len(pdf.pages)}\n")
        f.write("=" * 80 + "\n\n")
        for i, page in enumerate(pdf.pages):
            f.write(f"--- Page {i+1} ---\n")
            text = page.extract_text()
            if text:
                f.write(text)
            f.write("\n\n")
            
            # Extract tables
            tables = page.extract_tables()
            if tables:
                f.write(f"[TABLES ON PAGE {i+1}]\n")
                for j, table in enumerate(tables):
                    f.write(f"  Table {j+1}:\n")
                    for row in table:
                        f.write(f"    {row}\n")
                    f.write("\n")
            
            f.write("=" * 80 + "\n\n")

print(f"Extraction complete. Output saved to: {output_path}")
