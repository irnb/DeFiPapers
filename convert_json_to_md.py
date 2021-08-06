from pytablewriter import MarkdownTableWriter
import json


def main():
    f = open("papers.json")
    data = json.load(f)

    value_matrix = []

    for item in data:
        value_matrix.append(
            [item, data[item]["title"], data[item]["summary"], data[item]["pdf url"]]
        )
    writer = MarkdownTableWriter(
        table_name="example_table",
        headers=["number ", "title", "summary", "pdf url", "mix", "time"],
        value_matrix=value_matrix,
    )
    print(writer.write_table())


if __name__ == "__main__":
    main()
