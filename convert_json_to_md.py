from pytablewriter import MarkdownTableWriter
import json


def main():
    f = open("papers.json")
    data = json.load(f)

    value_matrix = []

    for item in data:
        temp = data[item]["summary"].find
        value_matrix.append(
            [item, data[item]["title"], data[item]["summary"][:data[item]["summary"].index(".")+1], data[item]["pdf url"]]
        )
    writer = MarkdownTableWriter(
        table_name="example_table",
        headers=["number ", "title", "first sentence of summary", "pdf url"],
        value_matrix=value_matrix,
    )
    print(writer.write_table())


if __name__ == "__main__":
    main()
