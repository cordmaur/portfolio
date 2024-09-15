const portfolioData = [
    {
        "Stock": "ABCB4",
        "AvgPrice": 14.61,
        "Price": 23.21,
        "Qty": 3128,
        "Volume": 72600.88,
        "recomendation": 2.5,
        "low": 21.83,
        "mean": 25.02,
        "high": 28.0,
        "analists": 8,
        "Date": "2024-09-13",
        "Upside": "7.8%"
    },
    {
        "Stock": "AGRO3",
        "AvgPrice": 26.17,
        "Price": 26.72,
        "Qty": 500,
        "Volume": 13360.0,
        "recomendation": 2.5,
        "low": 29.7,
        "mean": 36.35,
        "high": 43.0,
        "analists": 2,
        "Date": "2024-09-13",
        "Upside": "36.0%"
    },
    {
        "Stock": "AURE3",
        "AvgPrice": 11.79,
        "Price": 11.11,
        "Qty": 3200,
        "Volume": 35552.0,
        "recomendation": 2.6,
        "low": 12.0,
        "mean": 14.72,
        "high": 17.0,
        "analists": 13,
        "Date": "2024-09-13",
        "Upside": "32.5%"
    },
    {
        "Stock": "BBAS3",
        "AvgPrice": 21.28,
        "Price": 28.35,
        "Qty": 4950,
        "Volume": 140332.5,
        "recomendation": 1.8,
        "low": 17.5,
        "mean": 34.0,
        "high": 45.0,
        "analists": 14,
        "Date": "2024-09-13",
        "Upside": "19.9%"
    },
    {
        "Stock": "BBSE3",
        "AvgPrice": 28.81,
        "Price": 36.42,
        "Qty": 3700,
        "Volume": 134754.0,
        "recomendation": 2.7,
        "low": 30.0,
        "mean": 37.15,
        "high": 42.0,
        "analists": 12,
        "Date": "2024-09-13",
        "Upside": "2.0%"
    },
    {
        "Stock": "BLAU3",
        "AvgPrice": 26.45,
        "Price": 13.95,
        "Qty": 500,
        "Volume": 6975.0,
        "recomendation": 3.3,
        "low": 12.0,
        "mean": 16.55,
        "high": 26.0,
        "analists": 6,
        "Date": "2024-09-13",
        "Upside": "18.6%"
    },
    {
        "Stock": "BRBI11",
        "AvgPrice": 16.15,
        "Price": 15.8,
        "Qty": 700,
        "Volume": 11060.0,
        "recomendation": 1.8,
        "low": 18.0,
        "mean": 19.14,
        "high": 20.51,
        "analists": 6,
        "Date": "2024-09-13",
        "Upside": "21.1%"
    },
    {
        "Stock": "BRKM5",
        "AvgPrice": 29.85,
        "Price": 18.19,
        "Qty": 900,
        "Volume": 16371.0,
        "recomendation": 2.7,
        "low": 20.0,
        "mean": 26.39,
        "high": 35.0,
        "analists": 9,
        "Date": "2024-09-13",
        "Upside": "45.1%"
    },
    {
        "Stock": "CSAN3",
        "AvgPrice": 13.63,
        "Price": 13.06,
        "Qty": 1100,
        "Volume": 14366.0,
        "recomendation": 2.2,
        "low": 16.5,
        "mean": 23.69,
        "high": 31.8,
        "analists": 9,
        "Date": "2024-09-13",
        "Upside": "81.4%"
    },
    {
        "Stock": "EGIE3",
        "AvgPrice": 33.9,
        "Price": 44.13,
        "Qty": 1300,
        "Volume": 57369.0,
        "recomendation": 3.3,
        "low": 38.0,
        "mean": 44.15,
        "high": 50.0,
        "analists": 13,
        "Date": "2024-09-13",
        "Upside": "0.0%"
    },
    {
        "Stock": "ELET6",
        "AvgPrice": 46.05,
        "Price": 46.17,
        "Qty": 400,
        "Volume": 18468.0,
        "recomendation": 1.9,
        "low": 53.0,
        "mean": 58.07,
        "high": 69.0,
        "analists": 7,
        "Date": "2024-09-13",
        "Upside": "25.8%"
    },
    {
        "Stock": "ETER3",
        "AvgPrice": 10.22,
        "Price": 5.81,
        "Qty": 3250,
        "Volume": 18882.5,
        "recomendation": 3.0,
        "low": null,
        "mean": null,
        "high": null,
        "analists": 0,
        "Date": "2024-09-13",
        "Upside": "nan%"
    },
    {
        "Stock": "EZTC3",
        "AvgPrice": 16.37,
        "Price": 14.22,
        "Qty": 1000,
        "Volume": 14220.0,
        "recomendation": 3.1,
        "low": 14.0,
        "mean": 19.89,
        "high": 32.0,
        "analists": 9,
        "Date": "2024-09-13",
        "Upside": "39.9%"
    },
    {
        "Stock": "FLRY3",
        "AvgPrice": 23.18,
        "Price": 16.68,
        "Qty": 2100,
        "Volume": 35028.0,
        "recomendation": 2.4,
        "low": 16.0,
        "mean": 19.06,
        "high": 22.0,
        "analists": 8,
        "Date": "2024-09-13",
        "Upside": "14.3%"
    },
    {
        "Stock": "IRBR3",
        "AvgPrice": 50.84,
        "Price": 47.74,
        "Qty": 345,
        "Volume": 16470.3,
        "recomendation": 2.6,
        "low": 29.55,
        "mean": 41.11,
        "high": 46.0,
        "analists": 5,
        "Date": "2024-09-13",
        "Upside": "-13.9%"
    },
    {
        "Stock": "ITSA3",
        "AvgPrice": 10.61,
        "Price": 11.24,
        "Qty": 4273,
        "Volume": 48028.52,
        "recomendation": 1.8,
        "low": 11.3,
        "mean": 12.75,
        "high": 14.0,
        "analists": 4,
        "Date": "2024-09-13",
        "Upside": "13.4%"
    },
    {
        "Stock": "ITSA4",
        "AvgPrice": 10.46,
        "Price": 11.25,
        "Qty": 1827,
        "Volume": 20553.75,
        "recomendation": 1.8,
        "low": 11.3,
        "mean": 12.75,
        "high": 14.0,
        "analists": 4,
        "Date": "2024-09-13",
        "Upside": "13.3%"
    },
    {
        "Stock": "KLBN11",
        "AvgPrice": 18.81,
        "Price": 21.71,
        "Qty": 3580,
        "Volume": 77721.8,
        "recomendation": 2.5,
        "low": 20.0,
        "mean": 25.79,
        "high": 31.0,
        "analists": 14,
        "Date": "2024-09-13",
        "Upside": "18.8%"
    },
    {
        "Stock": "LEVE3",
        "AvgPrice": 24.13,
        "Price": 30.85,
        "Qty": 500,
        "Volume": 15425.0,
        "recomendation": 3.0,
        "low": 33.0,
        "mean": 33.0,
        "high": 33.0,
        "analists": 1,
        "Date": "2024-09-13",
        "Upside": "7.0%"
    },
    {
        "Stock": "MOVI3",
        "AvgPrice": 19.44,
        "Price": 7.05,
        "Qty": 1000,
        "Volume": 7050.0,
        "recomendation": 2.3,
        "low": 7.0,
        "mean": 11.76,
        "high": 17.6,
        "analists": 8,
        "Date": "2024-09-13",
        "Upside": "66.8%"
    },
    {
        "Stock": "NEOE3",
        "AvgPrice": 17.24,
        "Price": 19.5,
        "Qty": 1100,
        "Volume": 21450.0,
        "recomendation": 1.8,
        "low": 26.0,
        "mean": 29.37,
        "high": 37.0,
        "analists": 10,
        "Date": "2024-09-13",
        "Upside": "50.6%"
    },
    {
        "Stock": "PETR3",
        "AvgPrice": 14.79,
        "Price": 40.82,
        "Qty": 100,
        "Volume": 4082.0,
        "recomendation": 2.2,
        "low": 43.0,
        "mean": 45.78,
        "high": 49.0,
        "analists": 8,
        "Date": "2024-09-13",
        "Upside": "12.2%"
    },
    {
        "Stock": "PETR4",
        "AvgPrice": 34.34,
        "Price": 37.18,
        "Qty": 300,
        "Volume": 11154.0,
        "recomendation": 2.2,
        "low": 33.0,
        "mean": 43.39,
        "high": 49.0,
        "analists": 10,
        "Date": "2024-09-13",
        "Upside": "16.7%"
    },
    {
        "Stock": "RDOR3",
        "AvgPrice": 44.93,
        "Price": 34.07,
        "Qty": 229,
        "Volume": 7802.03,
        "recomendation": 1.9,
        "low": 33.0,
        "mean": 37.56,
        "high": 43.0,
        "analists": 9,
        "Date": "2024-09-13",
        "Upside": "10.2%"
    },
    {
        "Stock": "SANB3",
        "AvgPrice": 13.46,
        "Price": 14.66,
        "Qty": 4500,
        "Volume": 65970.0,
        "recomendation": 3.0,
        "low": 11.615,
        "mean": 14.695,
        "high": 17.0,
        "analists": 12,
        "Date": "2024-09-13",
        "Upside": "0.2%"
    },
    {
        "Stock": "TAEE11",
        "AvgPrice": 27.19,
        "Price": 35.26,
        "Qty": 2600,
        "Volume": 91676.0,
        "recomendation": 3.8,
        "low": 28.0,
        "mean": 34.68,
        "high": 37.8,
        "analists": 10,
        "Date": "2024-09-13",
        "Upside": "-1.6%"
    },
    {
        "Stock": "TASA4",
        "AvgPrice": 12.87,
        "Price": 11.18,
        "Qty": 3200,
        "Volume": 35776.0,
        "recomendation": 2.0,
        "low": 26.94,
        "mean": 26.94,
        "high": 26.94,
        "analists": 1,
        "Date": "2024-09-13",
        "Upside": "141.0%"
    },
    {
        "Stock": "TRPL4",
        "AvgPrice": 23.0,
        "Price": 24.85,
        "Qty": 1600,
        "Volume": 39760.0,
        "recomendation": 3.5,
        "low": 14.0,
        "mean": 24.57,
        "high": 32.0,
        "analists": 12,
        "Date": "2024-09-13",
        "Upside": "-1.1%"
    },
    {
        "Stock": "TTEN3",
        "AvgPrice": 9.85,
        "Price": 12.33,
        "Qty": 1800,
        "Volume": 22194.0,
        "recomendation": 1.7,
        "low": 13.0,
        "mean": 14.74,
        "high": 17.0,
        "analists": 7,
        "Date": "2024-09-13",
        "Upside": "19.5%"
    },
    {
        "Stock": "UNIP6",
        "AvgPrice": 49.66,
        "Price": 47.2,
        "Qty": 400,
        "Volume": 18880.0,
        "recomendation": null,
        "low": 95.0,
        "mean": 95.0,
        "high": 95.0,
        "analists": 1,
        "Date": "2024-09-13",
        "Upside": "101.3%"
    },
    {
        "Stock": "VALE3",
        "AvgPrice": 67.8,
        "Price": 58.15,
        "Qty": 1440,
        "Volume": 83736.0,
        "recomendation": 2.4,
        "low": 68.3,
        "mean": 87.35,
        "high": 116.98,
        "analists": 13,
        "Date": "2024-09-13",
        "Upside": "50.2%"
    },
    {
        "Stock": "VIVT3",
        "AvgPrice": 36.77,
        "Price": 55.27,
        "Qty": 500,
        "Volume": 27635.0,
        "recomendation": 2.2,
        "low": 43.0,
        "mean": 57.85,
        "high": 64.0,
        "analists": 13,
        "Date": "2024-09-13",
        "Upside": "4.7%"
    },
    {
        "Stock": "WIZC3",
        "AvgPrice": 8.63,
        "Price": 5.99,
        "Qty": 2200,
        "Volume": 13178.0,
        "recomendation": 2.7,
        "low": 7.0,
        "mean": 8.33,
        "high": 9.5,
        "analists": 3,
        "Date": "2024-09-13",
        "Upside": "39.1%"
    }
]