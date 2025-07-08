
import pandas as pd
import pdfplumber
import os
import json

from source.base_page import BasePage


def load_file(file_path):
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".xlsx" or extension == ".xls":
        return pd.read_excel(file_path)
    elif extension == ".csv":
        return pd.read_csv(file_path)
    elif extension == ".json":
        with open(file_path, "r") as f:
            data = json.load(f)
        return pd.DataFrame(data)
    elif extension == ".pdf":
        return load_pdf(file_path)
    else:
        raise ValueError(f"Unsupported file format: {extension}")


def load_pdf(file_path): 
    pdf_data = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                headers = table[0]
                for row in table[1:]:
                    row_dict = dict(zip(headers, row))
                    pdf_data.append(row_dict)
    return pd.DataFrame(pdf_data)


def reconcile_transactions(df1, df2):
    logger = BasePage.get_logger()

    df1["Amount"] = pd.to_numeric(df1["Amount"], errors="coerce")
    df2["Amount"] = pd.to_numeric(df2["Amount"], errors="coerce")

    merged = pd.merge(df1, df2, on="TransactionID", how="outer", suffixes=("_file1", "_file2"))

    merged["Status"] = merged.apply(
        lambda row: "Matched" if row["Amount_file1"] == row["Amount_file2"] else "Mismatched",
        axis=1
    )

    mismatched = merged[merged["Status"] == "Mismatched"]

    if not mismatched.empty:
        logger.warning("Mismatched transactions found:")
        for _, row in mismatched.iterrows():
            logger.warning(
                f"TransactionID: {row['TransactionID']}, "
                f"Amount_file1: {row['Amount_file1']}, "
                f"Amount_file2: {row['Amount_file2']}"
            )

    return merged[["TransactionID", "Amount_file1", "Amount_file2", "Status"]]
