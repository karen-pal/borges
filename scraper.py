from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from sentiment_analysis_spanish import sentiment_analysis
import pandas as pd
import tqdm

sentiment = sentiment_analysis.SentimentAnalysisSpanish()


class Scraper:
    def __init__(self, browser="Firefox", headless=False):
        options = Options()
        if headless:
            options.headless = True
        if browser == "Firefox":
            from selenium.webdriver import Firefox

            self.driver = Firefox()
        # self._br.set_page_load_timeout(25)

    def __del__(self):
        print("...Closing opened drivers")
        self.close()

    def close(self):
        self.driver.close()

    # needs a re-do
    def get_links(
        self,
        *,
        url="http://ciudadseva.com/autor/jorge-luis-borges/cuentos/",
        html_tag="div",
        html_class="text-justify"
    ):
        self.driver.get(url)  #'https://ciudadseva.com/texto/abel-y-cain-borges/')
        # raw_text = self.driver.find_elements_by_xpath('//div[@class="text-justify"]')
        raw_text = self.driver.find_elements_by_xpath(
            "//" + html_tag + '[@class="' + html_class + '"]'
        )
        # content = raw_text[0].text
        return raw_text

    def get_text(
        self,
        *,
        url="https://ciudadseva.com/texto/abel-y-cain-borges/",
        html_tag="div",
        html_class="text-justify"
    ):
        self.driver.get(url)
        raw_text = self.driver.find_elements_by_xpath(
            "//" + html_tag + '[@class="' + html_class + '"]'
        )
        content = raw_text[0].text
        text_sentiment = sentiment.sentiment(content)
        # sanitized
        sanit_text = content.replace("\n", " ")  # for whole sentence
        sentences = content.split("\n")
        sent = {}
        i = 0
        for sentence in sentences:
            row = {}
            row["sentence"] = sentence
            sent_score = round(sentiment.sentiment(sentence), 4)
            row["sent_score"] = sent_score
            # print("Sentence: ", sentence, "\n has sentiment: ", sent_score,"\n")
            sent[i] = row
            i += 1
        # print("\n")
        # print("Full text sentiment:", round(sentiment.sentiment(sanit_text),4))
        return sanit_text, sent


def build_dataset(*, links_file="./links.txt"):
    results = []
    scr = Scraper()
    with open(links_file, "r") as file:
        links = file.read().split("\n")
    links = links[:-1]
    for link in tqdm.tqdm(links):
        row = {}
        sanit_text, sent_dict = scr.get_text(url=link)
        row["link"] = link
        row["text"] = sanit_text
        row["sent_dict"] = sent_dict
        results.append(row)
    return results


def run(*, save=False):
    ds = build_dataset()
    df = pd.DataFrame(ds)

    # retrieve back sentiment data
    # and structure it by text

    sentiments = []
    for i in range(len(df)):
        sent_df = pd.DataFrame.from_dict(df["sent_dict"].iloc[i], orient="index")
        sentiments.append(sent_df)

    if save:
        # save list of sentiment dfs as pickle
        with open("sentiments.pkl", "wb") as f:
            pickle.dump(sentiments, f)

        # save full df in csv
        df.to_csv("borges_df.csv", sep="#", index=False)

    # later to use
    # with open('sents.pkl', 'rb') as f:
    #    mynewlist = pickle.load(f)

    return df, sentiments_df


if __name__ == "__main__":
    print(">>>> Building dataset")
    run()
