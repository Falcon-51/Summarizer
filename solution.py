import pandas as pd

class Summarizer:

    def __init__(self, dataframe:pd.DataFrame, output_type:str="markdown", output_filename:str="summarized") -> None:
        """
        Инициализирует объект обобщения заданным фреймом данных и настраивает желаемый тип выходных данных.

        Параметры:
        - dataframe (pandas.core.frame.Фрейм данных): данные, которые будут обобщены.
        - output_type (str): тип итогового вывода. Поддерживается "html", "markdown" и "xlsx". По умолчанию используется "markdown".
        - output_filename (str): имя файла для сгенерированного сводного файла. По умолчанию используется "summary".

        Возвращается:
            None
        """
        self.df = dataframe
        self.output_type = output_type
        self.output_file = output_filename + '.' + output_type

        # Итоговый датафрейм для хранения результатов обобщения
        self.summary = pd.DataFrame(
                    columns=['Column', 'Type', 'Min', 'Max', 'Mean', 'Median', 'Mode', '% Zeros',
                            'Variance', 'Std Dev', 'Interquartile Range', 'Coefficient of Variation',
                            'Distinct Values'])


    def calc_summary(self):
        """
        Вычисляет всю необходимую статистику для каждого столбца во фрейме данных и сохраняет ее в атрибуте `summary` 

        Параметры:
            None

        Возвращается:
            None
        """

        # Проходим циклом по колонкам
        for column in self.df.columns:
            # Узнаём тип данных
            col_type = self.df[column].dtype
            # Если 'object', то вычисляем ограниченный набор сведений
            if col_type == 'object':
                distinct_values = self.df[column].nunique()
                mode_val = self.df[column].mode()[0]
                percent_zeros = ((self.df[column].isnull().sum()) / (len(self.df[column]))) * 100
                new_row = pd.DataFrame({'Column': [column],
                            'Type': [col_type],
                            'Mode': [mode_val],
                            '% Zeros': [percent_zeros],
                            'Distinct Values': [distinct_values]})
                # Дополняем итоговый датафрейм
                self.summary = pd.concat([self.summary if not self.summary.empty else None, new_row], ignore_index=True)

            # Если НЕ 'object', то вычисляем полный набор сведений
            else:
                min_val = self.df[column].min(skipna=True)
                max_val = self.df[column].max(skipna=True)
                mean_val = self.df[column].mean(skipna=True)
                median_val = self.df[column].median(skipna=True)
                mode_val = self.df[column].mode()[0]
                percent_zeros = ((self.df[column].isnull().sum()) / (len(self.df[column]))) * 100
                variance_val = self.df[column].var(skipna=True)
                std_dev_val = self.df[column].std(skipna=True)
                interquartile_range = self.df[column].quantile(0.75) - self.df[column].quantile(0.25)
                coefficient_of_variation = (std_dev_val / mean_val) * 100
                distinct_values = self.df[column].nunique()
                new_row = pd.DataFrame({'Column': [column],
                            'Type': [col_type],
                            'Min': [min_val],
                            'Max': [max_val],
                            'Mean': [mean_val],
                            'Median': [median_val],
                            'Mode': [mode_val],
                            '% Zeros': [percent_zeros],
                            'Variance': [variance_val],
                            'Std Dev': [std_dev_val],
                            'Interquartile Range': [interquartile_range],
                            'Coefficient of Variation': [coefficient_of_variation],
                            'Distinct Values': [distinct_values]})

                # Дополняем итоговый датафрейм
                self.summary = pd.concat([self.summary if not self.summary.empty else None, new_row], ignore_index=True)

        

    def output_save(self) -> str:
        """
            Сохраняет сгенерированный сводный отчет в формате HTML/Markdown/xlsx на диск.
            
            Параметры:
                None

            Возвращает:
                str: Файл с сохраненным итоговым отчетом.
        """

        with open(self.output_file, "w") as f:
            if self.output_type == "html":
                self.summary.to_html(f, index=False)
            elif self.output_type == "xlsx":
                self.summary.to_excel(self.output_file, index=False)
            elif self.output_type == "markdown":
                self.summary.to_markdown(f, index=False)





if __name__ == "__main__":

    # Зададим названия колонок для датафрейма
    headers = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    df = pd.read_csv('iris_data.csv', names=headers)
    
    # Инициализируем объект
    model = Summarizer(df)
    # Вычисляем сведения
    model.calc_summary()
    # Сохраняем результат
    model.output_save()

