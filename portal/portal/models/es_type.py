from elasticsearch_dsl.connections import connections
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer
from elasticsearch_dsl import DocType, Date, Nested, Boolean, analyzer, InnerObjectWrapper, Completion, \
    Keyword, Text
connections.create_connection(hosts=['localhost'])


html_strip = analyzer('html_strip',
    tokenizer="ik_max_word",
    filter=["lowercase"],
    char_filter=["html_strip"]
)

class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}


ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])

class ArticleType(DocType):
    suggest = Completion(analyzer=ik_analyzer)
    title = Text(analyzer="ik_max_word")
    url = Keyword()
    source = Text(analyzer=html_strip)

    class Meta:
        index = "yyy1"
        settings = {
            "number_of_shards": 5,
        }


if __name__ == "__main__":
    ArticleType.init()
