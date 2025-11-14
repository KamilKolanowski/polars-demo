import polars as pl
from . import bronze as b

class TransformData:
    def __init__(self, sdr: b.SourceDataReader = b.SourceDataReader(), df: pl.DataFrame = None) -> None:
        self.df = df
        self.sdr = sdr

    def read_categories(self) -> pl.DataFrame:
        categories = (self.sdr.read_file(path="data/categories.csv")
                        .select(
                            pl.col("CategoryID").alias("CategoryId"),
                            pl.col("CategoryName")
                        )
        )

        return categories
    
    def read_cities(self) -> pl.DataFrame:
        cities = (self.sdr.read_file(path="data/cities.csv")
                        .select(
                            pl.col("CityID").alias("CityId"),
                            pl.col("CityName"),
                            pl.col("Zipcode").alias("ZipCode"),
                            pl.col("CountryID").alias("CountryId")
                        )
        )

        return cities
    
    def read_sales(self) -> pl.DataFrame:
        sales = (self.sdr.read_file(path="data/sales.csv")
                        .select(
                            pl.col("SalesID").alias("SalesId"),
                            pl.col("SalesPersonID").alias("SalesPersonId"),
                            pl.col("CustomerID").alias("CustomerId"),
                            pl.col("ProductID").alias("ProductId"),
                            pl.col("Quantity"),
                            pl.col("Discount"),
                            pl.col("TotalPrice"),
                            pl.col("SalesDate"),
                            pl.col("TransactionNumber")
                        )
        )

        return sales
    
    # def read_categories(self) -> pl.DataFrame:
    #     categories = (self.sdr.read_file(path="data/categories.csv")
    #                     .select(
    #                         pl.col("CategoryID").alias("CategoryId"),
    #                         pl.col("CategoryName")
    #                     )
    #     )

    #     return categories
    
    # def read_categories(self) -> pl.DataFrame:
    #     categories = (self.sdr.read_file(path="data/categories.csv")
    #                     .select(
    #                         pl.col("CategoryID").alias("CategoryId"),
    #                         pl.col("CategoryName")
    #                     )
    #     )

    #     return categories
    
    # def read_categories(self) -> pl.DataFrame:
    #     categories = (self.sdr.read_file(path="data/categories.csv")
    #                     .select(
    #                         pl.col("CategoryID").alias("CategoryId"),
    #                         pl.col("CategoryName")
    #                     )
    #     )

    #     return categories
