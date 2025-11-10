import polars as pl

class SourceDataReader:
    def __init__(self) -> None:
        pass

    def read_file(self, path: str, sep=",") -> pl.DataFrame:
        return pl.read_csv(path, separator=sep)
    
    def read_db(self, connection: str = None) -> pl.DataFrame:
        return pl.read_database(connection=self.connection)
    
    def read_source_example(self) -> pl.DataFrame:
        pass
        # return pl.read