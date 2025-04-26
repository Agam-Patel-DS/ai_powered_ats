import pandas as pd

def create_excel_report(results, output_path='output_company.xlsx'):
    df = pd.DataFrame(results)
    df.to_excel(output_path, index=False)
