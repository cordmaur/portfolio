from pathlib import Path
import pandas as pd
from typing import Optional


class Consolidator:

    tables = ["oportunidade", "medio", "projetivo", "yahoo"]

    keep_columns = [
        "Qtd",
        "PM",
        "PM Adj",
        "Cotação",
        "low",
        "mean",
        "high",
        "recomendation",
        "analists",
        "DYProjetivo",
        "DYMédio",
        "YoC",
        "TetoProj",
        "TetoMean",
        "DPAProj",
        "DPAMédio",
    ]

    rename_columns = {
        "AtualN°Ações": "Qtd",
        "Preço Médio": "PM",
        "PreçoMédioAjustado": "PM Adj",
        "DPAProjetivo": "DPAProj",
        "PreçoTeto": "TetoProj",
        "PreçoTeto_mean": "TetoMean",
        "Preço Médio Ajustado": "PM Adj",
        "Atual N° Ações": "Qtd",
        "recomendation": "Recom",
    }

    def __init__(self, folder: str, tables: Optional[list] = None) -> None:

        if tables is None:
            tables = Consolidator.tables

        self.data_path = Path(folder)

        # Open the original DataFrames and leave them in a dictionary
        self.raw_dfs = {
            table: pd.read_pickle(self.data_path / f"{table}_raw.pickle").set_index(
                "Empresa"
            )
            for table in tables
        }

        # Correct the name of the "oportunidade"
        tmpdf = self.raw_dfs["oportunidade"]
        tmpdf.index = tmpdf.index.map(lambda x: x.split(" ")[-1])

        self.consolidate()

    def consolidate(self):
        self.df = self.raw_dfs["projetivo"].join(self.raw_dfs["medio"], rsuffix="_mean")

        # correct the column names for the actual dataframe and the oportunidade
        for df in [self.df, self.raw_dfs["oportunidade"]]:
            df.rename(columns=Consolidator.rename_columns, inplace=True)

        # concatenate the two AGF tables
        self.df = pd.concat([self.df, self.raw_dfs["oportunidade"]], axis=0)

        # if yahoo is present, concatenate with the yahoo recomendations
        if "yahoo" in self.raw_dfs:

            self.df = pd.concat([self.df, self.raw_dfs["yahoo"].T], axis=1)

        # Keep just the columns that exists in the DF
        keep_columns = [c for c in Consolidator.keep_columns if c in self.df.columns]

        # make the final dataframe
        self.df = self.df[keep_columns].rename(columns=Consolidator.rename_columns)
