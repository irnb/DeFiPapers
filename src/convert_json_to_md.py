from pytablewriter import MarkdownTableWriter
import json


def main():
    f = open("results/arxiv_papers_6_Aug_2021.json")
    data = json.load(f)

    value_matrix = []

    for item in data:
        temp = data[item]["summary"].find
        value_matrix.append(
            [item, data[item]["title"], data[item]["summary"][:data[item]["summary"].index(".")+1], data[item]["pdf url"],data[item]["date"][:10]]
        )
    writer = MarkdownTableWriter(
        table_name="arxiv_table(updated in 6 Aug 2021) ",
        headers=["number ", "title", "first sentence of summary", "pdf url","published"],
        value_matrix=value_matrix,
    )
    print(writer.write_table())


if __name__ == "__main__":
    main()
