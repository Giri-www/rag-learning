from pipeline.rag_pipeline import RAGPipeline


def main():

    rag = RAGPipeline()

    while True:

        query = input("\nAsk question: ")

        answer, sources = rag.ask(query)

        print("\nAnswer:\n", answer)

        print("\nSources:")

        for s in sources:
            print(f"{s['source']} page {s['page']}")


if __name__ == "__main__":
    main()