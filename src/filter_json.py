import json
import time
import yaml

if __name__ == "__main__":
    final_result = {}
    last_number = 1

    with open("results/test.json", "r") as temp:
        data = json.load(temp)

    with open("config.yaml") as f:
        filter_words = yaml.load(f, Loader=yaml.SafeLoader)
        filter_words = filter_words["filter_words"]

    for item in data:
        for word in filter_words :
            if word in data[item]["summary"]:
                final_result[str(last_number)] = data[item]
                print(last_number,final_result[str(last_number)]['title'])
                last_number = last_number + 1
                time.sleep(0.01)
                break
            else:
                print("ریده بودی")
            

    with open("results/test4.json", "w") as outfile:
        json.dump(final_result, outfile)
