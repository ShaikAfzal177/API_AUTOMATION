
import pytest

from source.reconciliation import load_file, reconcile_transactions
import pandas as pd

class TestFlexibleReconciliation:

    def reconcile_and_validate(self, file1: str, file2: str, output_file: str) -> pd.DataFrame:
        df1 = load_file(file1)
        df2 = load_file(file2)
        result_df = reconcile_transactions(df1, df2)

        print(f"\nReconciliation Result for {file1} vs {file2}:\n")
        print(result_df)
        result_df.to_excel(output_file, index=False)

        assert not result_df.empty, "Resulting DataFrame is empty"
        assert "Status" in result_df.columns, "'Status' column missing in result"
        return result_df
    @pytest.mark.file
    def test_excel_vs_pdf(self):
        self.reconcile_and_validate(
            "data/transactions.xlsx",
            "data/bank_statement.pdf",
            "data/result_excel_vs_pdf.xlsx"
        )

    @pytest.mark.file
    def test_csv_vs_json(self):
        self.reconcile_and_validate(
            "data/transactions.csv",
            "data/bank_statement.json",
            "data/result_csv_vs_json.xlsx"
        )

    @pytest.mark.file
    def test_json_vs_excel(self):
        self.reconcile_and_validate(
            "data/transactions.json",
            "data/bank_statement.xlsx",
            "data/result_json_vs_excel.xlsx"
        )

    @pytest.mark.file
    def test_csv_vs_pdf(self):
        self.reconcile_and_validate(
            "data/transactions.csv",
            "data/bank_statement.pdf",
            "data/result_csv_vs_pdf.xlsx"
        )
