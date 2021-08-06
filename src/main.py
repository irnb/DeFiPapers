from os import times
import yaml
import arxiv
import json
import time

with open("config.yaml") as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)


downloaded = []
final_result = {}

if __name__ == "__main__":
    temp_number = 1
    for topic in data["topics"]:
        print(topic)
        try:
            search = arxiv.Search(
                query=topic,
                max_results=10000000000000000,
                sort_by=arxiv.SortCriterion.SubmittedDate,
            )

            for result in search.results():
                if not result.entry_id in downloaded:
                    check = any (filter_word in result.summary for filter_word in data["filter_words"])
                    if check:
                        downloaded.append(result.entry_id)
                        final_result[temp_number] = {
                            "title": result.title,
                            "summary": result.summary,
                            "pdf url": result.pdf_url,
                            "date" : str(result.published)
                        }
                        print(temp_number, result.title)
                        temp_number = temp_number + 1
        except:
            print("ریدییییی")
            
        time.sleep(2)

    with open("results/test.json", "w") as outfile:
        json.dump(final_result, outfile)
