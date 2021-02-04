from scraper import Scraper
import tqdm
import pandas as pd
import pickle


class TextScraper(Scraper):
    def get_text(
        self,
        *,
        url="https://ciudadseva.com/texto/abel-y-cain-borges/",
        html_tag="div",
        html_class="text-justify"
    ):
        self.driver.get(url)
        text_metadata = self.driver.find_elements_by_xpath(
            "//" + html_tag + '[@class="' + "text-center" + '"]'
        )
        metadata = text_metadata[0].text.split("\n")
        metadata_sanit = {
            "title": metadata[0],
            "metadata": metadata[1],
            "author": metadata[2],
        }
        print("- ", metadata_sanit["title"])
        raw_text = self.driver.find_elements_by_xpath(
            "//" + html_tag + '[@class="' + html_class + '"]'
        )
        content = raw_text[0].text
        sanit_text = content.replace("\n", " ")  # for whole sentence

        return sanit_text, metadata_sanit


def build_text_dataset(*, links_file="./links.txt"):
    results = []
    scr = TextScraper()
    with open(links_file, "r") as file:
        links = file.read().split("\n")
    links = links[:-1]
    for link in tqdm.tqdm(links):
        row = {}
        sanit_text, text_metadata = scr.get_text(url=link)
        row["link"] = link
        row["text_metadata"] = text_metadata
        row["text"] = sanit_text
        results.append(row)
    return results


def run(*, save=True):
    ds = build_text_dataset()
    df = pd.DataFrame(ds)
    if save:
        with open("borges_full_texts.pkl", "wb") as f:
            pickle.dump(df, f)
            print("[INFO] Saved dataset in: ", f)
    return df


if __name__ == "__main__":
    print(">>>> Building dataset")
    run()
    print(">>>> Bye!")
