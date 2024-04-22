import pandas as pd

class Summarizer:

    def __init__(self, dataframe:pd.DataFrame, output_type:str="markdown", output_filename:str="summarized") -> None:
        """
        Initializes the summarization object with a given DataFrame and sets up for desired output type.
        
        Parameters:
            - dataframe (pandas.core.frame.DataFrame): The data to be summarized.
            - output_type (str): Type of summary output. Currently supports "html" or "markdown". Default is "html".
            - output_type (str): Type of summary output. Options are "html" or "markdown". Default is "html".
            - output_filename (str): Filename for the generated summary file. Default is "summary".
            
        Returns:
            None
        """
        self.dataframe = dataframe
        self.output_type = output_type
        self.output_file = output_filename + '.' + output_type

        self.summary = pd.DataFrame(
                    columns=['Column Type', 'Min', 'Max', 'Mean', 'Median', 
                     'Mode', 'Percent Null', 'Variance', 'Standard Deviation', 
                     'Interquartile Range', 'Coefficient of Variation', 'Unique Values Count'])


    def calc_summary(self):
        pass
        
        
        

    def output_save(self) -> str:
        """
        Saves the generated summary report in HTML/Markdown format to disk.
        
        Parameters:
            None
            
        Returns:
            str: File with saved summary report.
        """
        
        with open(self.output_file, "w") as f:
            if self.output_type == "html":
                self.summary.to_html(f, index=False)
            elif self.output_type == "xlsx":
                self.summary.to_excel(f, index=False)
            elif self.output_type == "markdown":
                self.summary.to_markdown(f, index=False)





if __name__ == "__main__":


    headers = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    df = pd.read_csv('iris_data.csv', names=headers)
    model = Summarizer(df)
    model.output_save()

