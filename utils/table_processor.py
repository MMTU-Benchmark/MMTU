import pandas as pd

class TableProcessor(object):
    def process(self, df: pd.DataFrame):
        return df
    
class RandomProcessor(TableProcessor):
    def __init__(self, seed: int = 42):
        super().__init__()
        self.seed = seed

    def process(self, df: pd.DataFrame):
        raise NotImplementedError
    
class ShuffleRowsProcessor(RandomProcessor):
    def process(self, df: pd.DataFrame):
        return df.sample(frac=1, random_state=self.seed)
    
class ShuffleColumnsKeepFirstThreeProcessor(RandomProcessor):
    def process(self, df: pd.DataFrame):
        if len(df.columns) <= 3:
            # If there are 3 or fewer columns, return the DataFrame as is
            return df
        # Keep first 3 columns
        first_cols = df.iloc[:, :3]

        # Shuffle the rest
        remaining_cols = df.iloc[:, 3:]
        shuffled_cols = remaining_cols.sample(frac=1, axis=1, random_state=self.seed)

        return pd.concat([first_cols, shuffled_cols], axis=1)

class ShuffleColumnsProcessor(RandomProcessor):
    def process(self, df: pd.DataFrame):
        return df.sample(frac=1, axis=1, random_state=self.seed) # type: ignore
    
class FirstNRowsProcessor(TableProcessor):
    def __init__(self, n: int):
        super().__init__()
        self.n = n

    def process(self, df: pd.DataFrame):
        return df.head(min(self.n, len(df)))


# Test
if __name__ == "__main__":
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
        'Age': [25, 30, 35, 40, 45, 50],
        'Score': [90, 85, 88, 92, 95, 91],
        'Height': [5.5, 6.0, 5.8, 5.9, 6.1, 5.7],
        'Weight': [130, 150, 160, 170, 180, 190],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia'],
        'Country': ['USA', 'USA', 'USA', 'USA', 'USA', 'USA'],
        'Occupation': ['Engineer', 'Doctor', 'Artist', 'Scientist', 'Teacher', 'Nurse'],
    }
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)

    # processors = [ShuffleRowsProcessor(), FirstNRowsProcessor(n=3), ShuffleColumnsProcessor()]
    processors = [ShuffleColumnsKeepFirstThreeProcessor(), ShuffleRowsProcessor()]
    for processor in processors:
        df = processor.process(df)
        print(f"Processor: {processor.__class__.__name__}")
        print(df)