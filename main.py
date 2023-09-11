import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline


class SearchEngine:
    def __init__(self):
        self.search_engine_url = "https://www.example.com/search?q="

    def execute_search_query(self, query):
        search_url = self.search_engine_url + query
        response = requests.get(search_url)
        if response.status_code != 200:
            raise Exception("Failed to retrieve search results")
        return response.text


class DataExtractor:
    def extract_data_from_webpage(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        relevant_data = [paragraph.text for paragraph in soup.find_all("p")]
        return relevant_data


class DataCleaner:
    def clean_and_preprocess_data(self, data):
        cleaned_data = [text.replace("<br>", "").strip() for text in data]
        return cleaned_data


class SentimentAnalyzer:
    def __init__(self):
        self.nlp_pipeline = pipeline("sentiment-analysis")

    def perform_sentiment_analysis(self, text):
        result = self.nlp_pipeline(text)
        return result


class DataAnalyzer:
    def analyze_data(self, data):
        word_count = {}
        for text in data:
            words = text.split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

        df = pd.DataFrame.from_dict(
            word_count, orient='index', columns=['Count'])
        df = df.sort_values(by='Count', ascending=False)

        return df


class DataVisualizer:
    def visualize_data(self, df):
        plt.bar(df.index[:10], df['Count'][:10])
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.title('Top 10 Most Frequent Words')
        plt.show()


class WebData:
    def __init__(self, query):
        self.search_engine = SearchEngine()
        self.data_extractor = DataExtractor()
        self.data_cleaner = DataCleaner()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.data_analyzer = DataAnalyzer()
        self.data_visualizer = DataVisualizer()

        html_content = self.search_engine.execute_search_query(query)
        extracted_data = self.data_extractor.extract_data_from_webpage(
            html_content)
        cleaned_data = self.data_cleaner.clean_and_preprocess_data(
            extracted_data)
        sentiment_analysis_result = self.sentiment_analyzer.perform_sentiment_analysis(
            cleaned_data[0])
        df = self.data_analyzer.analyze_data(cleaned_data)
        self.data_visualizer.visualize_data(df)


if __name__ == "__main__":
    query = input("Enter your query: ")
    wd = WebData(query)
